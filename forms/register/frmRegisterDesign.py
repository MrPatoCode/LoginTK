import tkinter as tk
from tkinter.font import BOLD
import tools.generic as tool

class RegisterDesign:

    def newUser(self):
        pass

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title('Registrar usuario')
        self.window.config(bg='#ffecd6')
        self.window.resizable(width=0, height=0)
        tool.screenCenter(self.window, 600, 450)

        logo = tool.read_img("./images/logo.png", (150, 150))

        #Frame logo
        frame_logo = tk.Frame(self.window, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg='#ffecd6')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        
        label = tk.Label(frame_logo, image=logo, bg='#d08159')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #Frame form
        frame_form = tk.Frame(self.window,bd=0, relief=tk.SOLID, bg='#ffaa5e')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
                
        #Frame title top
        frame_title = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_title.pack(side="top", fill=tk.X)
        title = tk.Label(frame_title, text="Registro de nuevo usuario", font=('Times', 24), fg='#0d2b45', bg='#ffecd6', pady= 20)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame fill bottom
        frame_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#ffecd6')
        frame_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        user_label = tk.Label(frame_fill, text="Usuario", font=('Times', 20), fg='#0d2b45', bg='#ffecd6', anchor="w")
        user_label.pack(fill=tk.X, padx=20, pady=5)

        # New User entry
        self.newusr = tk.Entry(frame_fill, textvariable="NewUsuario", font=('Times', 20))
        self.newusr.pack(fill=tk.X, padx=20, pady=5)
        self.newusr.insert(0, "")


        new_psswrd = tk.Label(frame_fill, text="Password", font=('Times', 20), fg='#0d2b45', bg='#ffecd6', anchor="w")
        new_psswrd.pack(fill=tk.X, padx=20, pady=5)  

        #New Password Entry
        self.password = tk.Entry(frame_fill, font=('Times', 20))
        self.password.pack(fill=tk.X, padx=20, pady=5)
        self.password.insert(0, "")
        self.password.config(show="*")      

        confirmation_label = tk.Label(frame_fill, text="Confirmar", font=('Times', 20), fg='#0d2b45', bg='#ffecd6', anchor="w")
        confirmation_label.pack(fill=tk.X, padx=20, pady=5)  

        #Confirmation Entry
        self.confirmation = tk.Entry(frame_fill, font=('Times', 20))
        self.confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation.insert(0, "")
        self.confirmation.config(show="*")      

        button = tk.Button(frame_fill, text= "Registrar usuario", font=("Time", 18), fg='#0d2b45', activeforeground='#203c56', bg='#ffaa5e', activebackground='#d08159', command=self.newUser)
        button.pack(fill=tk.X, padx=20, pady=5)
        button.bind("<Return>", (lambda event: self.newUser()))

        self.window.mainloop()
