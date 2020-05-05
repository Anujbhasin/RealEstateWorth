from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from PIL import ImageTk,Image

root=Tk()

def ML(a,b,c,d,e):
    df = pd.read_csv(r'C:\Users\anujb\OneDrive\Desktop\Real Estate Worth Estimator\house\USA_Housing.csv')
    df.head()
    x=df.iloc[:,0:5].values

    y=df['Price'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

    lm = LinearRegression()

    lm.fit(x_train,y_train)

    pred=lm.predict(x_test)
    
    prediction=lm.predict([[a,b,c,d,e]])
    
    return prediction[0]

def remove(string):
    return string.replace(" ","")

def getvalues():
    global answer
    AAI=e1.get()
    AAHA=e2.get()
    AANOR=e3.get()
    AANOB=e4.get()
    AP=e5.get()
    AAI=remove(AAI)
    AAHA=remove(AAHA)
    AANOR=remove(AANOR)
    AANOB=remove(AANOB)
    AP=remove(AP)
    
    
    if AAI.isalpha():
        messagebox.showinfo('Error','INVALID INPUT')
    elif  AAHA.isalpha():
        messagebox.showinfo('Error','INVALID INPUT')
    elif  AANOR.isalpha():
        messagebox.showinfo('Error','INVALID INPUT')
    elif  AANOB.isalpha():
        messagebox.showinfo('Error','INVALID INPUT')
    elif  AP.isalpha():
        messagebox.showinfo('Error','INVALID INPUT')
        
    elif AAI=='':
        messagebox.showinfo('Error','INVALID INPUT')
        
    elif AAHA =='':
        messagebox.showinfo('Error','INVALID INPUT')
    elif AANOR =='':
        messagebox.showinfo('Error','INVALID INPUT')
    elif AANOB =='':
        messagebox.showinfo('Error','INVALID INPUT')
    elif AP =='':
        messagebox.showinfo('Error','INVALID INPUT')
        
    else:
        AAI=float(AAI)
        AAHA=float(AAHA)
        AANOB=float(AANOB)
        AANOR=float(AANOR)
        AP=float(AP)
        answer= ML(AAI,AAHA,AANOR,AANOB,AP)
       # messagebox.showinfo('SUCCESS',answer)
        root.destroy()
        import result 
def result():
	x=answer
	return x	

root.state('zoomed')
root.resizable(width=False,height=False)
canvas=Canvas(root,width=1910,height=1070)
image=ImageTk.PhotoImage(Image.open(r'C:\Users\anujb\OneDrive\Desktop\Real Estate Worth Estimator\house\png-format-1571400415903444040gamerwallpapers295727741120.png'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

l=Label(root,text='Estimator',fg='red4',bg='orange',font=('',60,'bold'))
l.place(x=750,y=10)

l1=Label(root,text='Avg. Area Income : ',bg='orange',fg='red4',font=('',20,'bold'))
l1.place(x=550,y=200)
e1=Entry(root,font=('',20,'bold'))
e1.configure(background='orange')
e1.place(x=1050,y=200)

l2=Label(root,text='Avg. House Age : ',bg='orange',fg='red4',font=('',20,'bold'))
l2.place(x=550,y=350)
e2=Entry(root,font=('',20,'bold'))
e2.configure(background='orange')
e2.place(x=1050,y=350)

l3=Label(root,text='Number of Rooms : ',bg='orange',fg='red4',font=('',20,'bold'))
l3.place(x=550,y=500)
e3=Entry(root,font=('',20,'bold'))
e3.configure(background='orange')
e3.place(x=1050,y=500)

l4=Label(root,text='Number of Bedrooms : ',bg='orange',fg='red4',font=('',20,'bold'))
l4.place(x=550,y=650)
e4=Entry(root,font=('',20,'bold'))
e4.configure(background='orange')
e4.place(x=1050,y=650)

l5=Label(root,text='Avg. Area Population : ',fg='red4',bg='orange',font=('',20,'bold'))
l5.place(x=550,y=800)
e5=Entry(root,font=('',20,'bold'))
e5.configure(background='orange')
e5.place(x=1050,y=800)


b=Button(root,command=getvalues,text='Submit',justify='center',font=('',30,'bold'),bg='orange',fg='red4')
b.place(x=850,y=950)

root.mainloop()