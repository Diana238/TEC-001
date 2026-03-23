#1 sorting
def sorting():
    list = []
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        list.append(int(number))
    list.sort(reverse=True)
    print("Five greatest numbers sorted in descending order:", list[0:5])

#2 prime
def prime():
    number = int(input("Enter a number: "))
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

#3 city
def city():
    list = []
    for i in range(5):
        city = input("Enter a city: ")
        list.append(city)
    for o in list:
        print(o)

#4 sum
def sum():
    list = input("Enter a list of number: ")
    total = 0
    for i in list.split(","):
        total += int(i)
    return total
print(sum())

#5 odd
def odd():
    inputlist = input("Enter list of numbers: ")
    originallist = []
    for i in inputlist.split(","):
        originallist.append(int(i))
    cutdownlist = []
    for o in originallist:
        if o % 2 == 0:
            cutdownlist.append(o)
    print("The original:", originallist)
    print("The cut-down:", cutdownlist)