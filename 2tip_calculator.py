# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.


print(f"Welcome to the tip calculator.")
total = int(input("What was the total bill?\n£"))
percentage = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))


total_tip = total * percentage / 100
total_person = "{:.2f}".format(total_tip / people)


print(f"Each person should pay: £{total_person}")
