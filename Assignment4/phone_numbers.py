#Write a function that replaces any sequence of 10 digits or those that starts with "+84" with the string
import re
def hide_phone_numbers(text):
    pattern = r'\b\d{10}\b|\+84\d{9}\b'
    return re.sub(pattern, '[REDACTED]', text)
while True:
    document = input('Enter text (press Enter to stop): ')
    if document == '':
        break
    print(hide_phone_numbers(document))