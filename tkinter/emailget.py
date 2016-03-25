from Tkinter import *
import feedparser

month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"

root = Tk()
root.title('Parker Raspberry Pi Email')

sender = Label(root, text='From', width=20, font=('Helvetica', 12, 'bold'))
sender.grid(row=1, column=0)

subject = Label(root, text='Subject', width=20, font=('Helvetica', 12, 'bold'))
subject.grid(row=1, column=1)

body = Label(root, text='Message', width=50, font=('Helvetica', 12, 'bold'))
body.grid(row=1, column=2)

timereceived = Label(root, text='Time', width=5, font=('Helvetica', 12, 'bold'), anchor=E)
timereceived.grid(row=1, column=3)

	

sendera = []
subjecta = []
bodya = []
timea = []

def getmail():
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	def readmail():
		currentmail = Toplevel()


	for i in range(0, unread_count):
		sendera.append(Button(root, text=str(response['items'][i].author_detail.name), width=20, anchor=W, bd=0))
		sendera[i].grid(row=(i+2), column=0, sticky=W)

		subjecta.append(Button(root, text=str(response['items'][i].title), width=20, anchor=W, bd=0))
		subjecta[i].grid(row=(i+2), column=1, sticky=W)

		bodya.append(Button(root, text=str(response['items'][i].summary_detail.value), width=50, anchor=W, bd=0))
		bodya[i].grid(row=(i+2), column=2, sticky=W)

		timea.append(Label(root, text=(str(month[list(response['items'][i].updated_parsed)[1]]) + ' ' + str(list(response['items'][i].updated_parsed)[2])), anchor=E))
		timea[i].grid(row=(i+2), column=3, sticky=E)

getmail()

refresh = Button(root, text='Refresh', width = 95, command=getmail)
refresh.grid(row = 0, column=0, columnspan = 4)

root.mainloop()