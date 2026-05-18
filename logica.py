"""
Módulo de lógica del juego de combate RPG.
Contiene las funciones principales para gestionar el flujo del combate,
determinar turnos, verificar estado de los personajes y mostrar resultados.
"""

import random

from combateUI import CombatUI as Ui

def bucle_acciones(atacante , defensor):
    atacante.escudo_activo = False
    atacante.contraataque = False
    accion_completada = False
    while not accion_completada:
        opcion = seleccionar_accion(atacante)
        accion_completada = ejecutar_accion(atacante, defensor, opcion)

def seleccionar_accion(personaje) -> str:
    print(f"\nEs el turno de {personaje.nombre}")
    opciones = ["1", "2", "3", "4"]
    if personaje.es_jugador:
        print("1 -> Atacar")
        print("2 -> Curar")
        print("3 -> Defender")
        print("4 -> Contraatacar")
        opcion = input("\nElige una acción: ")

        while opcion not in opciones:
            print("\nPor favor, elige una acción válida.")
            opcion = input("\nElige una acción: ")
    else:
        if personaje.pociones == 0 or personaje.salud > personaje.salud_maxima*0.5:
            opciones.remove("2")
        opcion = random.choice(opciones)
        print(f"El enemigo {personaje.nombre} ha elegido {opcion}")

    return opcion

def ejecutar_accion(personaje_que_actua , objetivo, opcion) -> bool:
    match opcion:
        case "1":
            # Guardamos el estado de defensa y contraataque del OBJETIVO antes de que se resetee
            estaba_defendido = objetivo.escudo_activo
            estaba_contraatacando = objetivo.contraataque

            danio_potencial , tipo_ataque = personaje_que_actua.atacar(objetivo)

            if tipo_ataque == "Evadido":
                Ui.mostrar_ataque(personaje_que_actua, objetivo, 0, "Evadido")
                return True

            # El objetivo procesa el daño y nos dice si devuelve algo
            vida_perdida , danio_devuelto = objetivo.recibir_danio( danio_potencial )

            # Mostramos el resultado del ataque principal

            Ui.mostrar_ataque(
                personaje_que_actua,
                objetivo,
                vida_perdida,
                tipo_ataque,
                mitigado=estaba_defendido and vida_perdida < danio_potencial,
                contraataque=estaba_contraatacando and danio_devuelto > 0
            )

            # Si hubo contraataque efectivo, aplicamos el daño de vuelta al atacante original
            if danio_devuelto > 0:
                # El atacante original recibe el daño directamente (sin escudarse de su propio contraataque)
                salud_anterior = personaje_que_actua.salud
                personaje_que_actua.salud = max(0, personaje_que_actua.salud - danio_devuelto)
                print(f"💥 ¡El contraataque causó {danio_devuelto} de daño a {personaje_que_actua.nombre}!")
            return True
        case "2":
            cantidad_curada = personaje_que_actua.curar()
            if cantidad_curada > 0:
                Ui.mostrar_curacion(personaje_que_actua , cantidad_curada)
                return True
            else:
                print(f"No tienes pociones...")
                return False
        case "3":
            personaje_que_actua.escudo_activo = True
            print(f"{personaje_que_actua.nombre} se ha defendido")
            return True
        case "4":
            personaje_que_actua.contraataque = True
            print(f"🛡️ {personaje_que_actua.nombre} se prepara para devolver el siguiente golpe.")
            return True
    return False

def determinar_mas_veloz(peleador_1, peleador_2) -> tuple:
    """
    Determina qué personaje ataca primero basado en su velocidad.
    Si tienen la misma velocidad, se decide al azar.
    
    Args:
        peleador_1 (Personaje): Primer luchador
        peleador_2 (Personaje): Segundo luchador
        
    Returns:
        tuple: (atacante, defensor) - Quién ataca primero y quién defiende
    """

    # El personaje con mayor velocidad ataca primero
    if peleador_1.velocidad > peleador_2.velocidad:
        return peleador_1, peleador_2
    elif peleador_2.velocidad > peleador_1.velocidad:
        return peleador_2, peleador_1
    
    # Velocidades iguales: se decide aleatoriamente
    lista_peleadores = [peleador_1, peleador_2]
    atacante = random.choice(lista_peleadores)
    lista_peleadores.remove(atacante)
    defensor = lista_peleadores[0]
    
    return atacante, defensor

def determinar_ganador(peleador_ganador):
    """
    Anuncia el ganador del combate.
    
    Args:
        peleador_ganador (Personaje): Personaje que ha ganado el combate
    """

    print(f"\n🏆 ¡EL JUEGO HA FINALIZADO! 🏆")
    print(f"🎊 El ganador ha sido {peleador_ganador.nombre} 🎊")

