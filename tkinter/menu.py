from Tkinter import *

def callback():
    print "called the callback!"

def test():
	newwindow = Toplevel(width =100, height = 100)
	question = Button(newwindow, text='hello', fg = 'RED')
	question.pack(side=LEFT)

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=test)

mainloop()