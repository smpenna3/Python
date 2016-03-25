from Tkinter import *
import time

master = Tk()

e = Text(master, width=40, height=10)
e.grid(row=0, column=0, columnspan=2)

e.focus_set()

def callback():
	s = e.get(1.0, END)
	print(s)
	e.delete(1.0,END)

b = Button(master, text="get", width=10, command=callback)
b.grid(row=1, column=0)

q = Button(master, text='quit', width=10, command=master.quit)
q.grid(row=1, column=1)

mainloop()