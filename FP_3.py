print ("Bienvenid@")
print ("------------------------------------------------------------------------------------------------------")

contador = 0
while (contador<=2):
    num = int (input("Ingrese un número entero: \n"))
    if (contador==0):
        mayor = num
    elif (num>mayor):
     mayor = num

    contador = contador+1
    
print ("El número", mayor, "es el más grande de los tres")
