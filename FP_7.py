string = input("Digite una frase a continuación: ")
string_reversed = ""

for character in string:
    string_reversed = character + string_reversed

print(f"Frase invertida: {string_reversed}")