import random

# Clase base
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, otro):
        daño = max(0, self.ataque - otro.defensa)
        otro.vida -= daño
        return daño

    def defender(self, otro):
        daño = max(0, (otro.ataque // 2) - self.defensa)
        self.vida -= daño
        return daño

# Clase para jugadores con poder especial
class Jugador(Personaje):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)
        self.contador_ataques = 0

    def atacar(self, otro):
        daño = super().atacar(otro)
        self.contador_ataques += 1
        return daño

    def poder_especial(self, otro):
        if self.contador_ataques >= 5:
            daño = max(0, (self.ataque * 2) - otro.defensa)
            otro.vida -= daño
            self.contador_ataques = 0
            return daño
        return None

# Subclases de personajes jugables
class HarryPotter(Jugador): pass
class HermioneGranger(Jugador): pass
class RonWeasley(Jugador): pass

# Subclases de enemigos
class LordVoldemort(Personaje): pass
class BellatrixLestrange(Personaje): pass
class LuciusMalfoy(Personaje): pass

# Diccionarios de personajes
personajes_jugables = [
    HarryPotter("Harry Potter", 100, 22, 12),
    HermioneGranger("Hermione Granger", 90, 25, 10),
    RonWeasley("Ron Weasley", 95, 18, 14)
]

enemigos = [
    LordVoldemort("Lord Voldemort", 110, 27, 8),
    BellatrixLestrange("Bellatrix Lestrange", 95, 26, 10),
    LuciusMalfoy("Lucius Malfoy", 90, 21, 11)
]

acciones = ["hechizar", "proteger"]

# Elegir personaje jugador
print("\n🧙‍♂️ Personajes disponibles:")
for i, p in enumerate(personajes_jugables):
    print(f"{i + 1}. {p.nombre} - ❤️ {p.vida}, 💥 {p.ataque}, 🛡️ {p.defensa}")

while True:
    entrada_personaje = input("\nElige tu mago (1-3): ").strip()
    if entrada_personaje.isdigit():
        opcion = int(entrada_personaje) - 1
        if 0 <= opcion < len(personajes_jugables):
            jugador = personajes_jugables[opcion]
            break
    print("Opción inválida. Intenta de nuevo.")

# Elegir enemigo aleatorio
enemigo = random.choice(enemigos)
print(f"\n🧟‍♂️ Te enfrentarás a: {enemigo.nombre}!")

# Bucle del combate
turno = 1
while jugador.vida > 0 and enemigo.vida > 0:
    print(f"\n--- Turno {turno} ---")
    print(f"👤 {jugador.nombre} ❤️ {jugador.vida} | 🧟‍♂️ {enemigo.nombre} ❤️ {enemigo.vida}")

    # Preguntar al jugador hasta que ingrese una opción válida
    while True:
        print("\n¿Qué harás?")
        print("1. Hechizo de ataque Bombarda 💥")
        print("2. Hechizo de protección Expectro Patronum 🛡️")
        if jugador.contador_ataques >= 5:
            print("3. Poder especial 🔥")

        entrada = input("Elige una acción: ").strip()
        if entrada == "1":
            accion_jugador = "hechizar"
            break
        elif entrada == "2":
            accion_jugador = "proteger"
            break
        elif entrada == "3" and jugador.contador_ataques >= 5:
            accion_jugador = "especial"
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

    accion_enemigo = random.choice(acciones)

    print(f"\n{jugador.nombre} lanza {'hechizo de ataque Bombarda' if accion_jugador == 'hechizar' else ('hechizo de protección Expectro Patronum' if accion_jugador == 'proteger' else 'poder especial 🔥')}!")
    print(f"{enemigo.nombre} lanza {'hechizo de ataque Bombarda' if accion_enemigo == 'hechizar' else 'hechizo de protección Expectro Patronum'}!")

    # Resolución del turno
    if accion_jugador == "hechizar" and accion_enemigo == "hechizar":
        daño1 = jugador.atacar(enemigo)
        daño2 = enemigo.atacar(jugador)
        print(f"⚔️ Ambos atacan: {enemigo.nombre} pierde {daño1}, {jugador.nombre} pierde {daño2}")
    elif accion_jugador == "hechizar" and accion_enemigo == "proteger":
        daño = max(0, (jugador.ataque // 2) - enemigo.defensa)
        if daño > 0:
            enemigo.vida -= daño
            print(f"💥 Tu hechizo daña ligeramente a {enemigo.nombre} por {daño} puntos")
        else:
            print("🛡️ El enemigo bloqueó totalmente tu hechizo")
    elif accion_jugador == "proteger" and accion_enemigo == "hechizar":
        daño = max(0, (enemigo.ataque // 2) - jugador.defensa)
        if daño > 0:
            jugador.vida -= daño
            print(f"💥 {enemigo.nombre} te daña con {daño} puntos")
        else:
            print("🛡️ Lograste bloquear completamente el ataque enemigo")
    elif accion_jugador == "proteger" and accion_enemigo == "proteger":
        print("✨ Ambos conjuraron protecciones. Nada ocurre.")
    elif accion_jugador == "especial":
        if accion_enemigo == "proteger":
            jugador.contador_ataques = 0
            print("🛡️ El enemigo se protegió. Tu poder especial fue bloqueado completamente.")
        else:
            daño = jugador.poder_especial(enemigo)
            print(f"🔥 ¡Poder especial activado! {enemigo.nombre} recibió {daño} de daño.")

    turno += 1

# Resultado final
print("\n⚡ Fin del duelo ⚡")
if jugador.vida <= 0 and enemigo.vida <= 0:
    print("🤯 Ambos cayeron al mismo tiempo. ¡Empate mágico!")
elif jugador.vida <= 0:
    print(f"💀 {enemigo.nombre} ha ganado el duelo.")
else:
    print(f"🏆 ¡{jugador.nombre} ha vencido a {enemigo.nombre}!")