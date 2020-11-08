from tkinter import *

root=Tk()
#label Widget
myLabel = Label(root,text="Hello World!")
myLabel2 = Label(root,text="My name is Aylin.")

#Shoving it onto the screen
myLabel.pack()

myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)


root.mainloop()
