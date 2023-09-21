string = input("Digite una frase a continuación: ")
word = input("Digite la palabra que desea eliminar de la frase anterior: ")
substring = ""


indice = string.find(word)
substring = string[0: indice] + string [indice + len(word) +1 : ]

print(f"Frase final: {substring}")
