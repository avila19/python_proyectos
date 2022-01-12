from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual
import random
import string


def obtener_palabras_validas(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado():

    print('=========================================')
    print('Bienvenido al juego el AHORCADO')
    print('=========================================')
    palabra = obtener_palabras_validas(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas =set()
    abecedario =set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0 :
        print(f"Tiene {vidas} vidas y has usado estas letras :{' '.join(letras_adivinadas)}")
        #estado actual de la palabra
        estado_palabra = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(estado_palabra)}")

        letra_usuario = input("Ingrese una letra ").upper()
        #si la letra elejida por el usuario esta en el abecedario
        #y no esta en el conjunto de letras que se an ingresado
        #se añade la letra al conjunto de letras ingresadas

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vidas = vidas-1
                print(f"\nTu letra {letra_usuario} no esta en la palabra")


        elif letra_usuario in letras_adivinadas:
            print(f"\n Ya se escogiste esta letra. Escoge una nueva")

        else:
            print('\n Esta letra no es valida')

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Perdite la palabra es {palabra}")

    else:
        print(f"Excelente as ADIVINADO LA PALABRA {palabra}")



print(ahorcado())