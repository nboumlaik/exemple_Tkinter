"""This module provides

* a small  collection (about 16%) of the colors found in the usual X11 color
data base

* ThemeFrame that frames a group of widger
* LabelEntry  an entry box with an associated label
* FilenameEntry an entry box for file with a browser button.

"""
from Tkinter import *
import string

from FileDialog import LoadFileDialog

# A small collection (about 16%) of the colors found in the usual X11 color
# data base:  .../lib/X11/rgb.txt

X11COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
          'old lace', 'linen', 'antique white', 'papaya whip',
          'blanched almond', 'bisque', 'peach puff', 'navajo white',
          'moccasin', 'cornsilk', 'ivory', 'lemon chiffon', 'seashell',
          'honeydew', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'white', 'black', 'dark slate gray',
          'dark slate grey', 'dim gray', 'dim grey', 'slate gray',
          'slate grey', 'light slate gray', 'light slate grey', 'gray',
          'grey', 'light grey', 'light gray', 'midnight blue', 'navy',
          'navy blue', 'cornflower blue', 'dark slate blue', 'slate blue',
          'medium slate blue', 'light slate blue', 'medium blue',
          'royal blue', 'blue', 'dodger blue', 'deep sky blue', 'sky blue',
          'light sky blue', 'steel blue', 'light steel blue', 'light blue',
          'powder blue', 'pale turquoise', 'dark turquoise',
          'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue',
          'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green',
          'light sea green', 'pale green', 'spring green', 'lawn green',
          'green', 'chartreuse', 'medium spring green', 'green yellow',
          'lime green', 'yellow green', 'forest green', 'olive drab',
          'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod',
          'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
          'sienna', 'peru', 'burlywood', 'beige', 'wheat', 'sandy brown',
          'tan', 'chocolate', 'firebrick', 'brown', 'dark salmon', 'salmon',
          'light salmon', 'orange', 'dark orange', 'coral', 'light coral',
          'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
          'light pink', 'pale violet red', 'maroon', 'medium violet red',
          'violet red', 'magenta', 'violet', 'plum', 'orchid',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
          'purple', 'medium purple', 'thistle', 'dark grey', 'dark gray',
          'dark blue', 'dark cyan', 'dark magenta', 'dark red', 'light green']

X11COLORS.sort(lambda a,b: cmp(string.split(a)[-1], string.split(b)[-1]))

class ThemeFrame(Frame):
    """A frame to ground widget
    
    see: __init__(self, master,color)

     """
    def __init__(self, master,color):
        """Frame with a standard display. Only color can be changed."""
        Frame.__init__(self, master, relief=RAISED, bd=2)
        l = Label(self, text=self.label, font=('Helvetica', 12, 'italic bold'),
                  background=color, foreground='white')
        l.pack(side=TOP, expand=NO, fill=X)


class LabelEntry(Frame):
    """ LabelEntry :
    A label + an entry + a browser button to choose a filename or enter it.
    
    see:   __init__(self, master, text,mytitle,var)
           get(self)

    """
    def __init__(self, master, text,mytitle,var):
        """
        text is the text of the label
        mytitle is the value of the string
        var is a global variable (or An application variable) to store the value
        """
        Frame.__init__(self, master)
        Label(self, text=text).pack(side=LEFT)
        self.entry = StringVar()
        self.entry.set(mytitle)
        Entry(self,width=40, textvariable=var).pack(side=LEFT, fill=X)

    def get(self):
        """ return the value of the LabelEntry"""
        return self.entry.get()

class FilenameEntry(Frame):
    """ FilenameEntry:
    A label + an entry + a browser button to choose a filename or enter it.

    see:   __init__(self, master, text,var)
           get(self)
           
           browse(self) if you wante to change the pattern or the type

    """
    def __init__(self, master, text,var):
        Frame.__init__(self, master)
        Label(self, text=text).pack(side=LEFT)
        self.filename = var
        Entry(self,width=40, textvariable=self.filename).pack(side=LEFT, fill=X)
        Button(self, text="Browse...", command=self.browse).pack(side=RIGHT)

    def browse(self):
        file = LoadFileDialog(self).go(pattern='*')
        if file:
            self.filename.set(file)

    def get(self):
        return self.filename.get()