class CombatUI:
    """Clase estática para manejar la salida de datos del combate."""

    @staticmethod
    def mostrar_ataque(atacante, defensor, danio, tipo, mitigado=False, contraataque=False):
        if tipo == "evadido":
            print(f"⚡ {defensor.nombre} ha evadido el ataque de {atacante.nombre}.")
        elif tipo == "critico":
            print(f"💥 ¡GOLPE CRÍTICO! {atacante.nombre} infligió {danio} a {defensor.nombre}.")
        else:
            print(f"⚔️ {atacante.nombre} infligió {danio} a {defensor.nombre}.")

        if mitigado and tipo != "evadido":
            print(f"🛡️ {defensor.nombre} absorbió parte del impacto.")

        if contraataque:
            print(f"🔄 ¡{defensor.nombre} devolvió el golpe!")

    @staticmethod
    def mostrar_curacion(personaje, cantidad):
        print(f"🧪 {personaje.nombre} usó una poción y recuperó {cantidad} HP.")
        print(f"❤️ Salud actual: {personaje.salud}/{personaje.salud_maxima}")

    @staticmethod
    def mostrar_estado(p1, p2):
        print(f"\n[ {p1.nombre}: {p1.salud} HP ] vs [ {p2.nombre}: {p2.salud} HP ]")