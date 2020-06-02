import Tkinter as tk
import threading
import Queue
import ttk

import matplotlib
import pandas as pd
import numpy as np
import os


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
        self.thread = Threaded(self.queue)
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


class Threaded(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue 
    def run(self):  
        path_all = r'C:\Users\nboumlaik\figures'
        for path_f in os.listdir (path_all):
            path_f = '\\' + path_f
            df = pd.read_csv(path_all+path_f, index_col = 0)
            name = path_f.split() [-1]
            self.to_map (df, path_save=path_all+name [:-4], title=name)
            msg = "file %s maped..." % name
            self.queue.put(msg)
    def to_map (self, df, path_save, title, format_fig = '.png', normalize = False):
    
        try:
            df = df.drop ('TIME_V!MOIS')
        except:
            pass
        del df ['Total']
        #self.fillna(value = 0.0, inplace = True)
    
        # Normalize data columns
        if normalize:
            df_norm = (df - df.mean ()) / (df.max () - df.min ())
        else:
            df_norm = df
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        # Plot it out
        fig = plt.gcf ()
        ax = fig.add_subplot (111)
        nbval = sum (np.sum (pd.notnull (df_norm), axis = 1))
        nbbool_pos = sum (np.sum (np.greater (df_norm, 0), axis = 1))
        nbbool_neg = nbval - nbbool_pos
        if nbbool_pos == nbval:
            color_cmap = plt.cm.Blues    
        elif nbbool_neg == nbval:
            color_cmap = plt.cm.Reds_r
        else:
            color_cmap = 'RdBu'
        df_norm.fillna (value = 0.0, inplace = True)
        try:
            heatmap = ax.pcolor (df_norm, cmap = color_cmap, alpha = 0.8)
        except:
            return    
        # Format
        fig.set_size_inches (20, 20)
        plt.subplots_adjust(left = 0.35, bottom = -0.01, right = 0.65, top=  None,
                        wspace = None, hspace = None)
        
        # turn off the frame
        ax.set_frame_on (False)
    
        # put the major ticks at the middle of each cell
        ax.set_yticks (np.arange(df_norm.shape [0]) + 0.5, minor = False)
        ax.set_xticks (np.arange(df_norm.shape [1]) + 0.5, minor = False)
    
        # want a more natural, table-like display
        ax.invert_yaxis ()
        ax.xaxis.tick_top ()
    
        # Set the labels
    
        # labels
        labels = df.columns
        # note I could have used df_sort.columns but made "labels" instead
        ax.set_xticklabels (labels, minor = False)
        ax.set_yticklabels (df_norm.index, minor = False)
        #Taille des etiquettes de l'axe des y
        #ax.tick_params(axis='y', labelsize=6)
        #ax.tick_params(axis='x', labelsize=10)
        fig.suptitle (title, fontsize = 25, fontweight = 'bold')
        #rotate the
        #plt.xticks (rotation = 35)
    
        for t in ax.xaxis.get_major_ticks ():
            t.tick1On = False
            t.tick2On = False
        for t in ax.yaxis.get_major_ticks ():
            t.tick1On = False
            t.tick2On = False
            
        plt.colorbar(mappable=heatmap, shrink=.5, pad=.2, aspect=10)
        fig.set_size_inches (30,25)
        fig.savefig (path_save + format_fig, dpi=100)
        plt.close(fig)
        return


app = App()
app.mainloop()
