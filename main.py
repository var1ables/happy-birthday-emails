import datetime as dt
import pandas
import random
import smtplib

#Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

MY_EMAIL = 'youremail@email.com'
MY_PASS = 'strongpasswordhere'



right_now = dt.datetime.now()
today = (right_now.month, right_now.day)

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(row['month'], row['day']): row for (index, row) in data.iterrorws()}

if today in birthday_dict:
    person = birthday_dict[today]
    filepath = f'letter_templates/letter_{random.randint(1,3)}'
    with open(filepath) as letter:
        contents = letter.read()
        contents = contents.replace('[NAME]', person['name'])

    with smtplib.SMTP('smtp.email.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person['email'])
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person['email'],
            msg=f'Subject: Happy Birthday \n\n {contents}'
        )


