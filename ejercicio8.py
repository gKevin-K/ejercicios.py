def factorial (n:int) :
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number:"))
Result = factorial(number)
print(Result)