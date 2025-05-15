def factorial (NumberFactorial:int) :
    if not type(NumberFactorial) == int:
        print("The NumberFactorial Not Is int")
    if NumberFactorial == 0 or NumberFactorial == 1 :
        return 1
    else:
        return NumberFactorial * factorial(NumberFactorial - 1)
Number = int(input("Enter a Number:"))
Result = factorial(Number)
print(Result)