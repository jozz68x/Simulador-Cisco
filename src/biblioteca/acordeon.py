'''The Accordion widget inherits from Tkinter's Frame class and provides stacked
expandable and collapseable containers for displaying other widgets.

Compliant with Python 2.5-2.7

Author: @ifthisthenbreak
'''

'''
modificado por Jose Diaz
Modificaciones:
    colores personalizados
    se agrego:
        cursor
        font
        evento activebackground
'''

from tkinter import Tk, Frame, PhotoImage, Label


class Chord(Frame):
    '''Tkinter Frame with title argument'''
    def __init__(self, parent, title='', *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        self.title = title
        

class Accordion(Frame):
    def __init__(self, parent, accordion_style=None, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # if no style dict, assign default style
        if accordion_style:
            self.style = accordion_style
        else:
            self.style = accordion_style = {
                'title_bg': '#263238',
                'title_fg': 'white',
                'highlight': '#00887a',
                'highlight_fg': 'white',
                'cursor': 'arrow'
                }
        self.columnconfigure(0, weight=1)
        
    def append_chords(self, chords=[]):
        '''pass a [list] of Chords to the Accordion object'''

        self.update_idletasks()
        row = 0
        width = max([c.winfo_reqwidth() for c in chords])
        
        for c in chords:
            i = PhotoImage() # blank image to force Label to use pixel size
            label = Label(self, text=c.title,
                          image=i,
                          compound='center',
                          width=width,
                          anchor='w',
                          font=('Franklin Gothic Book', 11),
                          bg=self.style['title_bg'],
                          fg=self.style['title_fg'],
                          cursor=self.style['cursor'],
                          bd=1, relief='flat')
            
            label.grid(row=row, column=0, sticky='nsew')
            c.grid(row=row+1, column=0, sticky='nsew')
            c.grid_remove()
            row += 2
            
            label.bind('<Button-1>', lambda e,
                       c=c: self._click_handler(c))
            label.bind('<Enter>', lambda e,
                       label=label, i=i: label.configure(bg=self.style['highlight'],fg=self.style['highlight_fg']))
            label.bind('<Leave>', lambda e,
                       label=label, i=i: label.configure(bg=self.style['title_bg'],fg=self.style['title_fg']))
                       
    def _click_handler(self, chord):
        if len(chord.grid_info()) == 0:
            chord.grid()
        else:
            chord.grid_remove()
        
            