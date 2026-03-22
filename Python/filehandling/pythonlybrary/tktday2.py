
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("image")
root.geometry("400x400")


upload = Image.open("img.jpeg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root,  text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)
root.mainloop()


from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text="Scan for Virus",
command=msg)
button.place(x=40, y=80)

root.mainloop()

#Function to open New (Top Level) Window
def topwin():

    top = Toplevel()
    top.geometry("180x180")
    top.title("toplevel")

    l2 = Label("top, text = This is toplevel window")
    l2.pack()
    top.mainloop()

l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

l.pack()
btn.pack()
