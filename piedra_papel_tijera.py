import  random
def jugar():
    usuario = input('Bienvenido al juego de piedra, papel o tijera \n'
         'Por Favor selecionen Piedra, Papel o Tijera \n').lower()
    computadora = random.choice(['piedra','papel','tijera']) #escoge un elemento aleatorio de una lista
    
    if usuario == computadora:
        return "Empate!"
    if gano_el_jugador(usuario,computadora):
        return "Ganaste!"
    return "Perdiste!"


def gano_el_jugador(usuario,oponente):
    #return True(verdadero) si gana el jugador.
    # Piedra gana Tijera
    # Tijera gana Papel
    # Papel gana piedra

    if ((usuario == 'piedra' and oponente == 'tijera')
        or(usuario == 'tijera' and oponente == 'papel')
        or(usuario == 'papel' and oponente == 'piedra')):
        return True
    else:   
        return False


print(jugar())