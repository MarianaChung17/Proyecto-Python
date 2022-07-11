# Proyecto-Python

Universidad de Costa Rica

Escuela de Ingenieria Electrica

Curso IE-0117 Programacion Bajo Plataformas Abiertas

I ciclo 2022

Estudiante 1: Julio Castro Fallas

Carne:

Estudiante 2: Mariana Chung Garita

Carne: B92250

Este es el repositoriodel proyecto de python del curso

## Descripcion del juego:

Se trata de un PacMan con tema de Tom y Jerry.

### Consta de 4 niveles:
- Nivel 1: Nivel de inicio, modo facil, 2 enemigos.
- Nivel 2: Modo intermedio, 4 enemigos.
- Nivel 3: Nivel de poder. Enemigos no pueden matar a Jerry.
- Nivel 4: Modo dificil, 8 enemigos.

### Controles
- Tecla R: Reinicia el juego.
- Tecla Q: Se sale del juego, lo termina.
- Tecla de direccion hacia arriba: Mueve a jerry hacia arriba.
- Tecla de direccion hacia abajo: Mueve a jerry hacia abajo.
- Tecla de direccion hacia la derecha: Mueve a jerry hacia la derecha.
- Tecla de direccion hacia la izquierda: Mueve a jerry hacia la izquierda.

### Figuras del juego
Bloque color cafe: Jerry
Bloques color gris: enemigos (Tom)
Circulos color amarillo: Quesos

Indicadores
Puntaje: Cantidad de quesos que jerry se ha comido.
Nivel: Nivel en el que se encuentra el jugador.
Vidas: Numero de vidas restantes.

### Explicacion del juego

El juego comienza con el Nivel 1 establecido, con 3 vidas y un puntaje de 0. 

Cuando jerry alcanza a comer 100 quesos, avanza al nivel 2.

Cuando jerry alcanza 200 quesos pasa al nivel de poder, donde se vuelve invisible a los enemigos, es decir si colisionan los enemigos con jerry no muere.
Este poder dura hasta obtener 300 quesos.

Cuando jerry obtiene los 300 quesos pasa al ultimo nivel, el 4.
#### Notas: 
- Si jerry muere 3 veces el juego se acaba, es decir se cierra.
- Cada vez que jerry muere se reinicia el juego y se devuelve a nivel 1. Con 1 vida menos cada vez que muere.
- Cuando jerry obtiene todos los quesos el juego termina.


## Correr el programa:

Para correr el programa se necesita la instalacion de:
- Pygame
```
sudo apt-get install python-pygam
```
Puede correr el programa desde terminal Ubunto con:
```
python3 Tom_Jerry.py
```
```
./Tom_Jerry.py
```
## Consejos
Para correr el programa asegurse de almacenar en la misma carpeta el Tom_Jerry.py conjunto las imagenes y el sonido.

Asegurese que en terminal se encuentre en el directorio correcto.





