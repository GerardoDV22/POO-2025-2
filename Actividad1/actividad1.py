#Luis Gerardo Dávalos Velásquez

#Ejercicio 1: Número mayor
def numero_mayor(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

#Ejercicio 2: Suma de impares
def suma_impares():
    while True:
        try:
            n = int(input("Ingrese un número entero: "))
            impares = 0
            for i in range(1,n+1,2):
                impares += i
            return impares
        except ValueError:
            input("Solo se permiten numeros")

#Ejercicio 3: Factorial recursivo
def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

#Ejercicio 4: Lista de pares
def lista_pares(lista):
    pares = []
    for numero in lista:
        if numero%2 == 0:
            pares.append(numero)
    return pares

#Ejercicio 5: Validación de contraseña
def validar_pass():
    contraseña = "admin123"
    intentos = 1
    while intentos < 4:
        password = input(f"Ingrese la contraseña (Intento {intentos}): ")
        if password == contraseña:
            return "Acceso autorizado, bienvenido"
        else:
            intentos += 1
    return "Acceso denegado, cuenta bloqueada"


#Ejecuciones de comprobación:
numeros = [1,2,3,4,5,6,7,8,9,10]

#print("El número mayor es: ", numero_mayor(2,5,1))

#print(suma_impares())

#print(factorial(5))

#print(lista_pares(numeros))

#print(validar_pass())