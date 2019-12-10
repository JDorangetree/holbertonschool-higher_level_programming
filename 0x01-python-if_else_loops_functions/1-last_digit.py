#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number_positive = number * -1
    last_digit = (number_positive % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print('last digit of {:d} is {:d} and is greater than 5'.format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print('last digit of {:d} is {:d} and is less than 6 and not 0'.format(number, last_digit))
else:
    print('last digit of {:d} is {:d} and is 0'.format(number, last_digit))
