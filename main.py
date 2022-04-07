import functools
import math

home_payment = 15000
food_payment = 13000
internet_payment = 250 + 250 + 450

payments = [home_payment, food_payment, internet_payment]

percentages = []
clears = []


def calculate(salary, payment):
    percentage_of_payment = math.ceil((payment / salary) * 100)
    return percentage_of_payment


for payment in payments:
    percentage = calculate(35000, payment)

    percentages.append(percentage)
    clears.append(payment)

    print(f"Percentage: {percentage}, clear: {payment}")

calculated_percentages = functools.reduce(lambda a, b: a+b, percentages)
calculated_clears = functools.reduce(lambda a, b: a+b, clears)

print(f"Sum of percentage: {calculated_percentages}")
print(f"Sum of clear: {calculated_clears}")
