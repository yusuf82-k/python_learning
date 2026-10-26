def check_age(age):
    if age < 0:
        # Manually trigger a ValueError if age is negative
        raise ValueError("Age cannot be negative!")

    print(f"Your age is {age}")


# Usage:
try:
    a=int(input("Enter your age: "))
    check_age(a)
   # check_age(-5)
except ValueError as error:
    print(f"Caught error: {error}")