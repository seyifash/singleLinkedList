def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", " if i != n else "\n")
        elif i % 3 == 0:
            print("Fizz", end=", " if i != n else "\n")
        elif i % 5 == 0:
            print("Buzz", end=", " if i != n else "\n")
        else:
            print(i, end=", " if i != n else "\n")

# Example call with n = 15
fizzBuzz(15)
