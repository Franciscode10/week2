# this program detects which kind of number the user introduces (+, -, 0)
number = int(input("Write a number: "))

if number > 0 :
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Number is 0")