import smtpd
import smtplib

from smtplib import SMTP_SSL

#server = smtplib.SMTP('emea.relay.ibm.com',587)
content = 'example email stuff here'

mail = smtplib.SMTP('emea.relay.ibm.com',587)

mail.ehlo()
mail.starttls()
#mail.login('suyash456@gmail.com','iamthebest1989')

mail.login('1suyash@my.ibm.com','ilusssm@1323')

mail.sendmail('1suyash@my.ibm.com','suyash_yadav@persistent.co.in',content)

mail.close()

#server = SMTP_SSL('emea.relay.ibm.com',25)

#server.login("1suyash@my.ibm.com", "ilusssm@1323")

#Send the mail
#msg = "Hello!" # The /n separates the message from the headers
#server.sendmail("1suyash@my.ibm.com","suyash_yadav@persistent.co.in",msg)
#print("hey its done")