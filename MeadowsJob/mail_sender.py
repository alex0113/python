import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "av.visarion@gmail.com"
password = "sotrgthxqwuxgagy"

class EmailSender:
    def __init__(self):
        #self.senderList = senderList
        self.context = ssl.create_default_context()
    def sendEmail(self, content):
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=self.context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)

            message = 'Subject: {}\n\n{}'.format("Daily stocks report", content)
            server.sendmail(sender_email, "andrei.macavei89@gmail.com", message)
            print(content)