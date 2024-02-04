from tkinter import *

root = Tk()

e = Entry(root, width=25, bg="white", fg="red")
e.pack()
e.insert(0, "enter info... ")

def myClick():
  jello = 'jello ' + e.get()
  myLabel = Label(root, text=jello)
  myLabel.pack()

myButton = Button(root, text='Submit', command=myClick)
myButton.pack()

root.mainloop()


