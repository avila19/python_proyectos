organizacion = "Taller Avila"
#print("Pinta tu automovil en "+organizacion)
#print("Repara tu automovil en {}".format(organizacion))
#print(f"Edereza y pinta tu automovil en {organizacion}") #f-string

adj = input("ingrese el adjetivo: ")
verbo1 = input("ingrese el verbo1: ")
verbo2 = input("ingrese el verbo2: ")
sust_plural = input("ingrese el sustantivo plurarl: ")

parrafo = f"Reparar y enderezar tu {adj}! Siempre sera un honor y placer porque nos {verbo1} complacer.!{verbo2} " \
          f"nuevos retos en {organizacion} es nuestra mision {sust_plural}!"
print(parrafo)