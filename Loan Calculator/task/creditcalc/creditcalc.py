import math
operation_type = input(r"""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: """)

if operation_type == "n":
    loan_principal = int(input("Enter the loan principal: "))
    monthly_payment = int(input("Enter the monthly payment: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    n = math.ceil(math.log(monthly_payment / (monthly_payment - (i * loan_principal)), 1 + i))
    years = n // 12
    months = n % 12
    if years:
        if months:
            print("It will take", years, "years and", months, "months to repay this loan!")
        else:
            print("It will take", years, "years to repay this loan!")
    else:
        print("It will take", months, "months to repay this loan!")
elif operation_type == "a":
    loan_principal = int(input("Enter the monthly payment: "))
    periods = int(input("Enter the number of periods: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    monthly_payment = loan_principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print("Your monthly payment = " + str(math.ceil(monthly_payment)) + "!")
elif operation_type == "p":
    payment = float(input("Enter the annuity payment: "))
    periods = int(input("Enter the number of periods: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    loan_principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print("Your loan principal = " + str(round(loan_principal)) + "!")