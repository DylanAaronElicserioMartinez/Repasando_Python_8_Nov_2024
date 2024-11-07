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