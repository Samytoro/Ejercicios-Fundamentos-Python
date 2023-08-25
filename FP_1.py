
print ("Bienvenido al Sistema de Vacaciones")
print ("A continuación podra conocer su tiempo de vacaciones")
print ("------------------------------------------------------------------------------------------------------")
Consulta=0
while (Consulta==0):
      nombre= str(input("Digite su nombre: \n"))
      clave = int (input("Ingrese la clave de su departamento: \n"))

      if clave==1:
       tiempo = int (input("Ingrese cuantos años lleva laborando en la empresa: \n"))
       if (tiempo==1):
        print(nombre + " tiene 6 días de vacaciones")
       elif (tiempo>=2)and (tiempo<=6):
        print(nombre + " tiene 14 días de vacaciones")
       elif (tiempo>=7):
        print(nombre + " tiene 20 días de vacaciones")
      if clave==2:
       tiempo = int (input("Ingrese cuantos años lleva laborando en la empresana: \n"))
       if (tiempo==1):
        print(nombre + " tiene 7 días de vacaciones")
       elif (tiempo>=2)and (tiempo<=6):
        print(nombre + " tiene 15 días de vacaciones")
       elif (tiempo>=7):
        print(nombre + " tiene 22 días de vacaciones")
      if clave==3:
       tiempo = int (input("Ingrese cuantos años lleva laborando en la empresa: \n"))
       if (tiempo==1):
        print(nombre + " tiene 10 días de vacaciones")
       elif (tiempo>=2)and (tiempo<=6):
        print(nombre + " tiene 20 días de vacaciones")
       elif (tiempo>=7):
        print(nombre + " tiene 30 días de vacaciones")
      if clave not in [1 , 2 ,3]:
        print("La clave que digitó es incorrecta")
      Consulta=int(input("Para repetir este proceso puede ingresar 0, si desea terminar ingrese 1 \n"))
      if Consulta==1:
         print ("Gracias por usar la aplicación")


