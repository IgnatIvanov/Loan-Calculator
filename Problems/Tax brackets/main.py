income = int(input())

if income >= 132407:
    tax = 0.28
elif income >= 42708:
    tax = 0.25
elif income >= 15528:
    tax = 0.15
else:
    tax = 0.00

print("The tax for "
      + str(income)
      + " is "
      + str(round(tax * 100))
      + "%. That is "
      + str(round(income * tax))
      + " dollars!")