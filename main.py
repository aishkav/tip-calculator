print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

total_tip = ((tip / 100) * bill) + bill
bill_per_person = total_tip / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
