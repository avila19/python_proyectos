import random
import time


def busqueda_ingenua(lista , tarjet):
    for i in range(len(lista)):
        if lista[i] == tarjet:
            return i
    return -1



def busqueda_binaria(lista,tarjet,limt_inferior = None ,limt_superior = None):
    if limt_inferior is None:
        limt_inferior = 0 #inicio de la lista
    if limt_superior is None:
        limt_superior = len(lista)-1 #fin de la lista
    if limt_superior < limt_inferior:
        return -1

    punto_medio = (limt_superior + limt_inferior) // 2

    if lista[punto_medio] == tarjet:
        return punto_medio
    elif tarjet < lista[punto_medio]:
        return busqueda_binaria(lista,tarjet,limt_inferior,punto_medio-1)
    else:
        return busqueda_binaria(lista,tarjet,punto_medio+1,limt_superior)



if __name__ == '__main__':

   # mi_lista = [1,3,5,10,12]
   #llenado de una lista
   tamaño = 10000
   conjunto_inicial = set()
   while len(conjunto_inicial) < tamaño:
       n=0
       conjunto_inicial.add(random.randint(n+1,tamaño))
       n=n+1

   lista_ordenada = sorted(list(conjunto_inicial))

   #calculo de tiempo de busqueda
   def timpo_busqueda_ingenua():
       inicio = time.time()
       for tarjet in lista_ordenada:
           busqueda_ingenua(lista_ordenada, tarjet)

       fin = time.time()
       print(f"Tiempo de busqueda ingenua es: {fin - inicio} segundos")

   def tiempo_busqueda_binaria(lista_ordenada,tarjet):
       inicio = time.time()
       for tarjet in lista_ordenada:
           busqueda_binaria(lista_ordenada, tarjet)

       fin = time.time()
       print(f"Tiempo de busqueda binaria es: {fin - inicio} segundos")


   print(busqueda_binaria(lista_ordenada,2))
   tiempo_busqueda_binaria(lista_ordenada,2)