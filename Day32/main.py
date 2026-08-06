import smtplib
import random
import datetime as dt

now =  dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(
            user="noreply@200oksolutions.com",
            password="lycgsdbrgsdsvlqz"
        )

        connection.sendmail(
            from_addr="noreply@200oksolutions.com",
            to_addrs="kushc@200oksolutions.com",
            msg=f"Subject: Today's quote\n\n{quote}"
        )
