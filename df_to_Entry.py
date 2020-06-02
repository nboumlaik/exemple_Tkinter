#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import Tkinter
import pandas as pd
import ScrolledText

name = r'C:\Users\nboumlaik\Desktop\MultiStrategies 16M Prod Mai15.csv'

df = pd.read_csv (name, index_col = 0)
dic_entry = {}

#creation d'une nouvelle fenetre
tk_listbox = Tkinter.Tk ()
tk_listbox.title ('Les Stratégies')
scrollbar = Tkinter.Scrollbar (tk_listbox, orient="vertical")

#affecter la listbox a la nouvelle fenetre
listbox = Tkinter.Listbox (tk_listbox, width = 60, height = 30, yscrollcommand = scrollbar.set)
scrollbar.config (command = listbox.yview)
scrollbar.pack (side = "right", fill = "y")
listbox.pack (side = "left",fill = "both", expand = True)

#EXTENDED: pour selectioner plusierus items
# listbox.config (selectmode = Tkinter.EXTENDED)
# listbox.pack ()

b = Tkinter.Button (tk_listbox, text ='Afficher la stratégie', command = lambda : show_strat (df))
b.pack ( expand = 1, padx = 5, pady = 5)

for item in df.index.tolist ():
    listbox.insert (Tkinter.END, item)

def show_strat (df):
    root = Tkinter.Toplevel ()
    selection = [listbox.get (listbox.curselection ())]
    
    df_sel = df.loc [selection].copy ()

    for c in df_sel.columns:

        label = Tkinter.Label (root, text = c)
        label.pack (padx = 5, pady = 5)
        
        if len (str (df_sel [c].values[0]) )> 10:
            e = ScrolledText.ScrolledText(root, wrap=Tkinter.WORD, width = 40, height = 5)
            e.pack (padx = 5, pady = 5)
            e.insert(Tkinter.INSERT, df_sel [c].values[0])
            dic_entry [c] = e
            
        else:
            dic_entry [c] = Tkinter.StringVar()
            e = Tkinter.Entry (root, textvariable = dic_entry [c])#, width = 40, bg = 'white')
            e.pack (padx = 5, pady = 5)
            dic_entry [c].set (df_sel [c].values[0])
            #print df_sel [c].values
    root.grid ()

Tkinter.mainloop ()