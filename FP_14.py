numero_matriz= int(input("¿Cuántas matrices quiere sumar?: "))

if numero_matriz> 1:
    filas= int(input("¿Cuántas filas tendrán las matrices?: "))
    columnas= int(input("¿Cuántas columnas tendrán las matrices?: "))

    matriz_list =[]
    
    for numero in range (numero_matriz):
        matriz =[]
        for fila in range (filas):
            new_fila=[]
            for columna in range (columnas):
                new_fila.append(int(input(f"Introduce un elemento para la matriz {numero + 1} fila {fila}, columna {columna}: ")))
            matriz.append(new_fila)
        matriz_list.append(matriz)

    matriz =[]
    for fila in range (filas):
        new_fila = []
        for columna in range (columnas):
            suma_matriz = 0
            for matriz_position in range (len(matriz_list)):
                suma_matriz += matriz_list[matriz_position][fila][columna]
            new_fila.append (suma_matriz)
        matriz.append(new_fila)
    matriz_list.append(matriz)

    for matriz_fila in range (filas):
        for matriz_list_position in range (len(matriz_list)):
            if matriz_fila != 1:
                print(f"{matriz_list[matriz_list_position][matriz_fila]}", end="  ")
            else:
                if matriz_list_position < len(matriz_list) -2:
                    print(f"{matriz_list[matriz_list_position][matriz_fila]}", end=" +")   
                elif matriz_list_position < len(matriz_list) -1:
                    print(f"{matriz_list[matriz_list_position][matriz_fila]}", end=" =") 
                else:
                    print(f"{matriz_list[matriz_list_position][matriz_fila]}", end="  ")
        print()

else:
    print("Se necesitan al menos dos matrices para realizar la suma.")
    