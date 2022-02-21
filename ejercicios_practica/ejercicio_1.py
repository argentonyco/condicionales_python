# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
from cgi import print_environ


numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda0

if numero_1 == numero_2:
    print('Los numeros son iguales')            
else:
    if numero_1 > numero_2 :
        print('{} es mayor que {}'.format(numero_1, numero_2))
    else:
        print('{} es mayor que {}'.format(numero_2, numero_1))

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
numero_1 = int(input('Ingrese un número:\n'))

if numero_1 > 0 :
    print('El numero ingresado es POSITIVO')
elif numero_1 < 0: 
    print('El numero ingresado es NEGATIVO')
else:
    print('El numero ingresado es 0') 

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

numero_1 = int(input('Ingrese un numero entre 0 y 100:\n'))

if numero_1 >= 0 and numero_1 <= 100:
    print ('El numero es correcto')
else:
    print ('El numero ingresado no es valido')
# if numero_1 > 0:
#     if numero_1 < 100:
#         print ('El numero ingresado es mayor que 0 y menor que 100')
#     else:
#         print('El numero ingresado es mayor que 0 y mayor que 100')
# elif numero_1 < 100:
#     print('El numero ingresado es menor que 0 y menor que 100')


# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición



