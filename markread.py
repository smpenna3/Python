import imaplib
obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login('parkerraspberrypi@gmail.com', 'Panthers1995')
obj.select('Inbox')
typ, data = obj.search(None, '(SINCE 11-Jun-2015)')
for num in data[0].split():
   obj.store(num, '+FLAGS', '\\Seen')


#SINCE will do emails after that date
#BEFORE will do emails before that date