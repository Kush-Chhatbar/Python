import sys
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L? ").lower()
if(size != "s" and size != "m" and size != "l"):
    print("Please select size from the provided size option")
    sys.exit()

pepperoni = input("Do you want pepperoni on pizza? Y or N: ").lower()
if(pepperoni != "y" and pepperoni != "n"):
    print("Please say only yes or no.")
    sys.exit()

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if(extra_cheese != "y" and extra_cheese != "n"):
    print("Please say only yes or no.")
    sys.exit()

final_bill = 0
pay_as_per_size = 0
pay_as_per_addition_of_pepperoni = 0
pay_as_per_extra_cheese = 0

if size == "s" or size == "S":
    pay_as_per_size += 15
    final_bill += pay_as_per_size
    if pepperoni == "y" or pepperoni == "Y":
        pay_as_per_addition_of_pepperoni += 2
        final_bill += pay_as_per_addition_of_pepperoni
    if extra_cheese == "y" or extra_cheese == "Y":
        pay_as_per_extra_cheese += 1
        final_bill += pay_as_per_extra_cheese
elif size == "m" or size == "M":
    pay_as_per_size += 20
    final_bill += pay_as_per_size
    if pepperoni == "y" or pepperoni == "Y":
        pay_as_per_addition_of_pepperoni += 3
        final_bill += pay_as_per_addition_of_pepperoni
        print(f"Bill before adding extra_cheese: {final_bill}")
    if extra_cheese == "y" or extra_cheese == "Y":
        pay_as_per_extra_cheese += 1
        final_bill += pay_as_per_extra_cheese
elif size == "l" or size == "L":
    pay_as_per_size += 25
    final_bill += pay_as_per_size
    if pepperoni == "y" or pepperoni == "Y":
        pay_as_per_addition_of_pepperoni += 3
        final_bill += pay_as_per_addition_of_pepperoni
    if extra_cheese == "y" or extra_cheese == "Y":
        pay_as_per_extra_cheese += 1
        final_bill += pay_as_per_extra_cheese

else:
    print("Please select out of the provided size option")

print(f"Total bill: {final_bill}")


    
