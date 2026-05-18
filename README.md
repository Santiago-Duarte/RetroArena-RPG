# RetroArena RPG ⚔️

Un motor de combate por turnos desarrollado en Python bajo el paradigma de Programación Orientada a Objetos (POO). El proyecto simula batallas estratégicas en consola entre diferentes héroes utilizando mecánicas matemáticas precisas para evadir, mitigar daño, defenderse y contraatacar.

## 🚀 Características Principales

* **Arquitectura de Turno Único:** Flujo de control optimizado mediante un bucle principal basado en operaciones de residuo matemático (`puntero % 2`), garantizando que la salud de los combatientes y los estados temporales se evalúen al instante.
* **Mecánicas Avanzadas de Combate:** Implementación de golpes críticos dinámicos basados en la suerte, cálculos de evasión mediante agilidad y mitigación de daño influenciada por estadísticas de defensa.
* **Acciones Estratégicas:** Los personajes pueden elegir entre atacar, defenderse (activando un escudo que mitiga o absorbe el impacto entrante), usar pociones de curación limitadas o preparar un contraataque letal.
* **Separación de Responsabilidades:** Arquitectura limpia que separa la lógica de datos de los personajes (`personaje.py`), las reglas del juego (`logica.py`), la interfaz de usuario en consola (`combateUI.py`) y el punto de entrada del programa (`main.py`).

## 🛠️ Estructura del Proyecto

* **`main.py`**: El punto de entrada del juego. Configura los personajes, inicializa sus estadísticas de balance y orquesta el bucle de juego principal.
* **`personaje.py`**: Contiene la clase `Personaje`, la cual gestiona el ciclo de vida de los luchadores, sus estadísticas dinámicas (salud, pociones, escudos) y los métodos matemáticos para calcular daño y curación.
* **`logica.py`**: Módulo encargado de controlar las reglas del juego, gestionar las decisiones de los jugadores/IA y aplicar el orden de turnos inicial basado en velocidad.
* **`combateUI.py`**: Módulo estático dedicado exclusivamente a manejar el formateo y la salida visual de los eventos del combate en la terminal.

## 🎮 Cómo Ejecutar

1. Asegúrate de tener instalado Python 3.x en tu sistema.
2. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)# RetroArena-RPG
