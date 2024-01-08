import tkinter as tk
from tkinter.font import BOLD
import tools.generic as tool
from forms.master.frmMaster import MasterPanel

class LoginDesign:

    def check(self):
        pass

    def register(self):
        pass

    def info(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Iniciar sesión")
        self.window.geometry('800x500') 
        self.window.config(bg='#ffecd6' )
        self.window.resizable(width=0, height=0)
        tool.screenCenter(self.window, 800, 500)

        logo = tool.read_img("./images/logo.png", (200, 200))
        smll_icon = tool.read_img("./images/logo_32px.png", (16, 16))
        big_icon = tool.read_img("./images/logo_32px.png", (32, 32))
        icon_info = tool.read_img("./images/icon_info.png", (32, 32))

        self.window.iconphoto(False, smll_icon, big_icon)

        #Frame logo
        frame_logo = tk.Frame(self.window, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#ffecd6')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        label = tk.Label(frame_logo, image=logo, bg='#203c56')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #Frame login
        frame_login = tk.Frame(self.window,bd=0, relief=tk.SOLID, bg='#ffaa5e')
        frame_login.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Frame title top
        frame_title = tk.Frame(frame_login, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_title.pack(side="top", fill=tk.X)
        title = tk.Label(frame_title, text="Iniciar sesión", font=('Times', 30), fg='#0d2b45', bg='#ffecd6', pady= 40)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame fill bottom
        frame_fill = tk.Frame(frame_login, height=50, bd=0, relief=tk.SOLID, bg='#ffecd6')
        frame_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        user_label = tk.Label(frame_fill, text="Usuario", font=('Times', 20), fg='#0d2b45', bg='#ffecd6', anchor="w")
        user_label.pack(fill=tk.X, padx=20, pady=5)

        # User entry
        self.user = tk.Entry(frame_fill, textvariable="Usuario", font=('Times', 20))
        self.user.insert(0, "Admin")
        self.user.pack(fill=tk.X, padx=20, pady=5)


        user_psswrd = tk.Label(frame_fill, text="Password", font=('Times', 20), fg='#0d2b45', bg='#ffecd6', anchor="w")
        user_psswrd.pack(fill=tk.X, padx=20, pady=5)

        # Password entry
        self.password = tk.Entry(frame_fill, font=('Times', 20))
        self.password.pack(fill=tk.X, padx=20, pady=5)
        self.password.config(show="*")

        button = tk.Button(frame_fill, text= "Iniciar sesión", font=("Time", 18), fg='#0d2b45', activeforeground='#203c56', bg='#ffaa5e', activebackground='#d08159', command=self.check)
        button.pack(fill=tk.X, padx=20, pady=5)
        button.bind("<Return>", (lambda event: self.check()))

        button = tk.Button(frame_fill, text= "Registrar usuario", relief="flat", borderwidth=0, highlightthickness=0, font=("Time", 18), fg='#544e68', activeforeground='#d08159', bg='#ffecd6', activebackground='#ffecd6', command=self.register)
        button.pack(fill=tk.X, padx=20, pady=18)
        button.bind("<Return>", (lambda event: self.register()))

        button = tk.Button(frame_fill, image=icon_info, relief="flat", borderwidth=0, highlightthickness=0, fg='#544e68', activeforeground='#d08159', bg='#ffecd6', activebackground='#ffecd6', command=self.info)
        button.pack(fill=tk.X, padx=20, pady=5)
        button.bind("<Return>", (lambda event: self.info()))

        self.window.mainloop()