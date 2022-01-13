import yagmail

sender = ''
receiver = ''
password = ''

subject = 'This is the subject'

contents = 'Here is the content of the email. Hi!'

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")


# Run using python3 main.py
