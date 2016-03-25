from Tkinter import *

root = Tk()

button1 = Button(root, text='top left', width=20).grid(row=0, column=0)
button2 = Button(root, text='bottom left', width=10).grid(row=1, column=0, sticky=W)
button3 = Button(root, text='top right', width=10).grid(row=0, column=1, sticky=E)
button4 = Button(root, text='bottom right', width=20).grid(row=1, column=1)


top = Toplevel()

button5 = Label(top, text='above', width=30).grid(row=0, column=0, columnspan=2)
button6 = Button(top, text='bottom left', width=10).grid(row=1, column=0)
button7 = Button(top, text='bottom right', width=10).grid(row=1, column=1)


root.mainloop()