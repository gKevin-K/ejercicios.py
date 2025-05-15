def potencia(Number,Number2):
    if Number2 == 0:
        return 1
    else:
        print(Number, Number2 - 1)
        result =  Number * potencia(Number, Number2 - 1)
        print(f"    {result}")
        return result
def entrada():
    try:
        Number = input("ingrese un numero natural:")
        Number2 = input("ingrese el segundo numero natural: ")
        Number = int(Number)
        Number2 = int(Number2)
        if Number < 0 or Number2 < 0 :
            print("error los numeros deben de ser naturales :  ")
            return
        print(f"el numero entero es {Number}")
        print(f"el segundo numero entero es :{Number2}")
        resultado = potencia (Number,Number2)
        print(f"{Number} elevado a {Number2} es : {resultado}")
        print("la operacion ha sido valida")
    except ValueError:
        print("uno de los valores unidos no es un numero valido")
print(entrada())


