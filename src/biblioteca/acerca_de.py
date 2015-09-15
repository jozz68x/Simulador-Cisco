#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jose Diaz"
__credits__ = ["person_1", "person_2", "person_3", "person_n"]
__copyright__ = "Copyright (C) 2015, Jose Diaz"
__license__ = "GPL"
__version__ = "1.1"
__revision__ = "8"
__date__ = "$23/02/2015 08:52:56 AM$"
__status__ = "Desarrollo"
__maintainer__ = "Jose Diaz"
__contact__ = "966403361"
__email__ = "jozz.18x@gmail.com"

from tkinter import *
from tkinter import ttk
from biblioteca.centerWindow import center_window

class AcercaDe(Toplevel):
    """
    Acerca del software
    """
    def __init__(self, parent, width, height, text1="", text2="", bg="white", fg="black", button=False, title=None, overrideredirect=False):
        Toplevel.__init__(self, parent)
        self.parent= parent
        
        self.wm_withdraw()
        self.configure(borderwidth=0)
        
        center_window(self, width, height, windowsbar=True)
        
        self.wm_title(title or 'Acerca de')
        self.parent.wm_attributes("-alpha", 0.9)
        self.parent.wm_attributes("-transparentcolor", "purple")
        
        self.create_widgets(text1, text2, bg, fg, overrideredirect, button)
        
        self.overrideredirect(overrideredirect)
        self.resizable(height=FALSE, width=FALSE) # don't allow resizing yet
        self.transient(self.parent)
        self.focus_set()
        
        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.bind("<Return>", self.exit)
        self.bind("<Escape>", self.exit)
        
        # wait for window to be generated
        self.update()
        # now allow resizing
        self.resizable(height=TRUE, width=TRUE)

        self.wm_deiconify()
        
        self.grab_set()
        
    def create_widgets(self, text1, text2, bg, fg, overrideredirect, btn):
        """Create the dialog's widgets."""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)

        borde = Frame(self, bg=bg, highlightbackground="BLACK", highlightthickness=1)
        borde.pack(fill=BOTH, expand=True)
        
        if overrideredirect:
            head = Frame(borde, bg='#121314')
            btn_close = Menubutton(head, text='X', bg=head['bg'], fg='white', relief=FLAT, bd=0, 
                            activebackground=head['bg'], activeforeground='red', font=('Purisa', 14))
            btn_close.pack(side=RIGHT, padx=10)
            btn_close.bind('<Button-1>', lambda e: self.exit())
            head.pack(side=TOP, fill=X)
        else:
            pass
            
        
        if btn:
            footer = Frame(borde, bg='#121314')
            btn_ok = Menubutton(footer, text="Aceptar", width=10, font=('Purisa', 10),
                    relief=FLAT, bd=0, bg='#282d32', fg='white',
                    activebackground='#373d45', activeforeground='white',
                    highlightbackground="BLACK", highlightthickness=1)
            btn_ok.pack(side=RIGHT, padx=10, pady=5, ipady=2)
            btn_ok.bind('<Button-1>', lambda e: self.exit())
            footer.pack(side=BOTTOM, fill=X)
        else:
            pass
          
        body = Frame(borde, bg=borde['bg'])
        body.pack(fill=BOTH, expand=1)
        
        Label(body, text=text1, font=("Arial", 20), justify="center", 
                        bg=body['bg'], fg=fg).pack()
        Label(body, text=text2, font=("Arial", 11), justify="center", 
                        bg=body['bg'], fg=fg).pack()
    
    def exit(self, event=None):
        self.parent.wm_attributes("-alpha", 1)
        self.destroy()
        
                        
        
def main():
    def about(win):
        AcercaDe(win, width=360, height=200, text1="Titulo", text2="lineas de texto.")
        
    root = Tk()
    ttk.Button(root, text="Open About", command=lambda: about(root)).pack(anchor=CENTER, padx=10, pady=20)
    root.mainloop()

#main()
    
        