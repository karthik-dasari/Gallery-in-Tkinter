from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Image Viewer")

myimg1=ImageTk.PhotoImage(Image.open("F:/Programming/Python/GUI/1.png"))
myimg2=ImageTk.PhotoImage(Image.open("F:/Programming/Python/GUI/2.png"))
myimg3=ImageTk.PhotoImage(Image.open("F:/Programming/Python/GUI/3.png"))
myimg4=ImageTk.PhotoImage(Image.open("F:/Programming/Python/GUI/4.png"))
myimg5=ImageTk.PhotoImage(Image.open("F:/Programming/Python/GUI/5.png"))

listofimages=[myimg1, myimg2, myimg3, myimg4, myimg5]

status=Label(root,text="Images 1 of "+str(len(listofimages)),bd=1,relief=SUNKEN,anchor=E).grid(row=3,column=0,columnspan=3,sticky=W+E)

label1=Label(image=myimg1)
label1.grid(row=0,column=0,columnspan=3)

def next(imgnumber):
    global label1
    global buttonback
    global buttonnext

    label1.grid_forget()

    label1=Label(image=listofimages[imgnumber-1])
    label1.grid(row=0,column=0,columnspan=3)
    buttonback=Button(root,text="<<",command=lambda : back(imgnumber-1)).grid(row=1,column=0)
    buttonnext=Button(root,text=">>",command=lambda : next(imgnumber+1)).grid(row=1,column=2)
    buttonexit=Button(root,text="EXIT",command=root.quit).grid(row=1,column=1)
    status=Label(root,text="Images "+str(imgnumber)+" of "+str(len(listofimages)),bd=1,relief=SUNKEN,anchor=E).grid(row=3,column=0,columnspan=3,sticky=W+E)

    
    if imgnumber==5:
        buttonnext=Button(root,text=">>",state=DISABLED).grid(row=1,column=2)

def back(imgnumber):
    global label1
    global buttonback
    global buttonnext

    label1.grid_forget()

    label1=Label(image=listofimages[imgnumber-1])
    label1.grid(row=0,column=0,columnspan=3)
    buttonback=Button(root,text="<<",command=lambda : back(imgnumber-1)).grid(row=1,column=0)
    buttonnext=Button(root,text=">>",command=lambda : next(imgnumber+1)).grid(row=1,column=2)
    buttonexit=Button(root,text="EXIT",command=root.quit).grid(row=1,column=1)
    status=Label(root,text="Images "+str(imgnumber)+" of "+str(len(listofimages)),bd=1,relief=SUNKEN,anchor=E).grid(row=3,column=0,columnspan=3,sticky=W+E)


    if imgnumber==1:
        buttonback=Button(root,text="<<",state=DISABLED).grid(row=1,column=0)

buttonexit=Button(root,text="EXIT",command=root.quit).grid(row=1,column=1)
buttonback=Button(root,text="<<",state=DISABLED).grid(row=1,column=0)
buttonnext=Button(root,text=">>",command=lambda :next(2)).grid(row=1,column=2)

root.mainloop()