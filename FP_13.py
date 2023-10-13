f = int(input("¿Cuántas filas quiere que tenga su matriz?"))
c = int(input("¿Cuántas columnas quiere que tenga su matriz?"))
matri = []

for f_position in range (f):
    f = []
    for element in range (c):
        f.append(int(input(f"Ingrese un elemento en la fila {f_position} : ")))
    matri.append (f)
for f in matri:
    print (f)    