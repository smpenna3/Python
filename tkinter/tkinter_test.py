from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", bg='blue', command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.test = Button(frame, text='Test', command=self.testcommand)
        self.test.pack(side=BOTTOM)

        w = Label(frame, text='will this work')
        w.pack(side=RIGHT)

    def say_hi(self):
        print "hi there, everyone!"

    def testcommand(self):
    	print "Test"

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below