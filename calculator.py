from tkinter import *

root = Tk()
root.title("Calculator Add")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
  #e.delete(0, END)
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current) + str(number))

def buttonClear():
  e.delete(0, END)

def buttonAdd():
  first_number = e.get()
  global fnum
  global math
  math = 'addition'
  fnum = int(first_number)
  e.delete(0, END)

def buttonEqual():
  second_number = e.get()
  e.delete(0, END)
  if(math == 'addition'):
    e.insert(0, fnum + int(second_number))
  elif(math == 'substraction'):
    e.insert(0, fnum - int(second_number))
  elif(math == 'multiplication'):
    e.insert(0, fnum * int(second_number))
  elif(math == 'division' & e.get() == 0):
    e.insert(0, 'cannot divide by 0')
  else:
    e.delete(0, END)


def buttonSubstract():
  first_number = e.get()
  global fnum
  global math
  math = 'substraction'
  fnum = int(first_number)
  e.delete(0, END)

def buttonMultiply():
  first_number = e.get()
  global fnum
  global math
  math = 'multiplication'
  fnum = int(first_number)
  e.delete(0, END)

def buttonDivide():
  first_number = e.get()
  global fnum
  global math
  math = 'division'
  fnum = int(first_number)
  e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
button_add = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
button_equal = Button(root, text="=", padx=91, pady=20, command=buttonEqual)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=buttonClear)
button_subtract = Button(root, text="-", padx=41, pady=20, command=buttonSubstract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=buttonMultiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=buttonDivide)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()




