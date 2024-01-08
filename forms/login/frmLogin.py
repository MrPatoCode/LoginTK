from forms.login.frmLoginDesign import LoginDesign
from forms.register.frmRegister import Register
from forms.master.frmMaster import MasterPanel
from db.operationsDb import OperationsDb
from db.connectionDb import Connect
from tkinter import messagebox

class Login(LoginDesign):
    MyConnect = Connect()
    Operations = OperationsDb()

    def check(self):
        user = str(self.user.get())
        passwd = str(self.password.get())
        data = self.Operations.selectUser(user, passwd)

        if(len(data)>0):
            if(len(user) > 3):
                if(user == data[0] and passwd == data[1]):
                    self.window.destroy()
                    MasterPanel()
                else:
                    messagebox.showerror(message= "Usuario o password incorrectos", title= "Error de inicio de sesión")
                    self.deleteEntry()
            else:
                    messagebox.showerror(message= "Usuario", title= "Error de inicio de sesión")
                    self.deleteEntry()
               
        else:
            messagebox.showerror(message= "Ingresa un nombre de usuario válido", title= "Error de inicio de sesión")
            self.deleteEntry()

    def register(self):
        Register()

    def verifyDb(self):
        if(True != self.MyConnect.verify()):
            messagebox.showerror(message="Base de datos no disponible",title="Error de conexión")

    def info(self):
        messagebox.showinfo(message="> Programador: Paulino M. \n> Imagenes: icon-icons.com", title= "Acerca de")
    
    def deleteEntry(self):
        self.user.delete(0, 'end')
        self.password.delete(0, 'end')
        self.user.focus()

    def __init__(self):
        self.verifyDb()
        super().__init__()




