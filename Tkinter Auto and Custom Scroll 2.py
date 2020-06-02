# Test Code for Tkinter with threads
import Tkinter
import threading
import Queue
import time

# Data Generator which will generate Data
def GenerateData(q):
    for i in range(1000000):
        #print "Generating Some Data, Iteration %s" %(i)
        time.sleep(0)
        q.put("Some Data from iteration %s. Putting this data in the queue for testing" %(i))

# Queue which will be used for storing Data
q = Queue.Queue()

def QueueHandler():
    global widinst, q
    linecount = 0
    if not q.empty():
        str = q.get()
        linecount = linecount + 1
        widinst.configure(state="normal")
        str = str + "\n"
        widinst.insert("end", str)
        if linecount > 100:
            widinst.delete('1.0', '2.0')
            linecount = linecount - 1
        widinst.see('end')
        widinst.configure(state="disabled")
        tk.after(1,QueueHandler)

# Create a thread and run GUI & QueueHadnler in it
tk = Tkinter.Tk()
scrollbar = Tkinter.Scrollbar(tk)
scrollbar.pack(side='right', fill='y' )
text_wid = Tkinter.Text(tk,yscrollcommand=scrollbar.set)
text_wid.pack()
t1 = threading.Thread(target=GenerateData, args=(q,))
#t2 = threading.Thread(target=QueueHandler, args=(text_wid,q))
#t2.start()
widinst = text_wid
t1.start()
tk.after(1,QueueHandler)
tk.mainloop()
