##from Tkinter import *
##import ttk
## 
##root = Tk()
## 
##tree = ttk.Treeview(root)
## 
##tree["columns"]=("one","two")
##tree.column("one", width=100 )
##tree.column("two", width=100)
##tree.heading("one", text="coulmn A")
##tree.heading("two", text="column B")
## 
##tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
## 
##id2 = tree.insert("", 1, "dir2", text="Dir 2")
##tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
## 
####alternatively:
##tree.insert("", 3, "dir3", text="Dir 3")
##tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))
## 
##tree.pack()
##root.mainloop()



try:
    from Tkinter import *
    import ttk
except:
    from tkinter import *
    from tkinter import ttk
 
ROWS = [('Dupont', 'Jean', 12356), ('Doe', 'John', 6789), ('Chaplin', 'Charlie', 67891)]
 
fenetre = Tk()
 
def on_click(event):
    seltxt = tv.set(tv.selection(), 'col1') or 'None'
    labsel.configure(text=seltxt)
    selfocus = tv.set(tv.focus(), 'col1') or 'None'
    labfocus.configure(text=selfocus)
 
frm = Frame(fenetre)
labseltitle = Label(frm, text='selection')
labseltitle.grid(row=0, column=0, sticky=E+W, padx=5)
labsel = Label(frm, text='None')
labsel.grid(row=1, column=0, sticky=E+W, padx=5)
labfocustitle = Label(frm, text='focus')
labfocustitle.grid(row=0, column=1, sticky=E+W, padx=5)
labfocus = Label(frm, text='None')
labfocus.grid(row=1, column=1, sticky=E+W, padx=5)
frm.pack(fill=Y)
# la creation de la TreeView 
tv = ttk.Treeview(fenetre, show='headings',  height=3, selectmode='browse')
tv["columns"]=("col1", "col2", "col3")
tv.column("col1", width=80, anchor="center")
tv.column("col2", width=80, anchor="center")
tv.column("col3", width=110, anchor="center")
tv.heading("col1", text="Nom")
tv.heading("col2", text="Prenom")
tv.heading("col3", text="Phone number")
tv.pack()
for row in ROWS:
    tv.insert('','end', text=row[0], values=row, tags=('mb3_click',))
tv.bind("<Button-1>", on_click)
#tv.bind("<Button-3>", on_click)
tv.tag_bind('mb3_click', '<3>', on_click)
Button(fenetre, text='Test', command=lambda: on_click(None)).pack()
 
fenetre.mainloop()try:
    from Tkinter import *
    import ttk
except:
    from tkinter import *
    from tkinter import ttk
 
ROWS = [('Dupont', 'Jean', 12356), ('Doe', 'John', 6789), ('Chaplin', 'Charlie', 67891)]
 
fenetre = Tk()
 
def on_click(event):
    seltxt = tv.set(tv.selection(), 'col1') or 'None'
    labsel.configure(text=seltxt)
    selfocus = tv.set(tv.focus(), 'col1') or 'None'
    labfocus.configure(text=selfocus)
 
frm = Frame(fenetre)
labseltitle = Label(frm, text='selection')
labseltitle.grid(row=0, column=0, sticky=E+W, padx=5)
labsel = Label(frm, text='None')
labsel.grid(row=1, column=0, sticky=E+W, padx=5)
labfocustitle = Label(frm, text='focus')
labfocustitle.grid(row=0, column=1, sticky=E+W, padx=5)
labfocus = Label(frm, text='None')
labfocus.grid(row=1, column=1, sticky=E+W, padx=5)
frm.pack(fill=Y)
# la creation de la TreeView 
tv = ttk.Treeview(fenetre, show='headings',  height=3, selectmode='browse')
tv["columns"]=("col1", "col2", "col3")
tv.column("col1", width=80, anchor="center")
tv.column("col2", width=80, anchor="center")
tv.column("col3", width=110, anchor="center")
tv.heading("col1", text="Nom")
tv.heading("col2", text="Prenom")
tv.heading("col3", text="Phone number")
tv.pack()
for row in ROWS:
    tv.insert('','end', text=row[0], values=row, tags=('mb3_click',))
tv.bind("<Button-1>", on_click)
#tv.bind("<Button-3>", on_click)
tv.tag_bind('mb3_click', '<3>', on_click)
Button(fenetre, text='Test', command=lambda: on_click(None)).pack()
 
fenetre.mainloop()
