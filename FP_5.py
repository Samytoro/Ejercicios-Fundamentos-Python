a = 0
b = 1
aux = None

for i in range(0,18):
        print (a, end=" ")
        aux = a
        a = b
        b = aux + a
   