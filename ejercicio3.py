# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False

def equaltree(x:int, y:int, z:int) :
    return x == y == z 
print(equaltree(4,4,4))
print(equaltree(4,3,4))
print(equaltree(4,4,3))