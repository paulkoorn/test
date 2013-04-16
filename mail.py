import smtplib

TO = 'paul_koorn@hotmail.com'
GMAIL_USER = 'paultjekoorn'
GMAIL_PASS = '@tl@s1989'

SUBJECT = 'Intrusion!!'
TEXT = 'Your PIR sensor detected movement'


def send_email():
	print("Sending Email")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(GMAIL_USER, GMAIL_PASS)
	header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
	header = header + '\n' + 'Subject:' + SUBJECT + '\n'
	print header
	msg = header + '\n' + TEXT + ' \n\n'
	smtpserver.sendmail(GMAIL_USER, TO, msg)
	smtpserver.close()
send_email()