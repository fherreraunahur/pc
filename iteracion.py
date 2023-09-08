# Calcular la suma de 10 numeros, utilizando la misma variables para leer los numeros desde la terminal.

vueltas=1#variable que controla el bucle
suma=0
print("Se van a sumar 10 numeros ")
while vueltas <= 10 :
    num=int(input("Ingrese un numero: "))
    suma=suma+num
    vueltas=vueltas+1#actualiza
print(f"La suma de los 10 numeros es {suma}")