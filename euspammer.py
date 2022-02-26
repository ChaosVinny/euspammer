import getpass
import smtplib
from colorama import Fore

print(Fore.MAGENTA+"""

▄▄▄ .▄• ▄▌.▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
▀▄.▀·█▪██▌▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
▐▀▀▪▄█▌▐█▌▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▄▄▌▐█▄█▌▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀  ▀▀▀  ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
 
 """)

smtp_server = 'smtp.gmail.com'
port = 587

email_user       = ''                        
password         = getpass.getpass('Password Account -> : ')       
email_receiver   = ''                        
subject          = ''         
body             = (open("message.txt","r")).read()     
repeat           = input('Tot. Emails: ')         

try:

    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email_user,password)
    print("\nSending To : " + email_receiver)

    for i in range(int(repeat)):
        msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body  
        server.sendmail(email_user,email_receiver,msg)                       
        print("\rEmail Sent - " + str(i+1) )                                 

    server.quit()                                       
    print("\n",repeat,"Email(s) sent successfully \n")  


except smtplib.SMTPAuthenticationError:
    print("\nError Impossibile to use the Account")
    sys.exit()
