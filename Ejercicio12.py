num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el sugundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
mayor=num1
if num1>num2:
    if num1>num3:
        mayor=num1
    else:
          mayor=num3
else:
    if num2>num3:
          mayor=num2
    else:
         mayor=num3

print(f"El mayor es {mayor}")

