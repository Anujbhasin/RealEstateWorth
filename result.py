from tkinter import *
from screen import *
from PIL import ImageTk,Image

root=Tk()

r=result()
def back():
    root.destroy()
   
root.state('zoomed')
root.resizable(width=False,height=False)
canvas=Canvas(root,width=1910,height=1070)
image=ImageTk.PhotoImage(Image.open(r'C:\Users\anujb\OneDrive\Desktop\Real Estate Worth Estimator\house\png-format-1571400415903444040gamerwallpapers295727741120.png'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

l=Label(root,text='RESULT',fg='red4',bg='orange',font=('',60,'bold'))
l.place(x=800,y=10)
l1=Label(root,text='Price of real estate',fg='red4',bg='orange',font=('',30))
l1.place(x=500,y=400)
l2=Label(root,text=r,fg='red4',bg='orange',font=('',30))
l2.place(x=1100,y=400)

b=Button(root,text='EXIT',command=back,justify='center',font=('',30,'bold'),bg='orange',fg='red4')
b.place(x=900,y=900)

root.mainloop()