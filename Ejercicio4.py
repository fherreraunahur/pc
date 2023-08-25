#Escribir un programa que cree dos variables, solicitar se ingresen los números
# de manera arbitraria
#y muestre por pantalla: la suma, la resta, la multiplicación, la división entera y
# el resto de la división entera cada operación por línea.
print("Bienvenidos a este sencillo programa ")
x=int(input("Ingrese el primer numero"))
y=int(input("Ingrese el segundo numero"))
suma=x+y
resta=x-y
producto=x*y
division_e=x//y
resto=x%y
print(f"La suma de {x} + {y} es igual a:  {suma}")
print(f"La resta de {x} - {y} es igual a:  {resta}")
print(f"La producto de {x} * {y} es igual a:  {producto}")