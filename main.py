"""
Módulo principal del juego de combate RPG.
Configura los personajes, inicia el combate y gestiona el flujo principal del juego.
"""

import time

import personaje
from personaje import Personaje
from logica import determinar_ganador, determinar_mas_veloz, bucle_acciones


def main():
    """
    Función principal que ejecuta el juego de combate RPG.
    
    Proceso:
        1. Crea los personajes con sus estadísticas
        2. Muestra mensaje de inicio del combate
        3. Ejecuta rondas de combate hasta que alguien muera
        4. Anuncia al ganador
    """
    # Creación de los personajes con sus estadísticas específicas

    # Thor: Alto poder de ataque y defensa, pero baja velocidad
    thor = Personaje(
        nombre="Thor",
        salud=180,
        fuerza=50,
        defensa=40,
        velocidad=40,
        suerte=15,
        agilidad=20,
        es_jugador=False
    )
    
    # Spiderman: Menos fuerza pero muy rápido y ágil
    spiderman = Personaje(
        nombre="Spiderman",
        salud=130,
        fuerza=40,
        defensa=50,
        velocidad=80,
        suerte=20,
        agilidad=30,
        es_jugador=False
    )
    
    # Lista de luchadores para facilitar el manejo
    luchadores = [thor, spiderman]
    
    # Asignar los combatientes
    p1 = luchadores[0]
    p2 = luchadores[1]

    print("🔔 ¡QUE COMIENCE EL DUELO LEGENDARIO! 🔔")
    print("=" * 50)
    print(f"⚔️ {p1.nombre} VS {p2.nombre}")
    print("=" * 50)

    # Determinamos el orden una sola vez
    primero, segundo = determinar_mas_veloz(p1, p2)

    # Metemos a los luchadores en una lista según su turno
    orden_de_turno = [primero, segundo]

    puntero = 0

    # Bucle principal del combate
    # Continúa mientras ambos personajes estén vivos
    while p1.salud > 0 and p2.salud > 0:

        residuo = puntero % 2
        personaje = orden_de_turno[residuo]
        objetivo = orden_de_turno[1 - residuo]

        # Ejecutamos su bucle de acciones
        bucle_acciones(personaje, objetivo)

        if not objetivo.esta_vivo():
            break

        time.sleep(0.5)

        print("-" * 30)

        puntero += 1

    
    # Determinar y anunciar al ganador
    if p1.salud > 0:
        determinar_ganador(p1)
    else:
        determinar_ganador(p2)


# Punto de entrada del programa
if __name__ == "__main__":
    main()