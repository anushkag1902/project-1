import smtplib 
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls() 
server.login("ccbasketiitjodhpur@gmail.com", "NiveditJain@ooad") 
message = "Hello"
server.sendmail("ccbasketiitjodhpur@gmail.com", "ishayadav139@gmail.com", message) 
server.quit()