#Your university uses course codes that consist of 3 uppercase letters, followed by 3 digits (e.g., "TEC001"). Write a function that returns True if a given string matches this format and False otherwise.
def course_code(code):
    if len(code) != 6:
        return False
    if not code[:3].isupper() or not code[:3].isalpha():
        return False
    if not code[3:].isdigit():
        return False
    return True
course = input("please type course code:")
if course_code(course):
    print("valid code")
else :
    print("Your code is not valid")
