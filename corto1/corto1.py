#carnet 201701042
#ultimos 3 digitos: 042

# #se define la función que calcula el siguiente numero de la seucencia
def calculo_N(num):
    lista=[num]
    while num!=1:  
        if num%2==0:
            num=num/2
        else:
            num=(3*num)+1
        lista.append(int(num))
    return lista

def agregar_texto(lista, archivo="collatz.txt"):
    documento=open(archivo, "a")
    documento.write(lista+"\n")
    documento.close()

documento=open("collatz.txt", "w")
documento.write("")
documento.close()
#se pone 42+1 porque range genera 42 numeros incluyendo el 2
#por lo que termina en 41

for i in range(2,(42+1)):
    secuencia=str(calculo_N(i))
    agregar_texto(secuencia)
    print(secuencia)
    