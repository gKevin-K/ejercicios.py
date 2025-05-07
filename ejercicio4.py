#Definir la función
#maxTres : (int, int, int) -> int
#tal que maxTres(x, y, z) es el máximo de x, y y z.

def Maxtree(x:int, y:int, z:int) :
        if x == y and  y == z :
            return True
        else:
            return False
Maximo = max(15,54,32)
print("The Number Max is:",max(15,54,32))