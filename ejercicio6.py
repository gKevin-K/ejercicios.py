def Numero (Inter:int) :
    if not type (Inter) == int :
        print ("The Inter Not Is int")
        return
Inter = int(input("Enter a number: "))
Square_Dict = {i: i * i for i in range(1, Inter + 1)}
print(range,f"----< {Inter} >----")
print(Square_Dict)