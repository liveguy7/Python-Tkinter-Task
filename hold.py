
myLabel = Label(root, text='Jello')
myLabel2 = Label(root, text='Jello')

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)


def myClick():
  myLabel = Label(root, text='Enter Name')
  myLabel.pack()

myClick()
myButton = Button(root, text='Submit')
myButton.pack()