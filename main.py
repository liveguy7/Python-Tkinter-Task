from tkinter import *
import sqlite3

app = Tk()
app.geometry('400x400')


def submit():
  conn = sqlite3.connect('jello.db')
  c = conn.cursor()

  c.execute("INSERT INTO tblJello VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
        })
  
  conn.commit()
  conn.close()
  
  f_name.delete(0, END)
  l_name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  state.delete(0, END)
  zipcode.delete(0, END)

def queryAll():
  conn = sqlite3.connect('jello.db')
  c = conn.cursor()

  c.execute("SELECT *, oid FROM tblJello")
  n = c.fetchall()
  print(n)

  print_records = ''
  for i in n:
    print_records += str(i[0]) + '\n'

  query_label = Label(app, text=print_records)
  query_label.grid(row=8, column=0, columnspan=2)

  
  conn.commit()
  conn.close()
  

f_name = Entry(app, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(app, width=30)
l_name.grid(row=1, column=1)
address = Entry(app, width=30)
address.grid(row=2, column=1)
city = Entry(app, width=30)
city.grid(row=3, column=1)
state = Entry(app, width=30)
state.grid(row=4, column=1)
zipcode = Entry(app, width=30)
zipcode.grid(row=5, column=1)

f_name_label = Label(app, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(app, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(app, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(app, text='City')
city_label.grid(row=3, column=0)
state_label = Label(app, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(app, text='Zip')
zipcode_label.grid(row=5, column=0)

submit_btn = Button(app, text="Add", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

query_btn = Button(app, text="Show All", command=queryAll)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=10)


app.mainloop()




