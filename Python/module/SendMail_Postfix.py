import os
from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

# Server
MailServer = 'cs-mta.carestreamhealth.com'
MailPort = 25

# Header
msg = MIMEMultipart()
msg['Subject'] = '[Test Mail] Send Email via Postfix'
msg['From']    = 'jun.yang@carestream.com'
msg['To']      = COMMASPACE.join(['jun.yang@carestream.com'])
msg['Date']    = formatdate(localtime=True)

# Body
msg.attach(MIMEText("""

`python -m this`

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""))

filelist = ['SendMail.py', 'ClassicalMultiThreadSample.py']
for i in filelist:
    j = MIMEBase('application', "octet-stream")
    j.set_payload(open(i,"rb").read())
    Encoders.encode_base64(j)
    j.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(i))
    msg.attach(j)

smtp = SMTP(MailServer, MailPort, timeout = 10)
smtp.set_debuglevel(1)
smtp.sendmail(msg['from'], msg['to'], msg.as_string())
