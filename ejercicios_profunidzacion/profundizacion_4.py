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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas\n')
# Empezar aquí la resolución del ejercicio
print ('Ingrese tres palabras a su eleccion\n')

pal_1 = (input('Ingrese primer palabra:\n'))
pal_2 = (input('Ingrese segunda palabra:\n'))
pal_3 = (input('Ingrese tercer palabra:\n'))

print("""¿Como quiere ordenar las palabras?\n
    1 - Ordenar por orden alfabético.
    2 - Ordenar por cantidad de letras.\n""")

orden = int(input('Esperando su respuesta: '))

if orden == 1: #Alfabeticamente
    if (pal_1 > pal_2) and (pal_1 > pal_3):
        if (pal_2 > pal_3) and (pal_1 > pal_3):
            print(f'{pal_3}\n{pal_2}\n{pal_1}')
        else:
            print(f'{pal_2}\n{pal_3}\n{pal_1}')


            if pal_1 > pal_3:
                print(f'{pal_3}\n{pal_2}\n{pal_1}')

                print(f'{pal_2}\n{pal_3}\n{pal_1}')
         if pal_2 > pal_3:     
             print(f'{pal_2}\n{pal_3}\n{pal_1}')
         else:
             print(f'{pal_2}\n{pal_3}\n{pal_1}')
    elif pal_2 > pal_3:# and pal_3:
        if pal_1 > pal_3:
            print(f'{pal_3}\n{pal_1}\n{pal_2}')
        else:
            print(f'{pal_1}\n{pal_3}\n{pal_2}')
    elif pal_3 > pal_1 and pal_2:
        if pal_1 > pal_2: 
            print(f'{pal_2}\n{pal_1}\n{pal_3}')
        else:
            print(f'{pal_1}\n{pal_2}\n{pal_3}')




