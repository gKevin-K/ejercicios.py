# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False

def EqualTree(x:int, y:int, z:int) :
    if not type(x) == int :
        print("The Value  x Is Not int")
        return
    if not type(y) == int :
        print("The Value y Is Not int")
        return
    if not type(z) == int:
        print("The Value z Is Not int")
        return
    if x == y and y == z :
        return True
    else:
        return False
print(EqualTree(4,4,4))
print(EqualTree(4,3,4))
print(EqualTree(3,3,3))
print(EqualTree(5,6,5))
