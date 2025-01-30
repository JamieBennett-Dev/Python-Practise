# take user input and print if the number is even or odd

user_input = input("choose any number, even or odd: ")
number = int(user_input)

if number % 2 == 0:
    print(f"your number, {number}, is even!")
else:
    print(f"your number, {number}, is odd!")