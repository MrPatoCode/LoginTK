from forms.register.frmRegisterDesign import RegisterDesign
from db.operationsDb import OperationsDb
from tkinter import messagebox

class Register(RegisterDesign):
    Operations = OperationsDb() 

    def newUser(self):
        user = str(self.newusr.get())
        passwd = str(self.password.get())
        confirmation = self.confirmation.get()
        data = self.Operations.selectUser(user, passwd)

        if(len(data) < 1):
            if((len(user) >= 3) and (len(passwd) >= 6)):
                if(passwd == confirmation):
                    self.Operations.insertRegister(user, passwd)
                    messagebox.showinfo(message="Registro de usuario exitoso", title="Registro de usuario", parent= self.window)
                    self.deleteEntry()
                    self.window.destroy()
                else:
                    messagebox.showerror(message="El password no coincide", title="Password incorrecto", parent= self.window)
                    self.deleteEntry(False)

            else:
                messagebox.showerror(message="-Ingresa un nombre de usuario válido \n-Ingresa una contraseña fuerte", title="Datos de usuarios no correctos", parent= self.window)
                self.deleteEntry()
        else:
            messagebox.showwarning(message="Nombre de usuario no disponible", title="Error de registro", parent= self.window)
            self.deleteEntry()

    def deleteEntry(self, usr = True):
        if(usr):
            self.newusr.delete(0, 'end')
            self.password.delete(0, 'end')
            self.confirmation.delete(0, 'end')
            self.newusr.focus()    
        else:
            self.password.delete(0, 'end')
            self.confirmation.delete(0, 'end')
            self.password.focus()

    def __init__(self):
        super().__init__()