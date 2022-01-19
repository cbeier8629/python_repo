import yagmail

sender = ''
receiver = ''
password = ''

subject = 'This is the subject'

contents = ['some text here', 'email.txt']

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")


# Run using python3 main.py
