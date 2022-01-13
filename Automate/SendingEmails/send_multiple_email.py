import yagmail
import time
sender = ''
receiver = ''
password = ''

subject = 'This is the subject'

contents = 'Here is the content of the email. Hi!'

while True:
    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(20)

# Run using python3 main.py
