# Define colors
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

#Write a program that asks your name and then greets you by your name.
name = input(f"{CYAN}What is your name ?{RESET}")
print(f"Hello!,{name.title()} Nice to meet you.我的名字交锋")

#Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle.
import math
radius_str = input(f"{CYAN}What is radius of your circle ?")
radius = float(radius_str)
circumference = 2 * math.pi * radius
print(f"The circumference {radius} rad is {circumference:.2f}{RESET}")

#Write a program that asks the user for the length and width of a rectangle.
print(f"{GREEN}Now give me the rectangle.{RESET}")
length = float(input(f"{CYAN}What is the length?{RESET}"))
Width = float(input(f"{CYAN}What is the width?{RESET}"))
perimeter = (length + Width) *2
area = length * Width   
print(f"{GREEN}Your rectangle's perimeter is {perimeter}  and area is {area}{RESET}")

#Write a program that asks the user for three integer numbers.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
total = num1 + num2 + num3
product = num1 * num2 * num3
average = total / 3
print("Sum:", total)
print("Product:", product)
print("Average:", average)

# Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots.
GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = int(input("Enter lots: "))
total_grams = (
    talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT +
    pounds * LOTS_PER_POUND * GRAMS_PER_LOT +
    lots * GRAMS_PER_LOT
)
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The weight is {kilograms} kilograms and {grams:.2f} grams.")

 #Write a program that draws two random combinations of numbers for a combination lock:
import random
combo1 = [random.randint(0, 9) for _ in range(3)]
combo2 = [random.randint(1, 40) for _ in range(4)]
print("First combination:", " ".join(map(str, combo1)))
print("Second combination:", " ".join(map(str, combo2)))
