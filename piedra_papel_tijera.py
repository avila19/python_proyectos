import random
def jugar():
    print('Bienvenido al juego PIEDRA PAPEL o TIJERA \n')
    usuario = input(f"Escriba la opcion escoja una opcion\n PIEDRA\n PAPEL\n TIJERA \n").upper()

    maquina = random.choice(['PIEDRA','PAPEL','TIJERA'])

    if usuario == maquina:
        return 'EMPATE'
    elif gana_el_jugador(usuario,maquina):
        return 'GANASTE'
    return 'PERDISTE'



def gana_el_jugador(jugador,oponente):

    if ((jugador == 'PIEDRA' and oponente == 'TIJERA')
            or (jugador == 'TIJERA' and oponente == 'PAPEL')
            or (jugador == 'PAPEL' and oponente == 'PIEDRA')):
        return True
    else:
        return False


print(jugar())