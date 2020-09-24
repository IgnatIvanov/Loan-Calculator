import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

if args.type:
    if args.type == "annuity":
        if args.payment:
            if args.principal:  # calculating periods
                if args.interest:
                    loan_principal = int(args.principal)
                    monthly_payment = int(args.payment)
                    i = float(args.interest) / (12 * 100)
                    if loan_principal > 0 and monthly_payment > 0 and i > 0:
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
                        print("Overpayment = " + str(round(monthly_payment * n - loan_principal)))
                    else:
                        print("Incorrect parameters")
                else:
                    print("Incorrect parameters")
            else:  # calculating annuity loan principal
                if args.periods and args.interest:
                    payment = float(args.payment)
                    periods = int(args.periods)
                    i = float(args.interest) / (12 * 100)
                    if payment > 0 and periods > 0 and i > 0:
                        loan_principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
                        print("Your loan principal = " + str(math.floor(loan_principal)) + "!")
                        print("Overpayment = " + str(round(payment * periods - math.floor(loan_principal))))
                    else:
                        print("Incorrect parameters")
                else:
                    print("Incorrect parameters")
        else:  # calculating annuity payment
            if args.principal and args.periods and args.interest:
                loan_principal = int(args.principal)
                periods = int(args.periods)
                i = float(args.interest) / (12 * 100)
                if loan_principal > 0 and periods > 0 and i > 0:
                    monthly_payment = loan_principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
                    print("Your monthly payment = " + str(math.ceil(monthly_payment)) + "!")
                    print("Overpayment = " + str(math.ceil(monthly_payment) * periods - loan_principal))
                else:
                    print("Incorrect parameters")
            else:
                print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal and args.periods and args.interest:
            P = int(args.principal)
            n = int(args.periods)
            i = float(args.interest) / 12 / 100
            if P > 0 and n > 0 and i > 0:
                sum = 0
                for m in range(1, n + 1, 1):  # Calculating monthly payments
                    D = P / n + i * (P - (P * (m - 1) / n))
                    D = math.ceil(D)
                    sum += D
                    print("Month " + str(m) + ": payment is " + str(D))
                print("Overpayment = " + str(sum - P))
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")
