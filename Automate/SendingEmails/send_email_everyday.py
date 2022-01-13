import yagmail
import time
import datetime import datetime as dt
sender = ''
receiver = ''
password = ''

subject = 'This is the subject'

contents = 'Here is the content of the email. Hi!'

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)

# Run using python3 main.py
