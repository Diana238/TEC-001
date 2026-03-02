#Write a function that will find all numbers in a given paragraph, then calculate the sum of all numbers you've found.
import re
def sum_number(text):
    numbers = re.findall('[0-9]+', text)
    total = 0
    for i in numbers:
        total += int(i)
    return total
find = input("How's your day?")
result = sum_number(find)
if result != 0:
    print(result)
else:
    print("There are no numbers")