import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com", port = 587 )
    server.starttls()
    
    ## receiver mail
    receiver_mail = input("Enter the receiver mail : ")
    
    ## mail credentials
    sender_email = "khushiguptakg2004@gmail.com"
    password = "klmb phiv vuvc calj"
    
    ## login
    server.login(sender_email,password)
    
    ## sending email
    subject = input("Enter the subject : ")
    body = input("Enter the body : ")
    message = f"subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("Email sent successfully")
    
    server.quit()
except Exception as e:
    print("An error occurred",e)
    