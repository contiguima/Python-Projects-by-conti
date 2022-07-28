
print (""" Las funciones disponibles son: 
1) Sumar dos números
2) Restar dos números
3) Multiplicar dos números
4) Dividir dos números
5) Obtener el resto de una división
6) Apagar calculadora
""")

option = int(input("Seleccione su opción: "))
x = float(input("Ingrese un valor: "))
y = float(input ("Ingrese otro valor: "))
suma = x + y
resta = x + -y
multiplicacion = x * y
division = x % y #Devuelve el resto
cociente= x/y #Devuelve el cociente 
if option == 1:
    print (suma)
elif option == 2:
    print (resta)
elif option == 3:
    print (multiplicacion)
elif option == 4:
    print (division)
elif option == 5:
    print (cociente)
elif option == 6:
    print ("Apagado")
else:
    print ("Esa opción no es válida")




