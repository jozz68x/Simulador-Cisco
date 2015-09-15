# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Jose Diaz"
__date__ = "$03/04/2015 09:43:29 PM$"

from tkinter import *
from acordeon import *
from widgetstyle import *
from PIL import ImageTk, Image


class Toolbox(object):
    
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
            
    def __init__(self, master, canvas=None):
        self.master = master
        
        self.load_images()
        self.toolbox = self.create_toolbox_body(self.master)
        self.toolbox.pack(side=LEFT, fill=Y)
        
        if canvas:
            print("Asignacion del canvas y configurando")
            self.canvas = canvas
            # this data is used to keep track of an item being dragged
            self._drag_data = {"x": 0, "y": 0, "item": None}

            # add bindings for clicking, dragging and releasing over any object with the "token" tag
            self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
            self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
            self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)
        else:
            print("Canvas creado.")
            self.canvas = Canvas(self.master, bg=self.BACKGROUND_DARK, cursor='fleur',
                             width=750, height=600, relief=FLAT, bd=0, highlightthickness=0)

            self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)
            
            # this data is used to keep track of an item being dragged
            self._drag_data = {"x": 0, "y": 0, "item": None}

            # add bindings for clicking, dragging and releasing over any object with the "token" tag
            self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
            self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
            self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)
        
    
    def create_toolbox_titlebar(self, master):
        toolbox_titlebar = Frame(master, bg=master['bg'])
        Frame(toolbox_titlebar, bg=self.BACKGROUND_DARK).pack(side=BOTTOM, fill=X)
        Label(toolbox_titlebar, text='Toolbox', font=self.FONT_MEDIUM, bg=toolbox_titlebar['bg'], fg=self.HIGHLIGHT_FG).pack(side=LEFT, anchor=W, padx=5, pady=2)
        btn_close = Menubutton(toolbox_titlebar, text='x', bg=toolbox_titlebar['bg'], **self.BUTTONCLOSE)
        btn_close.pack(side=RIGHT, anchor=E, padx=2, pady=2)
        btn_close.bind("<Button-1>", lambda e: self.exit_toolbox())
        return toolbox_titlebar
        
    def create_toolbox_body(self, master):
        """Documentation"""
        toolbox = Frame(master, relief=FLAT, bg=self.BACKGROUND_LIGHT)
        
        titlebar = self.create_toolbox_titlebar(toolbox)
        titlebar.pack(side=TOP, fill=X)
                
        accordion_style = {
                'title_bg': self.BACKGROUND_LIGHT,
                'title_fg': self.FOREGROUND_DARK,
                'highlight': self.HIGHLIGHT_FG_GREEN,
                'highlight_fg': self.HIGHLIGHT_FG,
                'cursor': 'hand2'
                }
        
        acordeon = Accordion(toolbox, bg=self.BACKGROUND_LIGHT, accordion_style=accordion_style)
        
        primer_chord = Chord(acordeon, title='  Network', bg=self.HIGHLIGHT_BG)
                
        self.btn_router = ButttonStyle(primer_chord, text="Router", **self.BUTTONSTYLE)
        self.btn_router.grid(row=1, column=1, padx=2, pady=2)
        self.btn_router.bind('<Button>', lambda e: self.show_image(image=self.imageRouter))
        
        self.btn_switch = ButttonStyle(primer_chord, text="Switch", **self.BUTTONSTYLE)
        self.btn_switch.grid(row=1, column=2, padx=2, pady=2)
        self.btn_switch.bind('<Button>', lambda e: self.show_image(image=self.imageSwitch))
        
        self.btn_server = ButttonStyle(primer_chord, text="Server",  **self.BUTTONSTYLE)
        self.btn_server.grid(row=2, column=1, padx=2, pady=2)
        self.btn_server.bind('<Button>', lambda e: self.show_image(image=self.imageServer))
        
        self.btn_wireless = ButttonStyle(primer_chord, text="Wireless", **self.BUTTONSTYLE)
        self.btn_wireless.grid(row=2, column=2, padx=2, pady=2)
        self.btn_wireless.bind('<Button>', lambda e: self.show_image(image=self.imageWireless))
        
        self.btn_host = ButttonStyle(primer_chord, text="Host", **self.BUTTONSTYLE)
        self.btn_host.grid(row=3, column=1, padx=2, pady=2)
        self.btn_host.bind('<Button>', lambda e: self.show_image(image=self.imageHost))

        self.btn_computer = ButttonStyle(primer_chord, text="Computer", **self.BUTTONSTYLE)
        self.btn_computer.grid(row=3, column=2, padx=2, pady=2)
        self.btn_computer.bind('<Button>', lambda e: self.show_image(image=self.imageComputer))
        
        self.btn_laptop = ButttonStyle(primer_chord, text="Laptop", **self.BUTTONSTYLE)
        self.btn_laptop.grid(row=4, column=1, padx=2, pady=2)
        self.btn_laptop.bind('<Button>', lambda e: self.show_image(image=self.imageLaptop))
        
        self.btn_firewall = ButttonStyle(primer_chord, text="Firewall", **self.BUTTONSTYLE)
        self.btn_firewall.grid(row=4, column=2, padx=2, pady=2)
        self.btn_firewall.bind('<Button>', lambda e: self.show_image(image=self.imageFirewall))
        
        self.btn_internet = ButttonStyle(primer_chord, text="Internet", **self.BUTTONSTYLE)
        self.btn_internet.grid(row=5, column=1, padx=2, pady=2)
        self.btn_internet.bind('<Button>', lambda e: self.show_image(image=self.imageInternet))
        
        self.btn_satelite = ButttonStyle(primer_chord, text = "Satelite", **self.BUTTONSTYLE)
        self.btn_satelite.grid(row=5, column=2, padx=2, pady=2)
        self.btn_satelite.bind('<Button>', lambda e: self.show_image(image=self.imageSatelite))
        
        self.btn_wifi = ButttonStyle(primer_chord, text = "Wifi", **self.BUTTONSTYLE)
        self.btn_wifi.grid(row=6, column=1, padx=2, pady=2)
        self.btn_wifi.bind('<Button>', lambda e: self.show_image(image=self.imageWifi))
        
        self.btn_hosting = ButttonStyle(primer_chord, text = "Hosting", **self.BUTTONSTYLE)
        self.btn_hosting.grid(row=6, column=2, padx=2, pady=2)
        self.btn_hosting.bind('<Button>', lambda e: self.show_image(image=self.imageHosting))
        
        segundo_chord = Chord(acordeon, title='  Perifericos', bg=self.HIGHLIGHT_BG)
        
        tercer_chord = Chord(acordeon, title='  Devices', bg=self.HIGHLIGHT_BG)
        
        self.btn_camputer = ButttonStyle(tercer_chord , text = "Computer", **self.BUTTONSTYLE)
        self.btn_camputer.grid(row=1, column=1, padx=2, pady=2)
        self.btn_camputer.bind('<Button>', lambda e: self.show_image(image=self.imageComputer))
        
        self.btn_laptop = ButttonStyle(tercer_chord , text = "Laptop", **self.BUTTONSTYLE)
        self.btn_laptop.grid(row=1, column=2, padx=2, pady=2)
        self.btn_laptop.bind('<Button>', lambda e: self.show_image(image=self.imageLaptop))
        
        self.btn_printer = ButttonStyle(tercer_chord , text = "Printer", **self.BUTTONSTYLE)
        self.btn_printer.grid(row=2, column=1, padx=2, pady=2)
        self.btn_printer.bind('<Button>', lambda e: self.show_image(image=self.imagePrinter))
        
        self.btn_webcam = ButttonStyle(tercer_chord, text = "Webcam", **self.BUTTONSTYLE)
        self.btn_webcam.grid(row=2, column=2, padx=2, pady=2)
        self.btn_webcam.bind('<Button>', lambda e: self.show_image(image=self.imageWebCam))
        
        self.btn_smartphone = ButttonStyle(tercer_chord, text = "Smartphone", **self.BUTTONSTYLE)
        self.btn_smartphone.grid(row=3, column=1, padx=2, pady=2)
        self.btn_smartphone.bind('<Button>', lambda e: self.show_image(image=self.imageSmartphone))
        
        
        cuarto_chord = Chord(acordeon, title='  Hardware', bg=self.HIGHLIGHT_BG)
        
        self.btn_circuito = ButttonStyle(cuarto_chord, text = "Circuito", **self.BUTTONSTYLE)
        self.btn_circuito.grid(row=1, column=1, padx=2, pady=2)
        self.btn_circuito.bind('<Button>', lambda e: self.show_image(image=self.imageCircuito))
        
        quinto_chord = Chord(acordeon, title='  Cables', bg=self.HIGHLIGHT_BG)
        
        self.btn_HDMI = ButttonStyle(quinto_chord, text='HDMI', **self.BUTTONSTYLE)
        self.btn_HDMI.grid(row=1, column=1, padx=2, pady=2)
        
        sexto_chord = Chord(acordeon, title='  Connectors', bg=self.HIGHLIGHT_BG)
        
        self.btn_line_left = ButttonStyle(sexto_chord, text="Line left", **self.BUTTONSTYLE)
        self.btn_line_left.grid(row=1, column=2, padx=2, pady=2)
        self.btn_line_left.bind('<Button>', lambda e: self.show_line(x0=80, y0=10, x1=10, y1=80))
        
        self.btn_line_right = ButttonStyle(sexto_chord, text="Line right", **self.BUTTONSTYLE)
        self.btn_line_right.grid(row=1, column=1, padx=2, pady=2)
        self.btn_line_right.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=80, y1=80))
        
        self.btn_line_center = ButttonStyle(sexto_chord, text="Line center", **self.BUTTONSTYLE)
        self.btn_line_center.grid(row=2, column=1, padx=2, pady=2)
        self.btn_line_center.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=10, y1=80))
        
        self.btn_line_plane = ButttonStyle(sexto_chord, text="Line plane", **self.BUTTONSTYLE)
        self.btn_line_plane.grid(row=2, column=2, padx=2, pady=2)
        self.btn_line_plane.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=80, y1=10))
        
        septimo_chord = Chord(acordeon, title='  Text', bg=self.HIGHLIGHT_BG)
        #self.btn_text = ButttonStyle(septimo_chord, text="Text", **self.BUTTONSTYLE)
        #self.btn_text.grid(row=1, column=1, padx=2, pady=2)
        #self.btn_text.bind('<Button>', lambda e: self.show_text())
        
        self.entry_text = EntryStyle(septimo_chord, font=self.FONT_SMALL, relief=FLAT, bd=0, 
                    bg=self.BACKGROUND_LIGHT, fg="white", justify=CENTER,
                    insertbackground="white", selectbackground="#2ebd59")
        self.entry_text.pack(fill=X, padx=5, pady=10, ipady=3)
        self.entry_text.focus_set()
        self.entry_text.bind('<Return>', lambda e: self.show_text(self.entry_text.get()))
        
        octavo_chord = Chord(acordeon, title='  Others', bg=self.HIGHLIGHT_BG)
        
        self.btn_batery = ButttonStyle(octavo_chord, text="Batery", **self.BUTTONSTYLE)
        self.btn_batery.grid(row=1, column=1, padx=2, pady=2)
        self.btn_batery.bind('<Button>', lambda e: self.show_image(image=self.imageBattery))
        
        acordeon.append_chords([primer_chord, segundo_chord, tercer_chord, cuarto_chord, quinto_chord, sexto_chord, septimo_chord, octavo_chord])
        acordeon.pack(fill=BOTH, expand=True)
        
        return toolbox
    
    def load_images(self):
        # Create the image objects for the hardware Images
        # ----------------------------------------------------------------------
        self.imageRouter = ImageTk.PhotoImage(Image.open(r"images\router.png"))
        self.imageSwitch = ImageTk.PhotoImage(Image.open(r"images\switch.png"))
        self.imageServer = ImageTk.PhotoImage(Image.open(r"images\server.png"))
        self.imageSmartphone = ImageTk.PhotoImage(Image.open(r"images\smartphone.png"))
        self.imageWireless = ImageTk.PhotoImage(Image.open(r"images\wireless.png"))
        self.imageHost = ImageTk.PhotoImage(Image.open(r"images\host.png"))
        self.imageComputer = ImageTk.PhotoImage(Image.open(r"images\computer.png"))
        self.imageLaptop = ImageTk.PhotoImage(Image.open(r"images\laptop.png"))
        self.imagePrinter = ImageTk.PhotoImage(Image.open(r"images\device.png"))
        self.imageWebCam = ImageTk.PhotoImage(Image.open(r"images\webcam.png"))
        self.imageInternet = ImageTk.PhotoImage(Image.open(r"images\internet.png"))
        self.imageFirewall = ImageTk.PhotoImage(Image.open(r"images\firewall.png"))
        self.imageSatelite = ImageTk.PhotoImage(Image.open(r"images\satelite.png"))
        self.imageHosting = ImageTk.PhotoImage(Image.open(r"images\hosting.png"))
        self.imageWifi = ImageTk.PhotoImage(Image.open(r"images\wifi.png"))
        self.imageBattery = ImageTk.PhotoImage(Image.open(r"images\battery.png"))
        self.imageCircuito = ImageTk.PhotoImage(Image.open(r"images\circuito.png"))
        
        
    def show_image(self, x=80, y=80, image=None):
        self.canvas.create_image(x, y, image=image, tags="token")
    
    def show_line(self, x0=80, y0=10, x1=10, y1=80):
        self.canvas.create_line(x0, y0, x1, y1, width=5, fill='#0f9d32', tags="token", capstyle='round', joinstyle='miter')
    
    def show_text(self, text, x=80, y=30):
        self.canvas.create_text(x, y, font="Purisa", fill='#207bab', text=text, tags="token")
    
    def show_widget(self, x=50, y=500, widget=None):
        self.canvas.create_window(x, y, window=widget, tags="token")
    
    def OnTokenButtonPress(self, event):
        '''Being drag of an object'''
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def OnTokenButtonRelease(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def OnTokenMotion(self, event):
        '''Handle dragging of an object'''
        # compute how much this object has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        
        self.update_layout()
        
        
    def update_layout(self):
        #self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.config(scrollregion=(0, 0, self.canvas['width'],self.canvas['height']))
        self.canvas.update_idletasks() 
        
    def exit_toolbox(self, event=None):
        self.master.destroy()
        
    
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.toolbox = Toolbox(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
