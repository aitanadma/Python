#Realizar un programa que retorne el número de elementos comunes iniciales de dos listas

#contador

#Subprograma

def contar_elementos (lista1,lista2):
    numeros_comunes=0
    for i in lista1:
        if i in lista2: 
                numeros_comunes += 1
    return numeros_comunes


#Programa Principal

lista1 = []
lista2 = []

i=0
while i == 0:
    valor_lista1=float(input("Escribe los valores que deseas introducir en la primera lista: "))
    lista1.append(valor_lista1)
    seguir=str(input("Pulsa x si no quieres añadir mas numeros, sino pulsa enter: "))
    if seguir == 'x':
        i=i+1
print(lista1)

i=0
while i == 0:
    valor_lista2=float(input("Escribe los valores que deseas introducir en la segunda lista: "))
    lista2.append(valor_lista2)
    seguir=str(input("Pulsa x si no quieres añadir mas numeros, sino pulsa enter: "))
    if seguir == 'x':
        i=i+1
print(lista2)

print('El numero de veces que se repiten elementos iguales de ambas listas son', contar_elementos(lista1,lista2))