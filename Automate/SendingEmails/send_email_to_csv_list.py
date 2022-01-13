import yagmail
import pandas

sender = ''

password = ''

subject = 'This is the subject'


# yag = yagmail.SMTP(user=sender, password=password)

df = pandas.read_csv('contacts.csv')
print(df)

for index, row in df.iterrows():
    contents = f"Hi {row['name'] this is the email contents}"
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)

# Run using python3 main.py
