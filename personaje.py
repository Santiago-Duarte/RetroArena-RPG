"""
Módulo de definición de la clase Personaje para el juego de combate RPG.
Define las características y comportamientos básicos de cada luchador.
"""

from random import randint

class Personaje:
    """
    Clase que representa a un luchador en el juego de combate RPG.
    
    Atributos:
        nombre (str): Nombre del personaje
        salud (int): Puntos de vida actuales
        fuerza (int): Poder de ataque base
        defensa (int): Capacidad de reducir daño recibido
        velocidad (int): Determina quién ataca primero
        suerte (int): Probabilidad de golpe crítico
        agilidad (int): Probabilidad de esquivar ataques
    """
    
    def __init__(self, nombre, salud, fuerza, defensa, velocidad, suerte, agilidad, es_jugador):
        """
        Inicializa un nuevo personaje con sus estadísticas base.
        
        Args:
            nombre (str): Nombre del personaje
            salud (int): Puntos de vida iniciales
            fuerza (int): Poder de ataque base
            defensa (int): Capacidad defensiva
            velocidad (int): Velocidad de combate
            suerte (int): Probabilidad de crítico (0-100)
            agilidad (int): Probabilidad de esquivar (0-100)
        """

        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.suerte = suerte
        self.agilidad = agilidad
        self.salud_maxima = salud
        self.pociones = 3
        self.es_jugador = es_jugador
        self.energia_cargada = 0
        self.escudo_activo = False
        self.contraataque = False

    def atacar(self, enemigo):
        """
        Realiza un ataque contra un enemigo.
        
        El ataque puede ser:
        - Esquivado: basado en la agilidad del defensor
        - Normal: daño base reducido por defensa
        - Crítico: daño duplicado basado en suerte
        
        Args:
            enemigo (Personaje): Personaje que recibirá el ataque
            
        Returns:
            tuple: (daño, tipo_ataque) donde tipo puede ser "evadido", "normal" o "critico"
        """

        # Verificar si el enemigo esquiva el ataque
        if randint(1, 100) <= enemigo.agilidad:
            return 0, "evadido"

        # Calcular daño base considerando la defensa del enemigo
        # La defensa reduce entre 50% y 80% del daño
        porcentaje_defensa = randint(50, 80) / 100
        danio_base = max(0, round(self.fuerza - enemigo.defensa * porcentaje_defensa))

        # Verificar si es un golpe crítico
        tipo_ataque = "normal"
        if randint(1, 100) <= self.suerte:
            danio_base *= 2
            tipo_ataque = "critico"

        return round(danio_base), tipo_ataque

    def recibir_danio(self, cantidad):
        """
        Procesa el daño recibido de un ataque enemigo.
        
        Args:
            cantidad (int): Cantidad de daño a recibir
            enemigo (Personaje): Personaje que infligió el daño
            tipo (str): Tipo de ataque recibido
        """

        danio_a_devolver = 0

        # Primero verificar contraataque si esa es tu mecánica
        if self.contraataque:
            self.contraataque = False  # Se gasta
            # 60% de probabilidad de devolver el doble y absorber el golpe
            if randint(1,100) <= 60:
                danio_a_devolver = cantidad * 2
                cantidad = 0


        # Si no es contraataque, verificar escudo
        # Se genera un numero aleatorio entre 1 y 101 y si esta en el rango
        # de 0 a 80 entonces el escudo absorbio el daño por completo sino ,
        # recibe la mitad del daño
        if cantidad > 0 and self.escudo_activo:
            self.escudo_activo = False #Se consume el escudo

            if randint(1,100) <= 80:
                cantidad = 0
            else:
                cantidad //= 2

        # Guardar salud anterior para calcular pérdida real
        salud_anterior = self.salud
        self.salud = max(0, self.salud - cantidad)
        vida_perdida = salud_anterior - self.salud

        return vida_perdida , danio_a_devolver

    def esta_vivo(self) -> bool:
        """
        Verifica si el personaje sigue con vida.
        
        Returns:
            bool: True si tiene salud > 0, False si está derrotado
        """

        return self.salud > 0

    def curar(self):
        if self.pociones > 0:
            cantidad_curada = round(self.salud_maxima * 0.3)
            self.salud = min(self.salud_maxima , self.salud + cantidad_curada)
            self.pociones -= 1
            return cantidad_curada
        return 0
