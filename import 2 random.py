import random
import os
import time

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def titulo():

  print("""
 /$$$$$$$   /$$$$$$                  /$$           /$$             /$$       /$$                     /$$                                           /$$      
| $$____/  /$$__  $$                | $$          | $$            | $$      | $$                    | $$                                          | $$      
| $$      |__/  \\ $$        /$$$$$$$| $$ /$$   /$$| $$$$$$$       | $$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$   /$$             /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$$$$$$   /$$$$$$/       /$$_____/| $$| $$  | $$| $$__  $$      | $$__  $$| $$ |____  $$ /$$_____/| $$  /$$/            |__/ |____  $$ /$$_____/| $$  /$$/
|_____  $$ /$$____/       | $$      | $$| $$  | $$| $$  \\ $$      | $$  \\ $$| $$  /$$$$$$$| $$      | $$$$$$/              /$$  /$$$$$$$| $$      | $$$$$$/ 
 /$$  \\ $$| $$            | $$      | $$| $$  | $$| $$  | $$      | $$  | $$| $$ /$$__  $$| $$      | $$_  $$             | $$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$/| $$$$$$$$      |  $$$$$$$| $$|  $$$$$$/| $$$$$$$/      | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$            | $$|  $$$$$$$|  $$$$$$$| $$ \\  $$
 \\______/ |________/       \\_______/|__/ \\______/ |_______/       |_______/ |__/ \\_______/ \\_______/|__/  \\__/            | $$ \\_______/ \\_______/|__/  \\__/
                                                                                                                     /$$  | $$                              
                                                                                                                    |  $$$$$$/                              
                                                                                                                     \\______/                               


def pantalla_inicio():

    limpiar()
    titulo()

    print("🎰 Bienvenido al Casino Pythonico 🎰\n")

    while True:

        op = input("¿Quieres jugar? (si/no): ").lower()

        if op in ["si","s"]:
            return True

        if op in ["no","n"]:
            return False

        print("Respuesta inválida")


def mostrar_creditos(creditos):

    print("══════════════════════════════")
    print("💰 CRÉDITOS DEL CASINO")
    print("══════════════════════════════\n")

    print(f"Jugador      →  ${creditos['jugador']}")
    print(f"Máquina      →  ${creditos['maquina']}")

    print("\n══════════════════════════════\n")


# =============================
# CREAR MAZO
# =============================

def crear_mazo():

    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠','♥','♦','♣']

    mazo = [v+p for v in valores for p in palos]

    random.shuffle(mazo)

    return mazo
def mostrar_cartas(mano):

    ROJO = "\033[91m"
    RESET = "\033[0m"

    lineas = ["", "", "", "", "", "", ""]

    for carta in mano:

        valor = carta[:-1]
        palo = carta[-1]

        color = ROJO if palo in ["♥","♦"] else ""

        dibujo = [
            f"{color}┌─────────┐{RESET}",
            f"{color}│{valor:<2}       │{RESET}",
            f"{color}│         │{RESET}",
            f"{color}│    {palo}    │{RESET}",
            f"{color}│         │{RESET}",
            f"{color}│       {valor:>2}│{RESET}",
            f"{color}└─────────┘{RESET}"
        ]

        for i in range(7):
            lineas[i] += dibujo[i] + "  "

    for linea in lineas:
        print(linea)
def valor_carta(carta):

    v = carta[:-1]

    if v in ["J","Q","K"]:
        return 10

    if v == "A":
        return 11

    return int(v)
def calcular_puntos(mano):

    total = sum(valor_carta(c) for c in mano)

    ases = sum(1 for c in mano if c[:-1] == "A")

    while total > 21 and ases:
        total -= 10
        ases -= 1

    return total
def apuesta_jugador(creditos):

    while True:

        try:

            apuesta = int(input("Tu apuesta (1-10): "))

            if 1 <= apuesta <= 10 and apuesta <= creditos:
                return apuesta

        except:
            pass

        print("Apuesta inválida")
def apuesta_maquina(creditos):

    apuesta = random.randint(1, min(10, creditos))

    print("La máquina apuesta:", apuesta)

    time.sleep(1)

    return apuesta
def turno_jugador(mano, mazo):

    while True:

        limpiar()
        titulo()

        print("══════ TU TURNO ══════\n")

        mostrar_cartas(mano)

        puntos = calcular_puntos(mano)

        print("\nPuntos:", puntos)

        if puntos > 21:
            print("💥 Te pasaste de 21")
            return puntos

        while True:

            print("\n1. Pedir carta")
            print("2. Plantarse")

            op = input("> ")

            if op == "1":

                carta = mazo.pop()

                print("\nRobaste:", carta)

                mano.append(carta)

                time.sleep(1)

                break

            elif op == "2":

                return puntos

            else:

                print("Opción inválida. Escribe 1 o 2.")
def turno_maquina(mano, mazo):

    while True:

        puntos = calcular_puntos(mano)

        if puntos >= 17:
            return puntos

        carta = mazo.pop()

        mano.append(carta)

        print("La máquina roba:", carta)

        time.sleep(1)



def preguntar_continuar():

    while True:

        op = input("\n¿Quieres seguir jugando? (si/no): ").lower()

        if op in ["si","s"]:
            return True

        if op in ["no","n"]:
            return False

        print("Respuesta inválida")
def jugar_ronda(creditos):

    mazo = crear_mazo()

    print("Barajando cartas...")
    time.sleep(2)

    jugador = [mazo.pop(), mazo.pop()]
    maquina = [mazo.pop(), mazo.pop()]

    turno = random.choice(["jugador","maquina"])

    print("Empieza:", turno)
    time.sleep(1)

    apuesta_j = apuesta_jugador(creditos["jugador"])
    apuesta_m = apuesta_maquina(creditos["maquina"])

    apuesta = min(apuesta_j, apuesta_m)

    if turno == "jugador":

        p1 = turno_jugador(jugador, mazo)

        limpiar()
        titulo()

        print("Turno de la máquina\n")

        mostrar_cartas(maquina)

        time.sleep(2)

        p2 = turno_maquina(maquina, mazo)

    else:

        print("Turno de la máquina\n")

        mostrar_cartas(maquina)

        time.sleep(2)

        p2 = turno_maquina(maquina, mazo)

        p1 = turno_jugador(jugador, mazo)

    limpiar()
    titulo()

    print("══════ RESULTADO ══════\n")

    print("Tus puntos:", p1)
    print("Máquina:", p2)

    if p1 > 21:

        creditos["jugador"] -= apuesta
        creditos["maquina"] += apuesta

        print("💻 La máquina gana")

    elif p2 > 21 or p1 > p2:

        creditos["jugador"] += apuesta
        creditos["maquina"] -= apuesta

        print("🏆 Ganaste 🏆")

    elif p2 > p1:

        creditos["jugador"] -= apuesta
        creditos["maquina"] += apuesta

        print("💻 La máquina gana")

    else:

        print("🤝 Empate")

    input("\nPresiona ENTER para continuar...")
def blackjack():

    if not pantalla_inicio():
        print("Hasta luego")
        return

    creditos = {
        "jugador":50,
        "maquina":50
    }

    while creditos["jugador"] < 100 and creditos["maquina"] < 100:

        limpiar()
        titulo()

        mostrar_creditos(creditos)

        jugar_ronda(creditos)

        if not preguntar_continuar():
            print("\n🎰 Gracias por jugar 🎰")
            return

    limpiar()
    titulo()

    if creditos["jugador"] >= 100:
        print("\n🥇 GANASTE 🥇")
    else:
        print("\n💻 LA MÁQUINA GANA 💻")



blackjack()
