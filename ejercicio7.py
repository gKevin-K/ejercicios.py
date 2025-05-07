entrada = "hello world and practice makes perfect and hello world again"
palabras = entrada.split(" ")
print(palabras)
contador = 0
for palabra in palabras:
    print(f"***{palabra}***")
    for validador in palabras :
        #print(f"   --{validador}--")
        if palabra == validador:
            contador +=1 
            if palabra <=0:
                print(f"***{palabra}***{contador}")
            #print("  son iguales")
        #else:
            #print("  no son iguales")
    contador = 0

