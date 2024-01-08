from PIL import ImageTk, Image

def read_img(patch, size):
    return ImageTk.PhotoImage(Image.open(patch).resize(size, Image.ANTIALIAS))

def screenCenter(window, width, height):
    screenW = window.winfo_screenwidth()
    screenH = window.winfo_screenheight()
    x = int((screenW/2) - (width/2))
    y = int((screenH/2) - (height/2))
    return window.geometry(f"{width}x{height}+{x}+{y}")

