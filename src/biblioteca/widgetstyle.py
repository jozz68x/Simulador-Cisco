# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Jose Diaz"
__date__ = "$03/04/2015 11:31:26 PM$"

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

class ButttonStyle(Button):
    '''Tkinter Button Style.'''
    
    def __init__(self, parent, *args, **kw):
        Button.__init__(self, parent, *args, **kw)
        
        self.bind('<Enter>', lambda e: self.configure(background='#26bf4c'))
        self.bind('<Leave>', lambda e: self.configure(background='#21a341'))

class MenubuttonStyle(Menubutton):
    '''Tkinter Button Style.'''
    
    def __init__(self, parent, *args, **kw):
        Menubutton.__init__(self, parent, *args, **kw)
        
        self.bind('<Enter>', lambda e: self.configure(highlightbackground='#15AE1F', highlightthickness=1))
        self.bind('<Leave>', lambda e: self.configure(highlightbackground='#121314', highlightthickness=1))
        
class EntryStyle(Entry):
    '''Tkinter Button Style.'''
    
    def __init__(self, parent, *args, **kw):
        Entry.__init__(self, parent, *args, **kw)
        
        self.bind('<Enter>', lambda e: self.configure(highlightbackground='#15AE1F', highlightcolor="#15AE1F", highlightthickness=1))
        self.bind('<Leave>', lambda e: self.configure(highlightbackground='#121314', highlightcolor="#121314", highlightthickness=1))
        

if __name__ == "__main__":
    print ("Hey Hello")
