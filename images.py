from tkinter import *
import image
from pillow import ImageTk, image

app = Tk()
app.title('Images')

my_img = ImageTk.PhoteImage(image.open('running4.jpg'))
my_label = Label(app, image=my_img)
my_label.pack()

app.mainloop()

