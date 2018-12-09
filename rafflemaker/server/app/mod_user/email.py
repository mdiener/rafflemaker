from smtplib import SMTP_SSL
# from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email(object):
    def __init__(self):
        self._smtp = SMTP_SSL('webdiener.ch')
        self._username = 'rafflemaker@webdiener.ch'
        self._password = 'xahf4uphu7OY'

    def send_reset_email(self, name, email, link_hash):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Rafflemaker Password Reset Email'
        msg['From'] = 'rafflemaker@webdiener.ch'
        msg['To'] = email

        text = '''\
Hello {name}

You requested a new password on [1]. Click on the following link to change your password. Do not share this link with anyone as it can be used to log in to your account.

https://summerhart.xxx/rafflemaker/user/reset-link?hash={hash}

[1] https://summerhart.xxx/rafflemaker
'''.format(name=name, hash=link_hash)

        html = '''\
<html>
<head></head>
<body>
    <h3>Hello {name}</h3>
    <p>You requested a new password on <a href="https://summerhart.xxx/rafflemaker">RaffleMaker</a>.</p>
    <p>Click on the following link to change your password. Do not share this link with anyone as it can be used to log in to your account.</p>
    <a href="https://summerhart.xxx/rafflemaker/user/reset-link?hash={hash}">Reset Link</a>
    <p>If the above link does not work copy and paste the following into your browser:<br />https://summerhart.xxx/rafflemaker/user/reset-link?hash={hash}</p>
</body>
</html>
'''.format(name=name, hash=link_hash)

        part1 = MIMEText(text, 'text')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        self._sendmsg(msg)

    def _sendmsg(self, message):
        self._smtp.login(self._username, self._password)
        self._smtp.send_message(message)
        self._smtp.quit()
