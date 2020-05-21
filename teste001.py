import pymysql.cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()

imagem = ImageTk.PhotoImage(file="transferir.gif")
w = Label(root, image=imagem)
w.grid()

root.mainloop()

