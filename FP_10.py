nums =[]
long_list = int(input("¿Cúantos números tedrá la lista?: "))

for _ in range (long_list):
    nums.append (int(input("Ingrese el número: ")))

print(f"Lista: {nums} \n La suma de los números es: {sum(nums)}")