print ("Bienvenid@")
print ("A continuación podra ingresar una frase de la cual se eliminaran las vocales")
print ("------------------------------------------------------------------------------------------------------")
string = input("Ingrese una frase a continuación: ")
letra = input("Escriba un carácter (letra, número, especial) con el que desee finalizar la acción de eliminar vocales: ") 

for character in string:
    if character.lower() == letra.lower () :
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print (character, end="")