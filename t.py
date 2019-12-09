from tkinter import *
import os
root=Tk()
root.title("Note Taking")
p=Label(root,text="Note taking app", height="18",width="250",bg='brown',fg='white',font=('Helvetica','20','bold','italic'))
p.pack()
root.configure(bg='brown')
root.geometry('400x600')
def notes():
    import functions
button=Button(root,text="Launch app",command=root.destroy,bg = "black",fg='black',padx=65,pady=8,font=('Helvetica','10','bold'))
button.pack(padx=25,pady=10)
butt1=Button(root,text="Exit",command=notes,bg = "black",fg='black',padx=40,pady=10,font=('Helvetica','10','bold'))
butt1.pack(padx=25,pady=0)
root.mainloop()

import tkinter.filedialog
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Notetaking app')

nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')

f1 = Text(root)
f2 = Text(root)
f3 = Text(root)
f4 = Text(root)
f5 = Text(root)
f6 = Text(root)

nb.add(f1, text='Biology')
nb.add(f2, text='History')
nb.add(f3, text='Drama')
nb.add(f4, text='Coding')
nb.add(f5, text='Physics')
nb.add(f6, text='Homework')

root.mainloop()
