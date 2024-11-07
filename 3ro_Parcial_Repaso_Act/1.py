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