import Tkinter as tk
import tkMessageBox

root = tk.Tk()

def on_closing():
    print "c'est fermer"
    root.destroy ()
    
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()