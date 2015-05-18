import Tkinter as tk
import threading
import Queue
import ttk
import time




class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.queue = Queue.Queue()
        self.listbox = tk.Listbox(self, width=20, height=5)
        self.progressbar = ttk.Progressbar(self, orient='horizontal',
                                           length=300, mode='determinate')
        self.button = tk.Button(self, text="Start", command=self.spawnthread)
        self.listbox.pack(padx=10, pady=10)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)
    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()
    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")
    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.listbox.insert('end', msg)
                self.progressbar.step(25)
            except Queue.Empty:
                pass


class ThreadedClient(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue 
    def run(self):
        for x in xrange(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


app = App()
app.mainloop()
