from tkinter import *
from PIL import ImageTk,Image

def login():
    root.destroy()
    import screen
root=Tk()

root.state('zoomed')
root.resizable(width=False,height=False)
canvas=Canvas(root,width=1910,height=1070)
image=ImageTk.PhotoImage(Image.open(r'C:\Users\anujb\OneDrive\Desktop\Real Estate Worth Estimator\house\png-format-1571400415903444040gamerwallpapers295727741120.png'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


l=Label(root,text='Real Estate Worth Estimator',fg='red4',bg='orange',font=('',60,'bold'))
l.place(x=450,y=10)

b=Button(root,command=login,text='Estimate',justify='center',font=('',30,'bold'),bg='orange',fg='red4')
b.place(x=850,y=400)

root.mainloop()