import sys
import smtplib
from smtplib import*

# removing extra traceback
sys.tracebacklimit = 0

for i in range(1,66):
    try:  
        # user name 
        gmail_user = "dimetryi1212@gmail.com"
        
        # application password (use 2FA (google account))
        gmail_pswrd = "prenedodnxshxovc"
        
        TO = 'dimetryi1212@gmail.com'
        SUBJECT = "Testing sending using gmail"
        TEXT = "Testing sending mail using gmail servers"
        BODY = '\r\n'.join(['To: %s' % TO,
                'From: %s' % gmail_user,
                'Subject: %s' % SUBJECT,
                '', TEXT])
        
        # connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        
        # identification
        server.ehlo()
        
        # encryption
        server.starttls()
        server.ehlo()
        
        # authorization
        server.login(gmail_user, gmail_pswrd)
        
        # sending
        server.sendmail(gmail_user, [TO], BODY)
        print("sending email #" + str(i))
        print("Successfully sent email")
        
    except SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        print("Error code:" + error_code)
        print("Message:" + error_message)
        if (error_code==422):
            print("Recipient Mailbox Full")
        elif(error_code==431):
            print("Server out of space")
        elif(error_code==447):
            print("Timeout. Try reducing number of recipients")
        elif(error_code==510 or error_code==511):
            print("One of the addresses in your TO, CC or BBC line doesn't exist.",
                  "Check again your recipients' accounts and correct any possible misspelling.")
        elif(error_code==512):
            print("Check again all your recipients' addresses:",
                  "there will likely be an error in a domain name (like mail@domain.coom instead of mail@domain.com)")
        elif(error_code==541 or error_code==554):
            print("Your message has been detected and labeled as spam. You must ask the recipient to whitelist you")
        elif(error_code==550):
            print("Though it can be returned also by the recipient's firewall (or when the incoming server is down),",
                  "the great majority of errors 550 simply tell that the recipient email address doesn't exist.",
                  "You should contact the recipient otherwise and get the right address.")
        elif(error_code==553):
            print("Check all the addresses in the TO, CC and BCC field. There should be an error or a misspelling somewhere.")
        else:
            print(error_code + ": " + error_message)
            
    finally:        
        server.quit()