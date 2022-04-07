import functools
import math

home_payment = 15000
food_payment = 13000
pets_payment = 1500
transport_payment = 2000
internet_payment = 165 + 250 + 350

total_salary = 35000

payments = [home_payment, food_payment, internet_payment, transport_payment, pets_payment]

percentages = []
clears = []


def calculate(salary, payment):
    percentage_of_payment = math.ceil((payment / salary) * 100)
    return percentage_of_payment


for payment in payments:
    percentage = calculate(total_salary, payment)

    percentages.append(percentage)
    clears.append(payment)

    print(f"Percentage: {percentage}, clear: {payment}")

calculated_percentages = functools.reduce(lambda a, b: a+b, percentages)
calculated_clears = functools.reduce(lambda a, b: a+b, clears)

print(f"Sum of percentage: {calculated_percentages}")
print(f"Sum of clear: {calculated_clears}")
print(f"You'll have: {total_salary - calculated_clears}")
