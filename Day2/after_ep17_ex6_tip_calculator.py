print("Welcome to the tip calculator!")
bill_amount = input("What was the total bill? ")
tip_percentage = input("How much tip would you like to give? 10, 12 or 15? ")
tip_amount = int(tip_percentage) / 100
number_of_people = input("How many people to split the bill? ")

amount_to_be_paid = round((float(bill_amount) + (float(bill_amount) * tip_amount))/int(number_of_people), 3)

print(f"Each person should pay: {amount_to_be_paid}")