nombre1 = input("¿Como se llamara el jugador 1?: ")
nombre2 = input("¿Como se llamara el jugador 2?: ")


Jugador1 = nombre1 input("¡Hola jugador1 ¿Que eliges? ¿Piedra, Papel o Tijera?: ")
Jugador2 = input("¡Hola jugador2 ¿Que eliges? ¿Piedra, Papel o Tijera?: ")

Condicion1 = Jugador1 == "piedra" and Jugador2 == "tijeras"
Condicion2 = Jugador1 == "papel" and Jugador2 == "piedra"
Condicion3 = Jugador1 == "tijera" and Jugador2 == "papel"

if Jugador1 == Jugador2:
    print("¡Ha sido un empate!")
elif Condicion1 or Condicion2 or Condicion3:
    print("¡Ha ganado:", nombre1)
else:
    print("¡Ha Ganado:", nombre2)

