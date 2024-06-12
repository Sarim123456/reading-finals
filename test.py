import re

def get_special_numeric_input():
    while True:
        date = input("Please enter date read: ")
        if re.match(r'^[0-9!@#$%^&*()-_+=?/]+$', date):
           return date

        else:
            print("Invalid input. Please enter special characters and numbers only.")

def main():
    input_value = get_special_numeric_input()
    print("You entered:", input_value)

if __name__ == "__main__":
    main()
    
    
    import re

def get_alphabetic_input():
    while True:
        value = input("Please enter the title of the book:")
        if re.match(r'^[a-zA-Z ]+$', value):
            return value
        else:
            print("Invalid input. Please enter alphabetic characters only.")

def main():
    input_value = get_alphabetic_input()
    print("You entered:", input_value)

if __name__ == "__main__":
    main()
