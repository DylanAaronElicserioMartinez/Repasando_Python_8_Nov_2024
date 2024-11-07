# Repasando_Python_8_Nov_2024
Actividad en clase

#Codigo 1

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco 

print("Hola Buenas Para Poder Acceder En Este Lugar Tendra Que Ser Mayor De Edad")#Imprime en la pantalla el texto que esta dentro de las ""

N=int(input("Ingresa tu edad:"))#Le damos a (N) el valor que ingresamos

Edad = N #le damos el valor de (N) a la variable (Edad)

if Edad >= 18:#Si el numero ingresado es mayor o igual a 18 pasara todo lo que esta en la variable (if)

    print("Acceso Consedido Eres Mayor De Edad")
    
    print("Bienvenido Porfavor Entra")
    
elif Edad < 18:#Si el numero ingresado es menor que 18 pasara todo lo que esta en la variable (elif)

    print("No Eres Mayor De Edad Entonces No Puedes Entrar")
    
    print("Adios y No Vuelvas Hasta Que Seas Mayor De Edad")
    
else:#Si lo que introdusiste no se puede usar en ninguna de las anteriores pasara lo que esta en esta variable (else)

    print("Lo que acabas de agregar no es valido")

![image](https://github.com/user-attachments/assets/f0eb4d46-319f-4cf7-aa0d-836fda5c8d96)

![image](https://github.com/user-attachments/assets/8124c7de-b6f1-40f2-9f00-ee032e34357a)

#Codigo 2

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

Nota=int(input("Ingresa tu nota:"))#ingresamos el valor de la variable (Nota)

if 0<=Nota<5:#Si el valor de la variable (Nota) es igual o mayor a 0 pero menor a 5 saldra este mensaje

    print("Suspenso")
    
elif 5<=Nota<6:#Si el valor de la variable (Nota) es igual o mayor a 5 pero menor a 6 saldra este mensaje

    print("Suficiente")
    
elif 6<=Nota<7:#Si el valor de la variable (Nota) es igual o mayor a 6 pero menor a 7 saldra este mensaje

    print("Bien")
    
elif 7<=Nota<9:#Si el valor de la variable (Nota) es igual o mayor a 8 pero menor a 9 saldra este mensaje

    print("Notable")
    
elif 9<=Nota<10:#Si el valor de la variable (Nota) es igual o mayor a 9 pero menor a 10 saldra este mensaje

    print("Sobresaliente")
    
else:#En cualquier otro caso, imprimir el texto: NOTA NO VÁLIDA.

    print("Nota no valida")

![image](https://github.com/user-attachments/assets/10846801-fcf4-4e65-8224-d47d11d7b874)

![image](https://github.com/user-attachments/assets/71be2f80-7542-4359-93c9-94108a63f4d6)

#Codigo 3

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

N=input("Ingresa tu nombre con la primera letra en mayusculas porfa:")#Le damos un valor a el valor (N)

A=input("Ingresa tu apellido con la primera letra en mayusculas porfa:")#Le damos un valor a el valor (A)

n="Daniel"#Le damos el valor de "Daniel" a (n)

a="Ramos"#Le damos el valor de "Ramos" a (a)

if N == n:#Comprobamos que el valor de (N) y el valor de (n) son iguales

    print("El nombre ingresado esta correcto")#si son iguales se imprimira este texto
    
elif N != n:#Comprobamos que el valor de (N) y el valor de (n) son iguales

    print("El nombre ingresado esta incorrecto")#si no son iguales se imprimira este texto
    
if A == a:#Comprobamos que el valor de (A) y el valor de (a) son iguales

    print("El apellido ingresado esta correcto")#si son iguales se imprimira este texto
    
elif A != a:#Comprobamos que el valor de (A) y el valor de (a) son iguales

    print("El apellido ingresado esta incorrecto")#si no son iguales se imprimira este texto

![image](https://github.com/user-attachments/assets/cbd3e9a8-4782-4934-804a-30fcc991cb02)

![image](https://github.com/user-attachments/assets/371d85a7-dc82-4101-bcbc-2be7dda24996)

#Codigo 4

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

notas = [7, 3, 9, 5, 6]# le damos el valor de una lista a la variable (notas)

nota_baja = min(notas)#comprobamos cual e el numero mas bajo de la lista

nota_alta = max(notas)#comprobamos cual e el numero mas alto de la lista

print(f"Nota mas baja: {nota_baja}")#imprimimos en la pantalla el numero mas bajo

print(f"Nota mas alta: {nota_alta}")#imprimimos en la pantalla el numero mas alto

![image](https://github.com/user-attachments/assets/ad94aefe-98e5-4be7-ad8b-0ef291353b3d)

![image](https://github.com/user-attachments/assets/5607d4d3-7295-4f9c-8b6a-ffbf46ae9ac6)

#Codigo 5

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

frutas = ["Manzana", "Banana", "Cereza", "Naranja"]#Creamos una lista de frutas llamada (frutas)

if "Cereza" in frutas:#si Cereza esta en la lista que imprima este texto

    print("Cereza si esta en la lista")
    
else:#si no esta que imprima este otro

    print("Cereza no estqa en la lista")

![image](https://github.com/user-attachments/assets/b7c3f0ab-2419-4dcf-b92d-2ebc18785e7a)

![image](https://github.com/user-attachments/assets/6c0e5675-637a-4031-88ea-ed766f21f037)

#Codigo 6

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Definimos una lista con nombre y dos apellidos

nombre_apellidos = ["Juan", "Pérez", "González"]

# Usamos índices para acceder a los apellidos e imprimirlos

print("Apellido 1:", nombre_apellidos[1])  # Imprimimos el primer apellido

print("Apellido 2:", nombre_apellidos[2])  # Imprimimos el segundo apellido

![image](https://github.com/user-attachments/assets/4a36005d-619e-495e-9043-b46518868828)

![image](https://github.com/user-attachments/assets/e711bd24-de14-4cfa-a3ff-61af0e99253e)

#Codigo 7

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Usamos la función sum() para sumar los números pares en el rango de 2 a 100 (inclusive)

suma = sum(range(2, 101, 2))  # El tercer parámetro (2) indica que solo tomamos números pares

print("La suma de los números pares es:", suma)  # Imprimimos el resultado

![image](https://github.com/user-attachments/assets/00f4fa9f-528d-4699-8dcd-85ff7829e6e0)

![image](https://github.com/user-attachments/assets/6a3b9eea-11c9-41cc-8dca-04fe97ac8ad2)

#Codigo 8

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Definimos un número para calcular su tabla de multiplicar

numero = 5  # Ejemplo de número

# Usamos un bucle for para imprimir la tabla de multiplicar del número

for i in range(1, 11):  # Vamos desde el 1 hasta el 10 (inclusive)

    print(f"{numero} x {i} = {numero * i}")  # Imprimimos cada multiplicación

![image](https://github.com/user-attachments/assets/98be1df3-a692-4b88-b66e-08dc3133f5cd)

![image](https://github.com/user-attachments/assets/29bb242e-d0e0-427b-a25b-0230fe927fda)


#Codigo 9

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Definimos una lista de frutas

mi_lista = ["manzana", "plátano", "cereza", "naranja"]#los integrantes de listra

# Usamos un bucle for para recorrer cada elemento de la lista

for item in mi_lista:

    print(item)  # Imprimimos cada elemento de la lista

![image](https://github.com/user-attachments/assets/db270c5d-5d06-4c65-afd7-e381700c545f)

![image](https://github.com/user-attachments/assets/56ba3de3-19cd-4048-90b3-56d32d4dbfe2)

#Codigo 10

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco}

# Definimos una lista de frutas

mi_lista = ["manzana", "plátano", "cereza", "naranja"]

# Usamos un bucle while para recorrer la lista

i = 0  # Inicializamos el índice

while i < len(mi_lista):  # Mientras el índice sea menor que la longitud de la lista

    print(mi_lista[i])  # Imprimimos el elemento correspondiente al índice
    
    i += 1  # Incrementamos el índice

![image](https://github.com/user-attachments/assets/ee9381c3-ecaa-4395-8618-039dd6081231)

![image](https://github.com/user-attachments/assets/1976756e-1722-44e6-8132-0d551946b557)

#Codigo 11

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Definimos una cadena de texto

texto = "Hola"

# Usamos un bucle for para recorrer cada carácter de la cadena

for caracter in texto:

    print(caracter)  # Imprimimos cada carácter por separado

![image](https://github.com/user-attachments/assets/fbe26879-2521-4625-9dd0-b9cbe74bc996)

![image](https://github.com/user-attachments/assets/0fc4bb50-ec23-4f32-8b72-7a962c11a9c3)

#Codigo 12

print(" ")#Imprime en la pantalla un espacio en blanco

print("Dyan Aaron Elicserio Martínez 3°W #Control:1179")#Imprime en l pantaqlla mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#Imprime en la pantalla un espacio en blanco

# Imprimir la parte superior del triángulo

for i in range(1, 6):  # Empezamos desde 1 hasta 5

    print('*' * i)  # Imprimimos i asteriscos en cada línea

# Imprimir la parte inferior del triángulo

for i in range(4, 0, -1):  # Empezamos desde 4 hasta 1

    print('*' * i)  # Imprimimos i asteriscos en cada línea


![image](https://github.com/user-attachments/assets/52f594bf-17cf-4709-8a73-0ce523f4494a)


![image](https://github.com/user-attachments/assets/2d710f26-865f-45e0-8050-c22fd87df0fe)

