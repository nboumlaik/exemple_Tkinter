import re,sys,time
from Tkinter import *
import Tkinter
import threading
import traceback
import Queue


class ReaderThread(threading.Thread): 
    def __init__(self, root, queue):
        print "Thread init"
        threading.Thread.__init__(self) 
        self.root = root
        self.running = True
        self.q = queue

    def stop(self):
        print "Stopping thread"
        running = False

    def run(self):
        print "Thread started"
        time.sleep(5)

        try:
            while(self.running):
                # emulating delay when reading from serial interface
                time.sleep(0.05)
                curline = "the quick brown fox jumps over the lazy dog\n"

                try:
                    self.q.put(curline)
                    self.root.event_generate('<<AppendLine>>', when='tail')
                # If it failed, the window has been destoyed: over
                except TclError as e:
                    print e
                    break

        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print "Exception in receiver thread, stopping..."
            pass
        print "Thread stopped"


class Transformer:
    def __init__(self):
        self.q = Queue.Queue()
        self.lineIndex = 1
        pass

    def appendLine(self, event):
        line = self.q.get_nowait()

        if line == None:
            return

        i = self.lineIndex
        curIndex = "1.0"
        lowerEdge = 1.0
        pos = 1.0

        # get cur position
        pos = self.scrollbar.get()[1]

        # Disable scrollbar
        self.text.configure(yscrollcommand=None, state=NORMAL)

        # Add to text window
        self.text.insert(END, str(line))
        startIndex = repr(i) + ".0"
        curIndex = repr(i) + ".end"

        # Perform colorization
        if i % 6 == 0:
            self.text.tag_add("warn", startIndex, curIndex)
        elif i % 6 == 1:
            self.text.tag_add("debug", startIndex, curIndex)                            
        elif i % 6 == 2:
            self.text.tag_add("info", startIndex, curIndex)                         
        elif i % 6 == 3:
            self.text.tag_add("error", startIndex, curIndex)                            
        elif i % 6 == 4:
            self.text.tag_add("fatal", startIndex, curIndex)                            
        i = i + 1

        # Enable scrollbar
        self.text.configure(yscrollcommand=self.scrollbar.set, state=DISABLED)

        # Auto scroll down to the end if scroll bar was at the bottom before
        # Otherwise allow customer scrolling                        

        if pos == 1.0:
            self.text.yview(END)

        self.lineIndex = i

    def start(self):
        """starts to read linewise from self.in_stream and parses the read lines"""
        count = 1
        self.root = Tk()
        self.root.title("Tkinter Auto-Scrolling Test")#
        self.root.bind('<<AppendLine>>', self.appendLine)
        self.topPane = PanedWindow(self.root, orient=HORIZONTAL)
        self.topPane.pack(side=TOP, fill=X)
        self.lowerPane = PanedWindow(self.root, orient=VERTICAL)

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(wrap=WORD, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        # Color definition for log levels
        self.text.tag_config("debug",foreground="gray50")
        self.text.tag_config("info",foreground="green")
        self.text.tag_config("warn",foreground="orange")
        self.text.tag_config("error",foreground="red")
        self.text.tag_config("fatal",foreground="#8B008B")
        # set default color
        self.text.config(background="black", foreground="gray");
        self.text.pack(expand=YES, fill=BOTH)       

        self.lowerPane.add(self.text)
        self.lowerPane.pack(expand=YES, fill=BOTH)

        t = ReaderThread(self.root, self.q)
        print "Starting thread"
        t.start()

        try:
            self.root.mainloop()
        except Exception as e:
            print "Exception in window manager: ", e

        t.stop()
        t.join()


if __name__ == "__main__":
    try:
        trans = Transformer()
        trans.start()
    except Exception as e:
        print "Error: ", e
        sys.exit(1)  
