import random
def adivina_el_numero(x):

    print("*******************************")
    print("!ADIVINA El NUMERO")
    print("*******************************")

    num_aleatorio = random.randint(0, x)
    num_a_predecir = 0

    while num_a_predecir != num_aleatorio:
        num_a_predecir = int(input(f"Adivina un numero entre 0 y {x}: "))
        if num_a_predecir < num_aleatorio:
            print("Intente otra vez el numero es muy pequeño")
        elif num_a_predecir > num_aleatorio:
            print("Intente otra vez el numero es muy alto")

    print(f"FELICIDADES ADIVINASTE EL NUMERO {num_aleatorio} ")

adivina_el_numero(10)