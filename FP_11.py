list = ["A", "B", "b", "c", "E", "E", "f"]
print (f"Lista original: {list}")

erase = input("Ingresa el elemento que desea eliminar de la lista: ")

for _ in list:
    if erase.lower () in list:
        list.remove(erase.lower())
    elif erase.upper () in list:
        list.remove(erase.upper())

print(f"La lista quedó así sin el elemento eliminado: {list}")