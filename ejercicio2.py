resultados = []
for num in range (2000,3201) :
            if num % 7 == 0 and num %5 != 0:
             resultados.append(str(num))
print(",".join(resultados))
