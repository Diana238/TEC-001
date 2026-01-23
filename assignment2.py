
def zander():
    a = float(input("Enter the length of a zander in centimeters: "))
    if a < 42:
        print("Please release the fish back into the lake, because it shorter than the size limit", 42 - a, "cm.")
        print("A zander must be 42 centimeters or longer to meet the size limit.")
    else:
        print("You can take the fish home.")
#zander()

def carbin_class():
    a = input("Enter the cabin class of a cruise ship: ")
    if a == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif a == "A":
        print("Above the car deck, equipped with a window.")
    elif a == "B":
        print("Windowless cabin above the car deck.")
    elif a == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid carbin class.")
#carbin_class()

def value(x, y):
    z = int(input("Enter hemoglobin value (g/l): "))
    if z > y:
        print("Your hemoglobin value is high")
    elif z < x:
        print("Your hemoglobin value is low")
    else:
        print("Your hemoglobin value is normal")
def hemoglobin():
    a = True
    while a == True:
        b = input("Enter biological sex(Male or Female): ")
        if b == "Male":
            value(134, 167)
            a = False
        elif b == "Female":
            value(117, 155)
            a = False
        else:
            print("Invalid biological sex, please rewrite")
#hemoglobin()

def leap_year():
    a = int(input("Enter the year: "))
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
#leap_year()

import math
def cal(x):
    a = float(input(f"Enter the diameter of the {x} round pizza(cm): "))
    b = float(input(f"Enter the price of the {x} pizza(USD): "))
    c = b / (((a / 100)  / 2) ** 2 * math.pi)
    return c
def com():
    a = cal("first")
    b = cal('second')
    if a < b:
        print("The first pizza provides better value for money")
    else:
        print("The second pizza provides better value for money")
com()