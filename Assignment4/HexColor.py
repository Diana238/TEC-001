# followed by exactly 6 characters (digits 0-9 or letters A-F, case insensitive). Write a function that checks if a given string is a valid hex color or not.
def hex_code(color):
    if len(color) != 7:
        return False
    if not color.startswith("#"):
        return False
    if not color[1:].upper() in "ABCDEF" or not color[1:].isdigit():
        return False
    return True
hex = input("Type your hex color code:")
if hex_code(hex):
    print("Your hex color code is valid")
else:
    print("Your code have some problem")