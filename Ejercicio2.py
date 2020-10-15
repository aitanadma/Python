#Realizar un programa que guarde los elementos en común que tienen dos listas.

#Subprograma

def elemento_igual (lista1,lista2):
    elementosiguales=[]
    for i in lista1:
        if i in lista2: 
                elementosiguales.append(i)
    return elementosiguales


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

print('Los elementos iguales de ambas listas son', elemento_igual(lista1,lista2))