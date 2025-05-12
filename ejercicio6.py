def n (n:int) :
    if not type (n) == int :
        return
n = int(input("Enter a number: "))
Square_Dict = {i: i * i for i in range(1, n + 1)}
print(Square_Dict)