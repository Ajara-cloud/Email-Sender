import smtplib

to =  input("Enter recepient email address: \n")
subject = input("Enter subject: \n")
content =  input("Type message here: \n")
sender = input("Enter your email address: \n")  # Enter your email address
password = input("Enter your email password: \n")   # Enter your email password

def sendEmail(to, subject, content):
    server =smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password) 
    message = f"Subject: {subject}\n\n{content}"
    server.sendmail(sender, to, message)
    server.close() 
    print("Email has been sent to ", to)    

sendEmail(to, subject, content)