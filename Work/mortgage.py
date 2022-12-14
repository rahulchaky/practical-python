# mortgage.py
#
# Exercise 1.7 - 1.11
# Not entirely sure that the math checks out tbh
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000.0

month = 0

while principal > 0:
    month += 1

    if principal * (1+rate/12) - payment < 0:
        principal = 0
        total_paid = total_paid - (principal * (1+rate/12) - payment)
        print(f'{month} {round(total_paid, 2)} {round(principal, 2)}')
        break

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month > extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{month} {round(total_paid, 2)} {round(principal, 2)}')


print(f'Total paid: {round(total_paid, 2)}')
print(f'Months: {month}')
