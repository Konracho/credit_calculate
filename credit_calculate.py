import math
import argparse

def credit_calculate():
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:''')
    want_to_calculate = input()
    if want_to_calculate == 'm':
        print('Enter the monthly payment:')
        monthly_payment = int(input())
        months = math.ceil(loan_principal / monthly_payment)
        if months != 1:
            print(f'It will take {months} months to repay the loan')
        else:
            print(f'It will take {months} month to repay the loan')
    else:
        print('Enter the number of months:')
        number_of_months = int(input())
        payment = round(loan_principal / number_of_months, 2)
        # print(f'Your monthly payment = {payment}')
        if payment != math.ceil(payment):
            payment_last = loan_principal - (number_of_months - 1) * math.ceil(payment)
            print(f'Your monthly payment = {math.ceil(payment)} and the last payment = {payment_last}.')
        else:
            print(f'Your monthly payment = {payment}')

parser = argparse.ArgumentParser()

parser.add_argument('--principal', type=int, help='Основная сумма кредита' )
parser.add_argument('--periods', type=int, help='количество месяцев' )
parser.add_argument('--interest', type=float, help='процентная ставка')
parser.add_argument('--payment', type=float, help='сумма платежа')
parser.add_argument('--type', type=str, help='тип платежа: diff or annuity')

args = parser.parse_args()

def number_monthly_payments(type, principal, payment, interest):  # количество платежей
    i = (interest / (12 * 100))
    periods = math.log(payment / (payment - i * principal), 1 + i)
    periods = math.ceil(periods)
    years = periods // 12  # лет платить
    months = periods % 12  # и месяцев платить
    overpayment = (payment * periods) - principal

    if years == 0 and months == 1:
        print(f'It will take {months} month to repay this loan!')
        print('')
        print(f'Overpayment = {overpayment}')

    elif years == 1 and months == 0:
        print(f'It will take {years} year to repay this loan!')
        print('')
        print(f'Overpayment = {overpayment}')

    elif years == 0 and months > 1:
        print(f'It will take {months} months to repay this loan!')
        print('')
        print(f'Overpayment = {overpayment}')

    elif years > 1 and months == 0:
        print(f'It will take {years} years to repay this loan!')
        print('')
        print(f'Overpayment = {overpayment}')

    else:
        print(f'It will take {years} years and {months} months to repay this loan!')
        print('')
        print(f'Overpayment = {overpayment}')

def monthly_payment(type, principal, periods, interest):  # ежемесячный платёж (ануитентный платёж)
    i = (interest / (12 * 100))
    payment = principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    payment = math.ceil(payment)
    overpayment = (payment * periods) - principal
    print(f'Your monthly payment = {payment}!')
    print('')
    print(f'Overpayment = {overpayment}')

def loan_principal(type, payment, periods, interest): # основная сумма кредита
    i = (interest / (12 * 100))
    # n = math.log(1 + i) * (payment / (payment - i * principal))
    principal = payment // ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    principal = math.ceil(principal)
    overpayment = math.ceil(payment * periods) - principal
    print(f'Your loan principal = {principal}!')
    print('')
    print(f'Overpayment = {overpayment}')

def differentiated_payments(tupe, principal, periods, interest):
    i = (interest / (12 * 100))
    result = 0
    for m in range(1, periods + 1):
        differentiated = (principal // periods) + i * (principal - (((principal * (m - 1))) // periods))
        differentiated = math.ceil(differentiated)
        result += differentiated
        overpayment = result - principal
        print(f'Month {m}: payment is {differentiated}')
    print('')
    print(f'Overpayment = {overpayment}')

if args.type == 'diff' and args.principal and args.periods:
    if args.principal == None or args.periods == None or args.interest == None:
        print('Incorrect parameters')
    elif args.principal < 0 or args.periods < 0 or args.interest < 0:
        print('Incorrect parameters')
    else:
        differentiated_payments(args.type, args.principal, args.periods, args.interest)

elif args.type == 'annuity' and args.principal and args.payment:
    if args.principal == None or args.payment == None or args.interest == None:
        print('Incorrect parameters')
    elif args.principal < 0 or args.interest < 0 or args.payment < 0:
        print('Incorrect parameters')
    else:
        number_monthly_payments(args.type, args.principal, args.payment, args.interest)

elif args.type == 'annuity' and args.principal and args.periods:
    if args.principal == None or args.periods == None or args.interest == None:
        print('Incorrect parameters')
    elif args.principal < 0 or args.periods < 0 or args.interest < 0:
        print('Incorrect parameters')
    else:
        monthly_payment(args.type, args.principal, args.periods, args.interest)

elif args.type == 'annuity' and args.payment and args.periods:
    if args.payment == None or args.periods == None or args.interest == None:
        print('Incorrect parameters')
    elif args.periods < 0 or args.interest < 0 or args.payment < 0:
        print('Incorrect parameters')
    else:
        loan_principal(args.type, args.payment, args.periods, args.interest)

else:
    print('Incorrect parameters')


# без пробелов 120 строк.
