import tkinter as tk
from tkinter.font import BOLD
import tools.generic as tool

class MasterPanel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Menú')
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w, h))
        self.window.config(bg='#ffecd6')
        self.window.resizable(width=0, height=0)  

        logo = tool.read_img("./images/logo.png", (200, 200))

        label = tk.Label(self.window, image=logo, bg='#ffecd6')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.window.mainloop()