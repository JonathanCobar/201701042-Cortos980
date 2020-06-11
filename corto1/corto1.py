#carnet 201701042
#ultimos 3 digitos: 042

# #se define la función que calcula el siguiente numero de la seucencia
def calculo_N(num):
    lista=[num]#se añade el numero inicial en la primera posición de la lista
    #se crea el ciclo que genera el siguiente numero siempre y cuando no se llegue a 1
    while num!=1:  
        if num%2==0:
            num=num/2
        else:
            num=(3*num)+1
        lista.append(int(num))#añade el número generado a la lista
    return lista#devuelve la secuencia
#crea la función para agregar texto, el archivo por defecto es collatz.txt
#a menos que se indique lo contrario, y el parametro que siempre se debe de dar
#es lo que se va a añadir al texto
def agregar_texto(lista, archivo="collatz.txt"):
    documento=open(archivo, "a")#se usa a para que no reescriba todo y se quede con una linea
    documento.write(lista+"\n")#se escribe un enter para que esté ordenado
    documento.close()
#se limpia el documento para que no se acumulen todas las ejecuciones
documento=open("collatz.txt", "w")
documento.write("")
documento.close()
#se pone 42+1 porque range genera 42 numeros incluyendo el 2
#por lo que termina en 41
for i in range(2,(42+1)):
    secuencia=str(calculo_N(i))
    agregar_texto(secuencia)
    print(secuencia)
    
#Funcionamiento:        40/40
#Uso de Funciones       20/20
#Manejo de archivos     10/10
#Manejo de Listas       10/10
#Uso de git             20/20
#*****************************
#Total                  100/100

