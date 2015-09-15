
__author__ = "Jose Diaz"
__copyright__ = "Copyright (C) 2015, Jose Diaz"
__license__ = "GPL v3.0"
__version__ = "1.0"
__revision__ = "18"
__date__ = "$02/04/2015 11:57:06 PM$"
__status__ = "Desarrollo"
__contact__ = "966403361"
__email__ = "jozz.18x@gmail.com"

import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser

from biblioteca.acordeon import *
from biblioteca.acerca_de import AcercaDe
from biblioteca.centerWindow import center_window
from biblioteca.widgetstyle import ButttonStyle, MenubuttonStyle, EntryStyle

from PIL import ImageTk, Image


class GUI(object):
    
    PROPERTIES_DESCRIPTION = {'router':'Controla el flujo de entrada y salida de datos.',
                              'switch':'Conecta varios computadores en una red.',
                              'server':'Controla el trafico de peticiones del usuario en tiempo de ejecucion.',
                              'wireless':'Senial analoga de conecciones por wifi',
                              'host':'Computadoras conectadas a una misma red.',
                              'computer':'Equipo del usuario.',
                              'laptop':'Equipo portatil del usuario.',
                              'firewall':'Controla la seguridad de un dispositivo.',
                              'internet':'Red amplia de conecciones globales.',
                              'satelite':'Equipo espacial.',
                              'wifi':'Coneccion wifi',
                              'hosting':'Servidor web que almacena data por medio de la nube.',
                              'printer':'Dispositivo periferico para impresion.',
                              'webcam':'Dispositivo periferico webcam',
                              'smartphone':'Dispositivo movil.',
                              'circuito':'Simula el circuito de un hardward.',
                              'battery':'Simula una bateria de carga.',
                              'line_left':'linea, conector o cable de interaccion con los dispositivos y objetos.',
                              'line_right':'linea, conector o cable de interaccion con los dispositivos y objetos.',
                              'line_center':'linea, conector o cable de interaccion con los dispositivos y objetos.',
                              'line_plane':'linea, conector o cable de interaccion con los dispositivos y objetos.',
                              'text':'Describe los objetos poniendoles nombres para una facil descripcion de los objetos en el lienzo.'
                             }
    
    BACKGROUND_DARK = '#121314'
    BACKGROUND_LIGHT = '#1a1e21'
    FOREGROUND_DARK = '#ADAFB2'
    FOREGROUND_LIGHT = '#DFE0E6'
    FONT_TITULO = ('Purisa', 24, 'bold')
    FONT_SMALL = ('Purisa', 9)
    FONT_MEDIUM = ('Purisa', 11)
    FONT_LARGE = ('Purisa', 12)
    HIGHLIGHT_BG = '#252a2d'
    HIGHLIGHT_FG = '#FFFFFF'
    HIGHLIGHT_FG_GREEN = '#21a341'
    
    BG_BUTTON = '#282d32'
    HIGHLIGHT_BUTTON = '#373d45'
    
    MENUBUTTONSTYLE = dict(font=FONT_SMALL, relief=FLAT, bd=0, width=12, 
                       bg=HIGHLIGHT_BG, fg=FOREGROUND_DARK, activebackground='#2a3136', 
                       activeforeground=HIGHLIGHT_FG, highlightbackground=BACKGROUND_DARK, highlightthickness=1)
    
    CHECKBUTTONSTYLE = dict(font=FONT_SMALL, bd=0,  width=12,
                       bg=HIGHLIGHT_BG, fg=FOREGROUND_DARK, 
                       activebackground=HIGHLIGHT_BG, activeforeground=HIGHLIGHT_FG,
                       highlightbackground=BACKGROUND_DARK, highlightthickness=1,
                       indicatoron=0, offrelief=FLAT, overrelief=FLAT, selectcolor=BACKGROUND_LIGHT, takefocus=0)
    
    BUTTONSTYLE = dict(font=FONT_MEDIUM, relief=FLAT, bd=0, width=10, bg=HIGHLIGHT_FG_GREEN, 
                             fg=HIGHLIGHT_FG, activebackground='#1c8a37', 
                             activeforeground=HIGHLIGHT_FG)
                    
    BUTTONCLOSE = dict(font=('Purisa', 10), relief=FLAT, bd=0, fg=FOREGROUND_DARK, 
                       activebackground=BG_BUTTON, activeforeground=HIGHLIGHT_FG)
                       
    MENUBUTTONSTYLE_MENU = dict(font=FONT_SMALL, relief=FLAT, bd=0, width=25, justify=LEFT, anchor=W,
                       bg=BACKGROUND_LIGHT, fg=FOREGROUND_DARK, activebackground=BG_BUTTON, 
                       activeforeground=FOREGROUND_LIGHT)
    
    def __init__(self, master):
        
        self.master = master
        
        self.frame = Frame(self.master, highlightbackground='black', highlightcolor='black', highlightthickness=1)
        self.frame.pack(fill=BOTH, expand=True)
        
        self.load_images()
        
        self.menu = self.create_menu(self.frame)
        self.master.config(menu=self.menu)
        
        self.menu_toolbar = self.create_menu_toolbar(self.frame)
        self.menu_toolbar.pack(side=TOP, fill=X)
        
        self.menu_toolbar.bind("<ButtonPress-1>", self.StartMove)
        self.menu_toolbar.bind("<ButtonRelease-1>", self.StopMove)
        self.menu_toolbar.bind("<B1-Motion>", self.OnMotion)
        
        self.taskbar = self.create_taskbar(self.frame)
        self.taskbar.pack(side=BOTTOM, fill=X)
        
        #self.toolbar = self.create_toolbar(self.master)
        #self.toolbar.pack(side=TOP, fill=X)
        
        self.panel = PanedWindow(self.frame, bg=self.BACKGROUND_DARK, orient=HORIZONTAL, bd=0, opaqueresize=True,
                                 sashwidth=5)
        
        self.space_simulation = self.create_space_simulation(self.panel)
        self.space_simulation.pack(fill=BOTH, expand=YES)
        
        self.toolbox = self.create_toolbox(self.panel)
        self.toolbox.pack(side=LEFT, fill=Y)
        
        self.properties = self.create_properties(self.panel)
        self.properties.pack(side=RIGHT, fill=Y, expand=NO)
        
        self.panel.add(self.toolbox)
        self.panel.add(self.space_simulation)
        self.panel.add(self.properties)
        
        self.panel.pack(fill=BOTH, expand=True, pady=1)
        
        self.example()
        self.create_toolbar_floting()
        
        #self.update_layout()
        self.master.update_idletasks()
                
        
    def create_menu_toolbar(self, master):
        """Menu Toolbar"""
        menu_toolbar = Frame(master, bg=self.BACKGROUND_LIGHT, cursor='fleur')
        
        title = Label(menu_toolbar, text='SimulatorSoft', font=self.FONT_TITULO, bg=menu_toolbar['bg'], fg=self.HIGHLIGHT_FG_GREEN)
        title.pack(side=LEFT, anchor=W, padx=10, pady=5)
        title.bind("<ButtonPress-1>", self.StartMove)
        title.bind("<ButtonRelease-1>", self.StopMove)
        title.bind("<B1-Motion>", self.OnMotion)
        
        menu_option = self.create_menu_options(menu_toolbar, bg=menu_toolbar['bg'], activebackground=menu_toolbar['bg'])
        menu_option.pack(side=RIGHT, anchor=E, padx=10, pady=5)
        
        return menu_toolbar
    
    def create_menu(self, master):
        ''' MENU '''
        menu = Menu(master, tearoff=0)
        
        self.menu_file = Menu(menu, tearoff=0)
        self.menu_file.add_command(label='New', accelerator='Ctrl+N', state=NORMAL)
        self.menu_file.add_command(label='Open', accelerator='Ctrl+A', state=NORMAL)
        self.menu_file.add_command(label='Save', accelerator='Ctrl+S', state=NORMAL)
        self.menu_file.add_command(label='Save as', accelerator='Ctrl+Mayus+S', state=NORMAL)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Close', accelerator='Ctrl+W', command=lambda: self.master.destroy(), state=NORMAL)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', command=self.exit, state=NORMAL)

        self.menu_edit = Menu(menu, tearoff=0)
        self.menu_edit.add_command(label='Undo', accelerator='Ctrl+Z', state=NORMAL)
        self.menu_edit.add_command(label='Redo', accelerator='Ctrl+Y', state=NORMAL)
        
        self.menu_view = Menu(menu, tearoff=0)
        self.var_sidebar_left = IntVar()
        self.var_sidebar_left.set(1)
        self.menu_view.add_checkbutton(label='Hide Side bar', variable=self.var_sidebar_left)
        self.var_sidebar_right = IntVar()
        self.var_sidebar_right.set(1)
        self.menu_view.add_checkbutton(label='Show info bar', variable=self.var_sidebar_right)
        self.menu_view.add_separator()
        self.var_full_screem = IntVar()
        self.var_full_screem.set(0)
        self.menu_view.add_checkbutton(label='Full Screem', command=self.full_screem, variable=self.var_full_screem)
        
        self.menu_tools = Menu(menu, tearoff=0)
        self.menu_tools.add_command(label='Command palette', state=NORMAL)
        self.menu_tools.add_separator()
        self.menu_tools.add_command(label='Build', state=NORMAL)
        self.menu_tools.add_command(label='Build System', state=NORMAL)
        self.menu_tools.add_separator()
        self.menu_tools.add_command(label='New Plugin', state=NORMAL)
        
        self.menu_help = Menu(menu, tearoff=0)
        self.menu_help.add_command(label='Documentation', state=NORMAL)
        self.menu_help.add_command(label='Help', command=self.help, state=NORMAL)
        self.menu_help.add_separator()
        self.menu_help.add_command(label='About Developer', command=self.about_developer, state=NORMAL)
        self.menu_help.add_separator()
        self.menu_help.add_command(label='About SimulationSoft', command=self.about_software, state=NORMAL)
        
        menu.add_cascade(label="File", menu=self.menu_file)
        menu.add_cascade(label="Edit", menu=self.menu_edit)
        menu.add_cascade(label="View", menu=self.menu_view)
        menu.add_cascade(label="Tools", menu=self.menu_tools)
        menu.add_cascade(label="Help", menu=self.menu_help)
        
        return menu
    
    def create_toolbox_titlebar(self, master):
        toolbox_titlebar = Frame(master, bg=master['bg'])
        Frame(toolbox_titlebar, bg=self.BACKGROUND_DARK).pack(side=BOTTOM, fill=X)
        btn_close = Menubutton(toolbox_titlebar, text='x', bg=toolbox_titlebar['bg'], **self.BUTTONCLOSE)
        btn_close.pack(side=RIGHT, anchor=E, padx=2, pady=2, ipadx=2, ipady=1)
        btn_close.bind("<Button-1>", lambda e: self.exit_toolbox())
        Label(toolbox_titlebar, text='Toolbox', font=self.FONT_MEDIUM, bg=toolbox_titlebar['bg'], fg=self.HIGHLIGHT_FG).pack(side=LEFT, anchor=W, padx=5, pady=2)
        grip = Label(toolbox_titlebar, bg=toolbox_titlebar['bg'], fg=self.FOREGROUND_DARK, bitmap="gray12", cursor='fleur')
        grip.pack(side=LEFT, fill=X, padx=10)
        
        return toolbox_titlebar
        
    def create_toolbox(self, master):
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
                
        self.btn_router = MenubuttonStyle(primer_chord, text="Router", **self.MENUBUTTONSTYLE)
        self.btn_router.grid(row=1, column=1, padx=2, pady=2)
        self.btn_router.bind('<Button>', lambda e: self.show_image(image=self.imageRouter, properties_name='Router', properties_description=self.PROPERTIES_DESCRIPTION['router']))
        
        self.btn_switch = MenubuttonStyle(primer_chord, text="Switch", **self.MENUBUTTONSTYLE)
        self.btn_switch.grid(row=1, column=2, padx=2, pady=2)
        self.btn_switch.bind('<Button>', lambda e: self.show_image(image=self.imageSwitch, properties_name='Switch', properties_description=self.PROPERTIES_DESCRIPTION['switch']))
        
        self.btn_server = MenubuttonStyle(primer_chord, text="Server",  **self.MENUBUTTONSTYLE)
        self.btn_server.grid(row=2, column=1, padx=2, pady=2)
        self.btn_server.bind('<Button>', lambda e: self.show_image(image=self.imageServer, properties_name='Server', properties_description=self.PROPERTIES_DESCRIPTION['server']))
        
        self.btn_wireless = MenubuttonStyle(primer_chord, text="Wireless", **self.MENUBUTTONSTYLE)
        self.btn_wireless.grid(row=2, column=2, padx=2, pady=2)
        self.btn_wireless.bind('<Button>', lambda e: self.show_image(image=self.imageWireless, properties_name='Wireless', properties_description=self.PROPERTIES_DESCRIPTION['wireless']))
        
        self.btn_host = MenubuttonStyle(primer_chord, text="Host", **self.MENUBUTTONSTYLE)
        self.btn_host.grid(row=3, column=1, padx=2, pady=2)
        self.btn_host.bind('<Button>', lambda e: self.show_image(image=self.imageHost, properties_name='Host', properties_description=self.PROPERTIES_DESCRIPTION['host']))

        self.btn_computer = MenubuttonStyle(primer_chord, text="Computer", **self.MENUBUTTONSTYLE)
        self.btn_computer.grid(row=3, column=2, padx=2, pady=2)
        self.btn_computer.bind('<Button>', lambda e: self.show_image(image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer']))
        
        self.btn_laptop = MenubuttonStyle(primer_chord, text="Laptop", **self.MENUBUTTONSTYLE)
        self.btn_laptop.grid(row=4, column=1, padx=2, pady=2)
        self.btn_laptop.bind('<Button>', lambda e: self.show_image(image=self.imageLaptop, properties_name='Laptop', properties_description=self.PROPERTIES_DESCRIPTION['laptop']))
        
        self.btn_firewall = MenubuttonStyle(primer_chord, text="Firewall", **self.MENUBUTTONSTYLE)
        self.btn_firewall.grid(row=4, column=2, padx=2, pady=2)
        self.btn_firewall.bind('<Button>', lambda e: self.show_image(image=self.imageFirewall, properties_name='Firewall', properties_description=self.PROPERTIES_DESCRIPTION['firewall']))
        
        self.btn_internet = MenubuttonStyle(primer_chord, text="Internet", **self.MENUBUTTONSTYLE)
        self.btn_internet.grid(row=5, column=1, padx=2, pady=2)
        self.btn_internet.bind('<Button>', lambda e: self.show_image(image=self.imageInternet, properties_name='Internet', properties_description=self.PROPERTIES_DESCRIPTION['internet']))
        
        self.btn_satelite = MenubuttonStyle(primer_chord, text = "Satelite", **self.MENUBUTTONSTYLE)
        self.btn_satelite.grid(row=5, column=2, padx=2, pady=2)
        self.btn_satelite.bind('<Button>', lambda e: self.show_image(image=self.imageSatelite, properties_name='Satelite', properties_description=self.PROPERTIES_DESCRIPTION['satelite']))
        
        self.btn_wifi = MenubuttonStyle(primer_chord, text = "Wifi", **self.MENUBUTTONSTYLE)
        self.btn_wifi.grid(row=6, column=1, padx=2, pady=2)
        self.btn_wifi.bind('<Button>', lambda e: self.show_image(image=self.imageWifi, properties_name='Wifi', properties_description=self.PROPERTIES_DESCRIPTION['wifi']))
        
        self.btn_hosting = MenubuttonStyle(primer_chord, text = "Hosting", **self.MENUBUTTONSTYLE)
        self.btn_hosting.grid(row=6, column=2, padx=2, pady=2)
        self.btn_hosting.bind('<Button>', lambda e: self.show_image(image=self.imageHosting, properties_name='Hosting', properties_description=self.PROPERTIES_DESCRIPTION['hosting']))
        
        segundo_chord = Chord(acordeon, title='  Perifericos', bg=self.HIGHLIGHT_BG)
        
        tercer_chord = Chord(acordeon, title='  Devices', bg=self.HIGHLIGHT_BG)
        
        self.btn_camputer = MenubuttonStyle(tercer_chord , text = "Computer", **self.MENUBUTTONSTYLE)
        self.btn_camputer.grid(row=1, column=1, padx=2, pady=2)
        self.btn_camputer.bind('<Button>', lambda e: self.show_image(image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer']))
        
        self.btn_laptop = MenubuttonStyle(tercer_chord , text = "Laptop", **self.MENUBUTTONSTYLE)
        self.btn_laptop.grid(row=1, column=2, padx=2, pady=2)
        self.btn_laptop.bind('<Button>', lambda e: self.show_image(image=self.imageLaptop, properties_name='Laptop', properties_description=self.PROPERTIES_DESCRIPTION['laptop']))
        
        self.btn_printer = MenubuttonStyle(tercer_chord , text = "Printer", **self.MENUBUTTONSTYLE)
        self.btn_printer.grid(row=2, column=1, padx=2, pady=2)
        self.btn_printer.bind('<Button>', lambda e: self.show_image(image=self.imagePrinter, properties_name='Printer', properties_description=self.PROPERTIES_DESCRIPTION['printer']))
        
        self.btn_webcam = MenubuttonStyle(tercer_chord, text = "Webcam", **self.MENUBUTTONSTYLE)
        self.btn_webcam.grid(row=2, column=2, padx=2, pady=2)
        self.btn_webcam.bind('<Button>', lambda e: self.show_image(image=self.imageWebCam, properties_name='Webcam', properties_description=self.PROPERTIES_DESCRIPTION['webcam']))
        
        self.btn_smartphone = MenubuttonStyle(tercer_chord, text = "Smartphone", **self.MENUBUTTONSTYLE)
        self.btn_smartphone.grid(row=3, column=1, padx=2, pady=2)
        self.btn_smartphone.bind('<Button>', lambda e: self.show_image(image=self.imageSmartphone, properties_name='Smartphone', properties_description=self.PROPERTIES_DESCRIPTION['smartphone']))
        
        
        cuarto_chord = Chord(acordeon, title='  Hardware', bg=self.HIGHLIGHT_BG)
        
        self.btn_circuito = MenubuttonStyle(cuarto_chord, text = "Circuito", **self.MENUBUTTONSTYLE)
        self.btn_circuito.grid(row=1, column=1, padx=2, pady=2)
        self.btn_circuito.bind('<Button>', lambda e: self.show_image(image=self.imageCircuito, properties_name='Circuito', properties_description=self.PROPERTIES_DESCRIPTION['circuito']))
        
        quinto_chord = Chord(acordeon, title='  Cables', bg=self.HIGHLIGHT_BG)
        
        self.btn_HDMI = MenubuttonStyle(quinto_chord, text='HDMI', **self.MENUBUTTONSTYLE)
        self.btn_HDMI.grid(row=1, column=1, padx=2, pady=2)
        
        sexto_chord = Chord(acordeon, title='  Connectors', bg=self.HIGHLIGHT_BG)
        
        self.btn_line_left = MenubuttonStyle(sexto_chord, text="Line left", **self.MENUBUTTONSTYLE)
        self.btn_line_left.grid(row=1, column=2, padx=2, pady=2)
        self.btn_line_left.bind('<Button>', lambda e: self.show_line(x0=80, y0=10, x1=10, y1=80, properties_name='Conector left', properties_description=self.PROPERTIES_DESCRIPTION['line_left']))

        self.btn_line_right = MenubuttonStyle(sexto_chord, text="Line right", **self.MENUBUTTONSTYLE)
        self.btn_line_right.grid(row=1, column=1, padx=2, pady=2)
        self.btn_line_right.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=80, y1=80, properties_name='Conector right', properties_description=self.PROPERTIES_DESCRIPTION['line_right']))
        
        self.btn_line_center = MenubuttonStyle(sexto_chord, text="Line center", **self.MENUBUTTONSTYLE)
        self.btn_line_center.grid(row=2, column=1, padx=2, pady=2)
        self.btn_line_center.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=10, y1=80, properties_name='Conector center', properties_description=self.PROPERTIES_DESCRIPTION['line_center']))
        
        self.btn_line_plane = MenubuttonStyle(sexto_chord, text="Line plane", **self.MENUBUTTONSTYLE)
        self.btn_line_plane.grid(row=2, column=2, padx=2, pady=2)
        self.btn_line_plane.bind('<Button>', lambda e: self.show_line(x0=10, y0=10, x1=80, y1=10, properties_name='Conector plane', properties_description=self.PROPERTIES_DESCRIPTION['line_plane']))
        
        self.var_dibujar_linea = IntVar()
        self.check_dibujar = Checkbutton(sexto_chord, text='Drawing', command=self.evento_checkbutton_dibujar, variable=self.var_dibujar_linea, **self.CHECKBUTTONSTYLE)
        self.check_dibujar.grid(row=3, column=1, padx=2, pady=2)
        
        septimo_chord = Chord(acordeon, title='  Text', bg=self.HIGHLIGHT_BG)
        self.var_add_text = StringVar()
        self.entry_text = EntryStyle(septimo_chord, font=self.FONT_SMALL, relief=FLAT, bd=0, 
                    bg=self.BACKGROUND_LIGHT, fg="white", justify=CENTER, textvariable=self.var_add_text,
                    insertbackground=self.FOREGROUND_LIGHT, insertwidth="1p", selectbackground="#2ebd59",
                    highlightcolor=self.BACKGROUND_DARK, highlightthickness=1)
        self.entry_text.pack(fill=X, padx=5, pady=5, ipady=3)
        self.entry_text.focus_set()
        self.entry_text.bind('<Return>', lambda e: self.show_text(self.entry_text.get(), properties_name='Text', properties_description=self.PROPERTIES_DESCRIPTION['text']))
        
        octavo_chord = Chord(acordeon, title='  Others', bg=self.HIGHLIGHT_BG)
        
        self.btn_batery = MenubuttonStyle(octavo_chord, text="Batery", **self.MENUBUTTONSTYLE)
        self.btn_batery.grid(row=1, column=1, padx=2, pady=2)
        self.btn_batery.bind('<Button>', lambda e: self.show_image(image=self.imageBattery, properties_name='Battery', properties_description=self.PROPERTIES_DESCRIPTION['battery']))
        
        acordeon.append_chords([primer_chord, segundo_chord, tercer_chord, cuarto_chord, quinto_chord, sexto_chord, septimo_chord, octavo_chord])
        acordeon.pack(fill=BOTH, expand=True)
        
        return toolbox
        
    def create_properties_titlebar(self, master):
        properties_titlebar = Frame(master, bg=master['bg'])
        Frame(properties_titlebar, bg=self.BACKGROUND_DARK).pack(side=BOTTOM, fill=X)
        btn_close = Menubutton(properties_titlebar, text='x', bg=properties_titlebar['bg'], **self.BUTTONCLOSE)
        btn_close.pack(side=RIGHT, anchor=E, padx=2, pady=2, ipadx=2, ipady=1)
        btn_close.bind("<Button-1>", lambda e: self.exit_properties())
        Label(properties_titlebar, text='Properties', font=self.FONT_MEDIUM, bg=properties_titlebar['bg'], fg=self.HIGHLIGHT_FG).pack(side=LEFT, anchor=W, padx=5, pady=2)
        grip = Label(properties_titlebar, bg=properties_titlebar['bg'], fg=self.FOREGROUND_DARK, bitmap="gray12", cursor='fleur')
        grip.pack(side=LEFT, fill=X, padx=10)
        
        return properties_titlebar
        
    def create_properties(self, master):
        """Create Properties."""
        properties = Frame(master, bg=self.BACKGROUND_LIGHT)
        
        titlebar = self.create_properties_titlebar(properties)
        titlebar.pack(side=TOP, fill=X)
        
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='default',
                        settings = {'TCombobox':
                                        {'configure':
                                            {'selectbackground': self.HIGHLIGHT_FG_GREEN,
                                             'selectforeground': self.FOREGROUND_LIGHT,
                                             'fieldbackground': self.BG_BUTTON,
                                             'background': self.BG_BUTTON,
                                             'foreground': self.FOREGROUND_LIGHT,
                                             'font': self.FONT_MEDIUM,
                                             'highlightbackground':'black',
                                             'highlightcolor':'black',
                                             'highlightthickness': 1,
                                             'relief': 'flat',
                                             'padding': 0,
                                             'borderwidth': 0
                                            },
                                            
                                        'map':
                                            {'highlightcolor':[('focus', self.HIGHLIGHT_FG_GREEN),('!focus', self.BACKGROUND_DARK)],
                                             'background': [('disabled', self.BACKGROUND_LIGHT), ('active', self.BACKGROUND_LIGHT),('pressed', '!focus', self.BACKGROUND_DARK)],
                                             'fieldbackground': [("disabled", self.BG_BUTTON), ('active', self.BACKGROUND_LIGHT),('pressed', '!focus', self.BACKGROUND_LIGHT)],
                                             'relief': [('selected', 'flat'),('pressed', 'flat'),('!pressed', 'flat')],
                                             'font': [('selected', ('Franklin Gothic Book', 12, 'bold'))]
                                            },
                                        }
                                    }
                         )
        combostyle.theme_use('combostyle')
                         
        self.var_properties_name = StringVar()
        self.combo_properties_name = ttk.Combobox(properties, textvariable=self.var_properties_name, state='readonly')
        self.combo_properties_name.pack(fill=BOTH, ipady=2)
    
        self.text_properties_description = Text(properties)
        self.text_properties_description.pack(pady=2)
        self.text_properties_description.config(font=self.FONT_SMALL, bg=self.BACKGROUND_LIGHT, fg=self.FOREGROUND_DARK,
                            autoseparators=5, wrap=WORD, undo=True, relief=FLAT, bd=0, state=DISABLED, cursor='arrow',
                            selectbackground=self.BACKGROUND_LIGHT, selectforeground=self.FOREGROUND_DARK)
        
        return properties
        
    def create_space_simulation(self, master):
        frame_simulation = Frame(master, bg=self.BACKGROUND_DARK, highlightbackground='BLACK', highlightthickness=0)
        
        self.width = 800; self.height = 600
        self.canvas = Canvas(frame_simulation, bg=self.BACKGROUND_DARK, cursor='tcross',
                             width=self.width, height=self.height, relief=FLAT, bd=0, highlightthickness=0)
        """
        sbar_vertical = ttk.Scrollbar(frame_simulation, command=self.canvas.yview, orient=VERTICAL)
        sbar_vertical.pack(side=RIGHT, fill=Y)

        sbar_horizontal = ttk.Scrollbar(frame_simulation, command=self.canvas.xview, orient=HORIZONTAL)
        sbar_horizontal.pack(side=BOTTOM, fill=X)                    
        
        self.canvas.config(yscrollcommand=sbar_vertical.set) 
        self.canvas.config(xscrollcommand=sbar_horizontal.set)
        """
        self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)
        
        # this data is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # add bindings for clicking, dragging and releasing over any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
        self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)
        
        # Add binding for Move to Scrollbar in Canvas
        self.canvas.bind("<Key-Prior>", self.page_up)
        self.canvas.bind("<Key-Next>", self.page_down)
        self.canvas.bind("<Key-Up>", self.unit_up)
        self.canvas.bind("<Key-Down>", self.unit_down)
        
        self.canvas.focus_set()
        
        return frame_simulation
    
    
    """Functions for events in Canvas Scrolled."""
    def page_up(self, event):
        self.canvas.yview_scroll(-1, "page")
        return "break"
    def page_down(self, event):
        self.canvas.yview_scroll(1, "page")
        return "break"
    def unit_up(self, event):
        self.canvas.yview_scroll(-1, "unit")
        return "break"
    def unit_down(self, event):
        self.canvas.yview_scroll(1, "unit")
        return "break"
    
        
    def create_toolbar(self, master):
        """Create Toolbar."""
        toolbar = Frame(master, bg=self.BACKGROUND_LIGHT)
        
        self.btn1 = ButttonStyle(toolbar, text=">>", ** self.BUTTONSTYLE)
        self.btn1.pack(side=RIGHT, padx=2, pady=5)
        
        self.btn2 = ButttonStyle(toolbar, text="IOI", ** self.BUTTONSTYLE)
        self.btn2.pack(side=RIGHT, padx=2, pady=5)
        
        self.btn3 = ButttonStyle(toolbar, text="<<", ** self.BUTTONSTYLE)
        self.btn3.pack(side=RIGHT, padx=2, pady=5)
        
        return toolbar
    
    def create_taskbar(self, master):
        """Create Taskbar."""
        taskbar = Frame(master, bg=self.BACKGROUND_LIGHT)
        
        self.btn0 = ButttonStyle(taskbar, text="Like", ** self.BUTTONSTYLE)
        self.btn0.pack(side=LEFT, fill=X, padx=10, pady=5)
        self.btn0.bind('<Button-1>', lambda e: self.open_facebook())
        
        self.btn1 = ButttonStyle(taskbar, text=">>", ** self.BUTTONSTYLE)
        self.btn1.pack(side=RIGHT, fill=X, padx=10, pady=5)
        
        self.btn2 = ButttonStyle(taskbar, text=">", ** self.BUTTONSTYLE)
        self.btn2.pack(side=RIGHT, fill=X, padx=0, pady=5)
        
        self.btn3 = ButttonStyle(taskbar, text="O", ** self.BUTTONSTYLE)
        self.btn3.pack(side=RIGHT, fill=X, padx=10, pady=5)
        
        self.btn4 = ButttonStyle(taskbar, text="<", ** self.BUTTONSTYLE)
        self.btn4.pack(side=RIGHT, fill=X, padx=0, pady=5)
        
        self.btn5 = ButttonStyle(taskbar, text="<<", ** self.BUTTONSTYLE)
        self.btn5.pack(side=RIGHT, fill=X, padx=10, pady=5)
        
        return taskbar
    
    def create_toolbar_floting(self):
        """Crea el boton flotante en la ventana principal"""
        frame = Frame(self.canvas, bg=self.BACKGROUND_LIGHT, highlightbackground='#0a0b0b', highlightcolor='green', highlightthickness=1)
        
        self.btn_flotante = Button(frame, text='New', image=self.iconOpen, compound=TOP, relief=FLAT, bd=0,
                                    bg=frame['bg'], fg=self.FOREGROUND_DARK, width=50, cursor='arrow',
                                    activebackground=self.BG_BUTTON, activeforeground=self.FOREGROUND_DARK)
        self.btn_flotante.pack(side=LEFT)
        
        self.btn_flotante = Button(frame, text='Commit', image=self.iconCommit, compound=TOP, relief=FLAT, bd=0,
                                    bg=frame['bg'], fg=self.FOREGROUND_DARK, width=50, cursor='arrow',
                                    activebackground=self.BG_BUTTON, activeforeground=self.FOREGROUND_DARK)
        self.btn_flotante.pack(side=LEFT)
        
        self.btn_flotante = Button(frame, text='Remove', image=self.iconRemove, compound=TOP, relief=FLAT, bd=0,
                                    bg=frame['bg'], fg=self.FOREGROUND_DARK, width=50, cursor='arrow', command=self.remove_item,
                                    activebackground=self.BG_BUTTON, activeforeground=self.FOREGROUND_DARK)
        self.btn_flotante.pack(side=LEFT)
        
        self.btn_flotante = Button(frame, text='Clear all', image=self.iconDelete, compound=TOP, relief=FLAT, bd=0,
                                    bg=frame['bg'], fg=self.FOREGROUND_DARK, width=50, cursor='arrow', command=self.remove_all,
                                    activebackground=self.BG_BUTTON, activeforeground=self.FOREGROUND_DARK)
        self.btn_flotante.pack(side=LEFT)
        
        #frame.place(in_=self.canvas, relx=0.0, rely=0, x=0, y=0, anchor=NW, bordermode="outside")
        frame.place(in_=self.canvas, relx=1.0, rely=0, x=0, y=0, anchor=NE, bordermode="inside")
        #frame.place(in_=self.canvas, relx=1.0, rely=1, x=0, y=0, anchor=SE, bordermode="outside")
        #frame.place(in_=self.canvas, relx=0.0, rely=1, x=0, y=0, anchor=SW, bordermode="outside")

    
    def create_menu_options(self, master, *args, **kw):
        """Crea el boton flotante en la ventana principal"""
        self.state_open_o_close = BooleanVar()
        self.state_open_o_close.set(False)
        btn_menu = Button(master, command=lambda: self.abrir_boton_flotante(btn_menu), 
                            image=self.iconOpen, relief=FLAT, bd=0, cursor="arrow", *args, **kw)
        return btn_menu
    
    def abrir_boton_flotante(self, btn_menu):
        """Abre los detalles cuando se presiona el boton flotante."""
        if not self.state_open_o_close.get():
            btn_menu.config(image=self.iconClose)
            self.crear_botones_flotante()
            self.state_open_o_close.set(True)
        else:
            btn_menu.config(image=self.iconOpen)
            self.frame_menu_option.destroy()
            self.state_open_o_close.set(False)
    
    def crear_botones_flotante(self):
        """Crea los widgets al presionar el boton flotante."""
        self.frame_menu_option = Frame(self.frame, bg=self.BACKGROUND_DARK, highlightbackground='black', highlightthickness=1)
        
        self.btn_menu_options = Menubutton(self.frame_menu_option, text='  Options', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_options.pack(side=TOP, fill=X, padx=0, pady=0, ipady=3)
        self.btn_menu_toolbox = Menubutton(self.frame_menu_option, text='  View Toolbox', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_toolbox.pack(side=TOP, fill=X, padx=0, pady=1, ipady=3)
        self.btn_menu_properties = Menubutton(self.frame_menu_option, text='  View Properties', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_properties.pack(side=TOP, fill=X, padx=0, pady=0, ipady=3)
        self.btn_menu_fullScreem = Menubutton(self.frame_menu_option, text='  Full Screem', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_fullScreem.pack(side=TOP, fill=X, padx=0, pady=1, ipady=3)
        self.btn_menu_fullScreem.bind('<Button-1>', lambda e: self.full_screem())
        self.btn_menu_news = Menubutton(self.frame_menu_option, text='  What is new', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_news.pack(side=TOP, fill=X, padx=0, pady=0, ipady=3)
        self.btn_menu_about_developer = Menubutton(self.frame_menu_option, text='  About Developer', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_about_developer.pack(side=TOP, fill=X, padx=0, pady=1, ipady=3)
        self.btn_menu_about_developer.bind('<Button-1>', lambda e: self.about_developer())
        self.btn_menu_about = Menubutton(self.frame_menu_option, text='  About', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_about.pack(side=TOP, fill=X, padx=0, pady=0, ipady=3)
        self.btn_menu_about.bind('<Button-1>', lambda e: self.about_software())
        self.btn_menu_exit = Menubutton(self.frame_menu_option, text='  Exit', **self.MENUBUTTONSTYLE_MENU)
        self.btn_menu_exit.pack(side=TOP, fill=X, padx=0, pady=1, ipady=3)
        self.btn_menu_exit.bind('<Button-1>', lambda e: self.exit())
        
        self.frame_menu_option.place(in_=self.frame, relx=1.0, rely=0.4, x=0, y=20, anchor=SE, bordermode="inside")
        
    
    
    def load_images(self):
        # Create the image objects for the hardware Images
        # ----------------------------------------------------------------------
        self.iconOpen = ImageTk.PhotoImage(Image.open(r"simuladores\icon_basic\icon_open.png"))
        self.iconClose = ImageTk.PhotoImage(Image.open(r"simuladores\icon_basic\icon_close.png"))
        self.iconCommit = ImageTk.PhotoImage(Image.open(r"simuladores\icon_basic\icon_commit.png"))
        self.iconRemove = ImageTk.PhotoImage(Image.open(r"simuladores\icon_basic\icon_remove.png"))
        self.iconDelete = ImageTk.PhotoImage(Image.open(r"simuladores\icon_basic\icon_delete.png"))
        
        self.imageRouter = ImageTk.PhotoImage(Image.open(r"simuladores\router.png"))
        self.imageSwitch = ImageTk.PhotoImage(Image.open(r"simuladores\switch.png"))
        self.imageServer = ImageTk.PhotoImage(Image.open(r"simuladores\server.png"))
        self.imageSmartphone = ImageTk.PhotoImage(Image.open(r"simuladores\smartphone.png"))
        self.imageWireless = ImageTk.PhotoImage(Image.open(r"simuladores\wireless.png"))
        self.imageHost = ImageTk.PhotoImage(Image.open(r"simuladores\host.png"))
        self.imageComputer = ImageTk.PhotoImage(Image.open(r"simuladores\computer.png"))
        self.imageLaptop = ImageTk.PhotoImage(Image.open(r"simuladores\laptop.png"))
        self.imagePrinter = ImageTk.PhotoImage(Image.open(r"simuladores\device.png"))
        self.imageWebCam = ImageTk.PhotoImage(Image.open(r"simuladores\webcam.png"))
        self.imageInternet = ImageTk.PhotoImage(Image.open(r"simuladores\internet.png"))
        self.imageFirewall = ImageTk.PhotoImage(Image.open(r"simuladores\firewall.png"))
        self.imageSatelite = ImageTk.PhotoImage(Image.open(r"simuladores\satelite.png"))
        self.imageHosting = ImageTk.PhotoImage(Image.open(r"simuladores\hosting.png"))
        self.imageWifi = ImageTk.PhotoImage(Image.open(r"simuladores\wifi.png"))
        self.imageBattery = ImageTk.PhotoImage(Image.open(r"simuladores\battery.png"))
        self.imageCircuito = ImageTk.PhotoImage(Image.open(r"simuladores\circuito.png"))
    
    def example(self):
        """Example simulation."""
        self.show_image(x=100, y=80, image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer'])
        self.show_image(x=300, y=80, image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer'])
        self.show_image(x=500, y=80, image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer'])
        self.show_image(x=700, y=80, image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer'])
        self.show_image(x=900, y=80, image=self.imageComputer, properties_name='Computer', properties_description=self.PROPERTIES_DESCRIPTION['computer'])
        
    def open_facebook(self):
        """Open facebook."""
        webbrowser.open('https://www.facebook.com/jozz.diaz.m')
    
    def show_properties(self, properties_name='', properties_description=''):
        self.var_properties_name.set(properties_name)
        self.combo_properties_name['values'] = properties_name
        self.text_properties_description.configure(state=NORMAL)
        self.text_properties_description.delete(0.0, END)
        self.text_properties_description.insert(END, properties_description)
        self.text_properties_description.configure(state=DISABLED)
    
    def show_image(self, x=80, y=80, image=None, properties_name='', properties_description=''):
        self.add_image(x, y, image)
        self.show_properties(properties_name, properties_description)
        
    def show_line(self, x0=80, y0=10, x1=10, y1=80, properties_name='', properties_description=''):
        self.add_line(x0, y0, x1, y1)
        self.show_properties(properties_name, properties_description)
    
    def show_text(self, text, x=80, y=30, properties_name='', properties_description=''):
        self.add_text(x, y, text)
        self.show_properties(properties_name, properties_description)
        self.var_add_text.set('') #Limpia el entry al insertar un texto
    
    def show_widget(self, x=50, y=500, widget=None, properties_name='', properties_description=''):
        self.add_window(x, y, window=widget, tags="token")
        self.show_properties(properties_name, properties_description)
        
    
    # Unserta en el canvas objectos. 
    #------------------------------------------------------------------
    def add_image(self, x, y, image):
        self.img = self.canvas.create_image(x, y, image=image, tags="token")
    
    def add_line(self, x0, y0, x1, y1):
        self.line = self.canvas.create_line(x0, y0, x1, y1, width=3, fill='#0f9d32', tags="token", capstyle='round', joinstyle='miter')
    
    def add_text(self, x, y, text):
        self.text = self.canvas.create_text(x, y, text=text, font=self.FONT_MEDIUM, fill='#207bab', tags="token")
    
    def add_widget(self, x, y, widget):
        self.widget = self.canvas.create_window(x, y, window=widget, tags="token")
        
    
    def dibujar_linea(self, event):
        """Dibuja una linea pulsando el canvas en un punto."""
        x_origem = self.canvas.winfo_rootx()
        y_origem = self.canvas.winfo_rooty()
        x_abs = self.canvas.winfo_pointerx()
        y_abs = self.canvas.winfo_pointery()
        try:
            P = (x_abs - x_origem, y_abs - y_origem)
            self.canvas.create_line(self.ultimo_P, P, width=3, fill='#0f9d32', capstyle='round', joinstyle='miter', tags="token")
            self.ultimo_P = P
        except:
            self.ultimo_P=(x_abs - x_origem, y_abs - y_origem)
    
    def evento_checkbutton_dibujar(self):
        """Evento para el Checkbutton dibujar."""
        if self.var_dibujar_linea.get() == 1:
            self.canvas.bind('<1>',self.dibujar_linea)
        else:
            self.ultimo_P = None #Coloca el el punto anterior a None para iniciar una nueva linea de un nuevo punto.
            self.canvas.unbind('<1>')
            
        
        
    def remove_item(self):
        """Remove only the last object in the canvas"""
        if self.img:
            self.canvas.delete(self.img) # remove
        elif self.line:
            self.canvas.delete(self.line) # remove
        elif self.text:
            self.canvas.delete(self.text) # remove
        elif self.widget: 
            self.canvas.delete(self.widget) # remove
        else:
            pass

    def remove_all(self):
        """Remove all object in the canvas."""
        self.canvas.delete(ALL) # remove all items
        self.show_properties(properties_name='', properties_description='') #Clean the properties values
    
    
    def full_screem(self, event=None):
        """Window in full screem."""
        val = self.var_full_screem.get()
        if val:
            self.master.withdraw() #Oculta la ventana
            self.master.overrideredirect(False) #Pone en estado con borde la ventana
            self.master.wm_attributes("-fullscreen", True) #Estado fullScreem
            self.master.update_idletasks() #Actualiza la ventana
            self.master.deiconify() #Aparece la ventana
        elif not val:
            self.master.withdraw() #Oculta la ventana
            self.master.wm_attributes("-fullscreen", False) #Estado fullScreem
            self.master.overrideredirect(True) #Pone en estado sin borde la ventana
            self.master.update_idletasks() #Actualiza la ventana
            self.master.deiconify() #Aparece la ventana
        else:
            print('nada')
        
        
        
    """Move to windows."""
    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry("+%s+%s" % (x, y))
        
        
    """Move to objects in canvas."""
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
        
            
    def about_developer(self):
        """About Developer"""
        text1 = "\nJose Diaz Mayta"
        text2 = "\n\nFundador, SEO Coorporativo y developer en \nDiazCompany Inc.\n\nDeveloper in Python Proggraming\n\n\n\n\nE-mail: jozz.18x@gmail.com    cell: 966403361"
        AcercaDe(self.master, title="About Developer", bg=self.BACKGROUND_LIGHT, fg=self.FOREGROUND_LIGHT, 
                 text1=text1, text2=text2, button=True, width=360, height=350, overrideredirect=True)
    
    def about_software(self):
        """About Software"""
        titulo = "\n\nSimulationSoft"
        text = "\nversion 1.0\n\n\n\n\nCopyright (C) 2015 Jose Diaz"
        AcercaDe(self.master, title=titulo, bg=self.BACKGROUND_LIGHT, fg=self.FOREGROUND_LIGHT,
                 text1=titulo, text2=text, button=True, width=550, height=320, overrideredirect=True)
                    
    def help(self, event=None):
        messagebox.showinfo("Ayuda", "Para cualquier ayuda escribir a: jozz.18x@gmail.com ", icon='question')
        
    
        

    def exit_toolbox(self, event=None):
        self.toolbox.destroy()
        
    def exit_properties(self):
        self.properties.destroy()
        
    def exit(self):
        sys.exit()
    
if __name__ == "__main__":
    root = Tk()
    root.wm_iconbitmap(r"images\Icon.ico")
    root.title("Simulador de redes")
    #root.overrideredirect(True)
    center_window(root, width=1200, height=660, windowsbar=True)
    app = GUI(root)
    bg = app.frame.config(bg=app.BACKGROUND_DARK)
    root['bg'] = bg
    root.mainloop()
    

