"""
Coder: James J. Yang

This module is based on smtplib, packing some funcions to make it more easier to send mail.
As it is planned for 'simple used', CC and BCC are not supported.

The sample is,
    x = SendMail('smtp.gmail.com', 465, SSL = True)
    x.debugmode()
    x.loginserver('username@gmail.com', 'password')
    x.setmsgbody('username@gmail.com', ['username@gmail.com'], 'Subject -> Test', 'How are you?', ['username@gmail.com'], ['username@gmail.com'])
    x.addattachment(['SendMail_Postfix.py'])
    x.sendmail()


History:
1.0, 2014-07-31

"""


import os
from smtplib import SMTP, SMTP_SSL
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

class SendMail:

    def __init__(self, MailServer = 'cs-mta.carestreamhealth.com', MailPort = 25, SSL = False, Timeout = 5):
        self.MailServer = MailServer
        self.MailPort = MailPort
        self.Timeout = Timeout
        self.msg = MIMEMultipart()
        if SSL:
            self.Connection = SMTP_SSL(self.MailServer, self.MailPort, self.Timeout)
        else:
            self.Connection = SMTP(self.MailServer, self.MailPort, self.Timeout)

    def debugmode(self, switch = 1):
        self.Connection.set_debuglevel(switch)

    def loginserver(self, user, password):
        self.Connection.login(user, password)

    def setmsgbody(self, FROM, TO, SUBJECT, BODY):
        self.msg['From'] = FROM
        self.msg['To'] = COMMASPACE.join(TO)
        self.msg['Date'] = formatdate(localtime = True)
        self.msg['Subject'] = SUBJECT
        self.msg.attach(MIMEText(BODY))

    def addattachment(self, filelist):
        for i in filelist:
            j = MIMEBase('application', "octet-stream")
            j.set_payload(open(i,"rb").read())
            Encoders.encode_base64(j)
            j.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(i))
            self.msg.attach(j)

    def sendmail(self):
        self.Connection.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.Connection.close()
