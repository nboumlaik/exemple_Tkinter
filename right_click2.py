import Tkinter

def context_menu(event, menu):
    widget = event.widget
    index = widget.nearest(event.y)
    _, yoffset, _, height = widget.bbox(index)
    if event.y > height + yoffset + 5: # XXX 5 is a niceness factor :)
        # Outside of widget.
        return
    item = widget.get(index)
    print "Do something with", index, item
    menu.post(event.x_root, event.y_root)

root = Tkinter.Tk()
aqua = root.tk.call('tk', 'windowingsystem') == 'aqua'

menu = Tkinter.Menu()
menu.add_command(label=u'hi')

listbox = Tkinter.Listbox()
listbox.insert(0, *range(1, 10, 2))
listbox.bind('<2>' if aqua else '<3>', lambda e: context_menu(e, menu))
listbox.pack()
root.mainloop()