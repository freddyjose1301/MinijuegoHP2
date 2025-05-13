🧙‍♂️ Descripción del programa:

Este programa es un minijuego de combate por turnos ambientado en el universo de *Harry Potter*. El jugador elige un personaje entre varios magos disponibles, cada uno con atributos de vida, ataque y defensa, y se enfrenta a un enemigo aleatorio extraído de una lista de villanos.

🧩 Funcionamiento del juego:

En cada turno, el jugador puede:

  * Lanzar un hechizo de ataque Bombarda.
  * Usar un hechizo de protección Expectro Patronum.
  * Usar un poder especial (solo disponible después de 5 ataques exitosos).

El enemigo (villano) decide su acción de forma aleatoria entre atacar o defenderse.

⚔️ Mecánica de combate:

* El daño se calcula en función del ataque del atacante y la defensa del oponente.
* Al usar defensa, el daño recibido se reduce a la mitad o se anula según el nivel de defensa.
* El **poder especial** inflige el doble de daño, pero solo está disponible para personajes jugables y se recarga tras cada uso.

💡 Estructura del código:

Se utiliza programación orientada a objetos:

  * Una clase base `Personaje` con los métodos comunes: `atacar()` y `defender()`.
  * Una subclase `Jugador` que hereda de `Personaje` e incluye el uso del poder especial.
  * Subclases específicas para cada personaje y villano.
El código también implementa **validaciones de entrada** para evitar errores si el jugador escribe mal o deja una opción en blanco.

🎯 Objetivo:

Vencer al enemigo agotando su vida mágica antes de que él agote la tuya.

