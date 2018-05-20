import smtplib

server = smtplib.SMTP('emea.relay.ibm.com',587)

server.starttls()
server.login("1suyash@my.ibm.com", "icwttlboml@1323")

msg = "YOUR MESSAGE!"
server.sendmail("1suyash@my.ibm.com", "shailesh_joshi@persistent.co.in", msg)
server.quit()


