# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print('Ingrese tres numeros enteros')

num_1 = int(input('Ingrese N° 1:\n'))
num_2 = int(input('Ingrese N° 2:\n'))
num_3 = int(input('Ingrese N° 3:\n'))

resto_1 = num_1 % 2
resto_2 = num_2 % 2
resto_3 = num_3 % 2

#si el numero tiene resto 0 es par sino impar
# si num_1 // 2 = 0
if resto_1 == 0:
    print(f'El numero {num_1} es par')
else:
    print(f'El numero {num_1} es impar')

if resto_2 == 0:
    print(f'El numero {num_2} es par')
else:
    print(f'El numero {num_2} es impar')

if resto_3 == 0:
    print(f'El numero {num_3} es par')
else:
    print(f'El numero {num_3} es impar')



