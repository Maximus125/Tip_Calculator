#Tip Calculator
print("Welcome to Tip Calculator")

bill = float(input("What was your total bill?  $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
people = int(input("How many people to split the bill?\n"))

new_bill = (bill+((tip/100)*bill))/people

print(f"Each person should pay: ${round(new_bill,2)}.")