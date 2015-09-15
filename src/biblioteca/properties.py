# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Jose Diaz"
__date__ = "$04/04/2015 03:52:11 AM$"

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
    

class Properties(object):
    """docstring for Properties"""
    BACKGROUND_DARK = '#121314'
    BACKGROUND_LIGHT = '#1a1e21'
    FOREGROUND_DARK = '#ADAFB2'
    FOREGROUND_LIGHT = '#DFE0E6'
    FONT_TITULO = ('Arial', 24, 'bold')
    FONT_SMALL = ('Purisa', 9)
    FONT_MEDIUM = ('Purisa', 11)
    FONT_LARGE = ('Purisa', 12)
    HIGHLIGHT_BG = '#252a2d'
    HIGHLIGHT_FG = '#FFFFFF'
    HIGHLIGHT_FG_GREEN = '#21a341'
    
    
    BUTTONSTYLE = dict(font=FONT_SMALL, relief=FLAT, bd=0,  width=12, 
                    bg=HIGHLIGHT_BG, fg=FOREGROUND_DARK, activebackground='#2a3136', 
                    activeforeground=HIGHLIGHT_FG, highlightbackground=BACKGROUND_DARK, highlightthickness=1)
                    
    BUTTONSTYLE_GREEN = dict(font=FONT_MEDIUM, relief=FLAT, bd=0,  width=10, bg=HIGHLIGHT_FG_GREEN, 
                    fg=HIGHLIGHT_FG, activebackground='#26bf4c', 
                    activeforeground=HIGHLIGHT_FG, highlightbackground=BACKGROUND_DARK, highlightthickness=1)
                    
    BUTTONCLOSE = dict(font=FONT_LARGE, relief=FLAT, bd=0, fg=FOREGROUND_DARK, 
            activebackground=BACKGROUND_LIGHT, activeforeground='red')
    
    def __init__(self, master):
        self.master = master
        self.properties = self.create_properties(self.master)
        self.properties.pack(fill=BOTH, expand=YES)
        
    def create_properties_titlebar(self, master):
        properties_titlebar = Frame(master, bg=master['bg'])
        Frame(properties_titlebar, bg=self.BACKGROUND_DARK).pack(side=BOTTOM, fill=X)
        Label(properties_titlebar, text='Properties', font=self.FONT_MEDIUM, bg=properties_titlebar['bg'], fg=self.HIGHLIGHT_FG).pack(side=LEFT, anchor=W, padx=5, pady=2)
        btn_close = Menubutton(properties_titlebar, text='x', bg=properties_titlebar['bg'], **self.BUTTONCLOSE)
        btn_close.pack(side=RIGHT, anchor=E, padx=2, pady=2)
        btn_close.bind("<Button-1>", lambda e: self.exit_properties())
        return properties_titlebar
        
    def create_properties(self, master):
        """Toolbar right"""
        properties = Frame(master, bg=self.BACKGROUND_LIGHT)
        
        titlebar = self.create_properties_titlebar(properties)
        titlebar.pack(side=TOP, fill=X)
        
        return properties
    
    def exit_properties(self):
        self.master.destroy()
        
        

if __name__ == "__main__":
    root = Tk()
    Properties(root)
    root.mainloop()
