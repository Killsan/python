#python -m smtpd -c DebuggingServer -n localhost:1025
import smtplib
import ssl

smtp_server = 'smtp.gmail.com'
port = 465 #587 --unsecure 

sender = 'marshallmethers7@gmail.com'
password = 'perehod2020'
receiver = 'reversflash47@gmail.com'

message = input("Message: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
	server.login(sender, password)
	#sending email
	server.sendmail(sender, receiver, message) 
	print('Sended')


#=====================================UNSECURE CONNECTION====================================


# try:
# 	server = smtplib.SMTP(smtp_server, port)
# 	server.ehlo() #hello for the server 
# 	server.starttls(context = context)
# 	server.ehlo()
# 	server.login(sender, password)
# 	print('Working, again')
# except Exception as e:
# 	pirnt(e)
# finally:
# 	server.quit()


#==========================THE END OF UNSECURE CONNECTION====================================