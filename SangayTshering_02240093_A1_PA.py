def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

def length_converter(value, unit):
    if unit == 'M':
        return round(value * 3.28084, 2)
    elif unit == 'F':
        return round(value / 3.28084, 2)
    else:
        return None
    
def consonant_counter(text):
    consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    count = 0
    for letter in text:
        if letter in consonants:
            count += 1
    return count

def min_max_finder(numbers):
    if len(numbers) == 0:
        return None, None
    smallest = largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

def is_palindrome(text):
    cleanedtext = text.replace(" ", "").lower()
    return cleanedtext == cleanedtext[::-1]

import requests

def word_counter(filepath):
    response = requests.get(filepath)
    text = response.text.lower()
    wlist = ["the", "was", "and"]
    word = {word:text.count(word)for word in wlist}
    return word 

def menu_display():
    print("\nSelect an option from 1 to 6")
    print("1. Prime Number sum calculator")
    print("2. Length unit Converter")
    print("3. Consonant Counter")
    print("4. Maximum or Minimum Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter from a text file")
    print("0. Exit")

def main():
    while True:
        menu_display()
        try:
            input1 = int(input("Select a Function (1-6) and 0 to Exit:"))

            if input1 == 1:
                start = int(input("Enter the start of your Range: "))
                end = int(input("Enter the end of your Range: "))
                result = prime_sum(start, end)
                print(f"Sum of the Prime Numbers from {start} to {end} is {result}.")

            elif input1 == 2:
                value = float(input("Enter the length value You want to Convert: "))
                unit = input("Enter M to convert meters to feet and F for Feet to Meters): ").upper()
                result = length_converter(value, unit)
                if result is None:
                    print("Invalid directions! Please enter 'M' or 'F'.")
                else:
                    print(f"Coverted value is {result}")
                
            elif input1 == 3:
                text = str(input("Enter your Text: "))
                result = consonant_counter(text)
                print(f"The Number of Consonants in your Text is {result}.")

            elif input1 == 4:
                numbers = []
                total_numbers = int(input("How many Numbers do you want to enter? "))
                for _ in range(total_numbers):
                    number = float(input("Enter a Number: "))
                    numbers.append(number)
                smallest, largest = min_max_finder(numbers)
                if smallest is None or largest is None:
                    print("No numbers Entered.")
                else:
                    print(f"Smallest: {smallest}, Largest: {largest}")

            elif input1 == 5:
                text = input("Enter a text for Palindrome Check: ")
                result = is_palindrome(text)
                print(f"Is the text a palindrome? {result}")

            elif input1 == 6:
                filepath = input("Enter the Path of text file: ")
                result = word_counter(filepath)
                if result is None:
                    print("Upps, File not found, please check the file path.")
                else:
                    print(f"Word count in your Text File: {result}")
                
            elif input1 == 0:
                print("You have Exited the program, Thank You.")
                break

            else:
                print("Invalid Choise! Please select a number between 0 to 6. ")

        except ValueError:
            print("Invalid Input! Please enter a valid number from 1 to 6.")

if __name__ == "__main__":
    main()

