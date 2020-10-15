# Programa que sume dos listas de diferente longitud y retorne otra lista que contenga la suma de 
# las originales elemento a elemento más los elementos sobrantes de la lista más larga.


######En este ejercicio entiendo que los valores de la lista ya vienen dados. 

#Subprograma

def sumatorio (lista1,lista2):

   
    for i in range(len(lista2)):
        resultado.append(lista2[i])
    for i in range(len(lista1)):
        resultado[i] = resultado[i] + lista1[i]

    return resultado


#Programa Principal

lista1 = [1, 2, 3, 4, 5]
print('Los valores de la primera lista son: ', lista1)
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Los valores de la primera lista son: ', lista2)

resultado=[]


print('La suma de ambas listas es', sumatorio(lista1,lista2))

