from Tkinter import *

counter = 0
def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))

root = Tk()

menubar = Menu(root)

menu = Menu(menubar, tearoff=0)
menu.add_command(label=str(counter))
menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Test", menu=menu)

def popup(event):
    menu.post(event.x_root, event.y_root)
    menu.grab_release ()
    menu.add_command (label=str(counter))

# attach popup to canvas
root.bind("<Button-3>", popup)

root.config(menu=menubar)
mainloop()