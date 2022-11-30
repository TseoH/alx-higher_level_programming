#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
less_than_mgs = 'and is less than 6 and not 0'
if number > 5:
    print(f'Last digit of {number:d} is {last_digit:d} and is greater than 5')
elif number == 0:
    print(f'Last digit of {number:d} is {last_digit:d} and is 0')
elif number < 0:
    print(f'Last digit of {number:d} is -{last_digit:d} {less_than_mgs}')
else:
    print(f'Last digit of {number:d} is {last_digit:d} {less_than_mgs}')
