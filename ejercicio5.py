# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista.

def rotacion1(listEnumerate:list):
        if not type(listEnumerate) == list:
            print("listEnumerate not list")
            return
        if len(listEnumerate) <=1 :
            print("List obtenid for listEnumerate")
            return listEnumerate[:]
        else:
            return listEnumerate[1:] + [listEnumerate[0]]
listEnumerate = [10,20,30,40,50,]
listEnumerate2= ["A","B","C","D","E"]

print(rotacion1(listEnumerate))

