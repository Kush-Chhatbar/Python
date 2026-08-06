##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import datetime as dt
import random
import smtplib

data = pd.read_csv("birthdays.csv")
new_data = data.to_dict(orient="records")
birthdays_dict = {}
birthdays_dict = {(person["month"], person["day"]): person for person in new_data}
print(birthdays_dict)

today = dt.datetime.today()
today_month = today.month
today_day = today.day

birthday = (today_month, today_day)
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
print(birthday)
if birthday in birthdays_dict:
    person_name = birthdays_dict[birthday]["name"]
    person_email = birthdays_dict[birthday]["email"]
    chosen_letter = random.choice(letters)
    print(chosen_letter)
    with open(chosen_letter, mode="r") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace("[NAME]", person_name)
        with open(f"letter_templates/new_letters/birthday_wishes_{person_name}.txt", mode="w") as birthday_wishes_letter:
            birthday_wishes_letter.write(new_letter)
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
                to_addrs=f"{person_email}",
                msg=f"Subject: Birthday Wishes \n\n{new_letter}"
            )