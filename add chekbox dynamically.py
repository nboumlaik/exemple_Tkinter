#!/usr/bin/python
import os, sys
import threading
import Queue
from Queue import Empty
import time
from itertools import count

import Tkinter
from Tkinter import *
from Tkinter import tix
import Tkinter.tix
from Tkinter.constants import *
import traceback, Tkinter.messagebox
from Tkinter import ttk

TCL_DONT_WAIT           = 1<<1
TCL_WINDOW_EVENTS       = 1<<2
TCL_FILE_EVENTS         = 1<<3
TCL_TIMER_EVENTS        = 1<<4
TCL_IDLE_EVENTS         = 1<<5
TCL_ALL_EVENTS          = 0

class GUI(threading.Thread):

    def __init__(self):
        """ thread init
        defines some vars and starts stuff when the class is called (gui=GUI())
        """
        self.root=Tkinter.tix.Tk()
        z = self.root.winfo_toplevel()
        z.wm_title('minimal example')
        if z.winfo_screenwidth() <= 800:
            z.geometry('790x590+10+10')
        else:
            z.geometry('890x640+10+10')
        frame1 = self.MkMainNotebook()
        frame2 = self.MkMainStatus()
        frame1.pack(side=TOP, expand=1, fill=BOTH, padx=4, pady=4)
        frame2.pack(side=BOTTOM, fill=X)
        z.wm_protocol("WM_DELETE_WINDOW", lambda self=self: self.stop())

        threading.Thread.__init__(self)

    def run(self):
        """ thread start
        kick starts the main loop when the thread start()
        """
        self.root.mainloop()

    def stop(self):
        """ escape plan
        Exits gui thread
        """
        self._stop()
        raise SystemExit

    def MkMainStatus(self):
        """ status bar
        """
        top = self.root
        w = Tkinter.tix.Frame(top, relief=Tkinter.tix.RAISED, bd=1)

        self.status = Tkinter.tix.Label(w, anchor=E, bd=1)
        self.exitbutton = Tkinter.Button(w, text='Exit GUI Thread', width=20, command=lambda self=self: self.stop())

        self.print_queue=queue.Queue()
        self.print_label()

        self.status.grid(row=0, column=0, sticky=W, padx=3, pady=3)
        self.exitbutton.grid(row=0, column=1, sticky=E, padx=3, pady=3)
        return w

    def print_label(self):
        """ listner
        listner
        """
        rate=0.5 # seconds to re-read queue; 0.5=half a second, 1=a full second
        counter = count(0, rate)
        def update_func():
            secs= str(counter.__next__())
            try:
                self.status.config(text=str("%s(secs): Processing queue..." % (secs.split('.'))[0]), fg=str("red"))
                a = tix.Label(self.LogFrame, text=(self.print_queue.get(False)))
            except Empty:
                self.status.config(text=str("%s(secs): Waiting for queue..." % (secs.split('.'))[0]), fg=str("black"))
                self.status.after(int(rate*1000), update_func)
            else:
                a.pack()
                a.after(int(rate*1000), update_func)
        update_func()

    def MkMainNotebook(self):
        """ the tabs frame
        defines the tabs
        """
        top = self.root
        w = Tkinter.tix.NoteBook(top, ipadx=5, ipady=5, options="""
        tagPadX 6
        tagPadY 4
        borderWidth 2
        """)
        top['bg'] = w['bg']

        w.add('log', label='Log', underline=0)
        self.MkLog(w, 'log')
        w.add('pro', label='Progress', underline=0)
        self.MkProgress(w, 'pro')
        w.add('set', label='Settings', underline=0)
        self.MkSettings(w, 'set')
        return w

    def MkSettings(self, nb, name):
        """ TODO: settings tab
        """
        w = nb.page(name)
        options="label.width %d label.anchor %s entry.width %d" % (10, Tkinter.tix.E, 13)
        settings_scr_win = tix.ScrolledWindow(w, width=400, height=400)
        settings_scr_win.pack(side=Tkinter.tix.TOP, padx=2, pady=2, fill='both', expand=1)        
        self.SettingsFrame = settings_scr_win.window

    def MkProgress(self, nb, name):
        """ TODO: progress tab
        """
        w = nb.page(name)
        options = "label.padX 4"
        progress_scr_win = tix.ScrolledWindow(w, width=400, height=400)
        progress_scr_win.pack(side=Tkinter.tix.TOP, padx=2, pady=2, fill='both', expand=1)        
        self.ProgressFrame = progress_scr_win.window

    def MkLog(self, nb, name):
        """ log
        """
        w = nb.page(name)
        options = "label.padX 4"
        log_scr_win = tix.ScrolledWindow(w, width=400, height=400)
        log_scr_win.pack(side=Tkinter.tix.TOP, padx=2, pady=2, fill='both', expand=1)
        self.LogFrame = log_scr_win.window

def main(argv):
    """ main function
    Keyword arguments:
    args[0] -- 
    args[1] -- 
    Returns: 
    None
    """

    #GUI
    gui=GUI()
    gui.start()

    gui.print_queue.put("log")

    time.sleep(10) # timed release test
    gui.print_queue.put("timed release test")

    return None    

if __name__ == "__main__":
    sys.exit(main(sys.argv))