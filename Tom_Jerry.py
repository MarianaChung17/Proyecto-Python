#!/usr/bin/python3
# Proyecto Python
# Juego Tom y Jerry con tematica de PacMan
# Mariana Chung B92250

import pygame
from pygame.locals import *
from random import randint
from pygame import mixer


# Se crea el laberinto del juego mediante una clase.
class Laberinto():

    # Se crea un metodo constructor con las principales variables del juego.
    def __init__(self):
        # Se establecen colores del juego, formato RGB.
        # Color Negro para las letras.
        self.Negro = (0, 0, 0)
        # Color Oro para el Queso.
        self.Queso = (246, 253, 49)
        # Color Gris para Tom (gato).
        self.Gris = (131, 139, 139)
        # Color cafe para Jerry (raton).
        self.cafecito = (204, 102, 0)
        # Color del background del juego.
        self.Lila = (171, 130, 255)
        # Color muebles.
        self.Cafe = (139, 119, 101)
        # Color del piso.
        self.piso = (67, 205, 128)
        # Anchoo de los cuadrados.
        self.ancho = 20
        # Alto de los cuadrados.
        self.alto = 20
        # Contador del puntaje.
        self.puntaje = 0
        # Contador de niveles.
        self.nivel = 1
        # Variable para pasar al nivel_1.
        self.nivel_1 = True
        # Variable para pasar al nivel_2.
        self.nivel_2 = None
        # Variable para pasar al nivel_3.
        self.nivel_3 = None
        # Variable para pasar al nivel_4.
        self.nivel_4 = None
        # Contador de vidas.
        self.vidas = 3
        # Se crea una matriz base.
        self.matriz = []
        # Se crea una matriz para los muebles y paredes.
        self.muebles = []
        # Metodo para rellenar las matrices.
        self.make()
        # Tamano de ventana.
        self.size = [1200, 600]
        # Se le aplica el tamano de ventana.
        self.screen = pygame.display.set_mode(self.size)
        # Se inicia el juego con musica de fondo
        mixer.init()
        # Se carga el archivo de musica en .ogg
        mixer.music.load('tom-and-jerry-ringtone.ogg')
        # Se corre la cancion.
        mixer.music.play()

    # Se crea funcion para crear el tablero de juego (Matricez).
    def make(self):
        #  i = y, j = x, colocar en el plano los muebles.
        # Se puede modificar al gusto.
        #  Crea mueble.
        for i in range(1, 4):
            for j in range(5, 17):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([i, j])
        #  Crea mueble.
        for i in range(3, 5):
            for j in range(1, 20):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        #  Crea mueble.
        for i in range(10, 12):
            for j in range(10, 15):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        #  Crea mueble.
        for i in range(17, 19):
            for j in range(1, 21):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        #  Crea mueble.
        for i in range(26, 28):
            for j in range(0, 13):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([i, j])
        #  Crea mueble.
        for i in range(4, 6):
            for j in range(31, 35):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        #  Crea mueble.
        for i in range(38, 40):
            for j in range(2, 21):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([i, j])
        #  Crea mueble.
        for i in range(29, 31):
            for j in range(18, 30):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([i, j])
        for i in range(5, 7):
            for j in range(24, 30):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([i, j])
        #  Crea mueble.
        for i in range(23, 25):
            for j in range(10, 25):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        #  Crea mueble.
        for i in range(0, 1):
            for j in range(0, 26):
                # Agrega los espacios que ocupa el mueble
                # en la matriz muebles.
                self.muebles.append([j, i])
        # Crea el piso del juego una matriz (30x40)
        # Tambien se puede modificar
        for fila in range(30):
            self.matriz.append([])
            for columna in range(40):
                # Se crea una matriz de 0
                self.matriz[fila].append(0)
        # Se agrega 1 donde haya muebles a la matriz principal.
        for wall in self.muebles:
            # Recorre la matriz muebles y establece un 1.
            # Esto nos sirve para cuando Tom o Jerry, solo
            # puedan moverse entre los 0, y no los 1 del tablero.
            self.matriz[wall[1]][wall[0]] = 1
        return self

    # Se crea un reset del tablero, en caso de perder,
    # avanzar de nivel o reiniciar el juego.
    def reset(self):
        # Se borran las matrices.
        self.matriz = []
        self.muebles = []
        # Se vuelven a llenar las matrices.
        self.make()
        return self

    # Se crea un "titulo_juego" para el juego.
    def titulo_juego(self):
        # Se establece el texto con una fuente y color escogido.
        textotitulo_juego = self.scorefont.render("TOM Y JERRY", 1, self.Negro)
        # Se coloca en la ubicacion de la ventana 950x100 el texto.
        self.screen.blit(textotitulo_juego, (950, 100))
        # Se extrae la imagen.
        imagen_tom = pygame.image.load('tom.png')
        # Se coloca en la ubicacion de la ventana, la imag en 1000x130.
        self.screen.blit(imagen_tom, (960, 130))
        # Se extrae la imagen.
        imagen_jerry = pygame.image.load('jerry.png')
        # Se coloca en la ubicacion de la ventana 1040x130 el texto.
        self.screen.blit(imagen_jerry, (1040, 130))

    # Se crea un "display" para cuando gane.
    def Ganador(self):
        texto_ganador = self.scorefont.render(
            "Has ganado el juego", 1, self.Negro)
        self.screen.blit(texto_ganador, (950, 500))

    # Se crea un "display" para el puntaje de quesos recolectados.
    def puntaje_disp(self):
        # Se establece el texto con una fuente y color esogido.
        texto_puntaje = self.scorefont.render(
            "Quesos: "+(str)(self.puntaje), 1, self.Negro)
        # Se coloca en la ubicacion de la ventana 970x200 el texto.
        self.screen.blit(texto_puntaje, (970, 200))

    # Se crea un "display" para saber en que nivel se esta jugando.
    def nivel_disp(self):
        # Se establece el texto con una fuente y color esogido.
        texto_nivel = self.scorefont.render("Nivel: "+(str)(
            self.nivel), 1, self.Negro)
        # Se coloca en la ubicacion de la ventana 980x300 el texto.
        self.screen.blit(texto_nivel, (980, 300))

    # Se crea un "display" para saber cuantas vidas tiene el jugador.
    def vidas_disp(self):
        # Se establece el texto con una fuente y color esogido.
        # el self.vidas va disminuytendo conforme muere jerry.
        textovidas = self.scorefont.render(
            "Vidas: "+(str)(self.vidas), 1, self.Negro)
        # Se coloca en la ubicacion de la ventana 980x400 el texto.
        self.screen.blit(textovidas, (980, 400))

    # Se crea un "display" para dibujar el tablero.
    def laberinto_disp(self):
        # Se dibuja la matriz fila por columna (30x40).
        for fila in range(30):
            for columna in range(40):
                # La funcion .draw dibuja, la rect() dibuja rectangulos y
                # requiere entrada de una superficie, en esta caso el Screen
                # como segunda entrada requiere color, por ultimo requiere
                # posicion y dimensiones.
                pygame.draw.rect(self.screen, self.piso, [(
                    self.ancho)*columna, (self.alto)*fila,
                    self.ancho, self.alto])
                # Si en matriz hay un 0(espacios por los que
                # se pueden mover los jugadores)
                # dibuje en la mitad del cuadrado del laberinto
                # los quesos de Jerry.
                if self.matriz[fila][columna] == 0:
                    # La funcion .draw dibuja, la ellipse(), dibuja elipses
                    # requiere entrada de una superficie, en
                    # esta caso el Screen
                    # como segunda entrada requiere color, por ultimo requiere
                    # posicion (centrados) y dimensiones.
                    pygame.draw.ellipse(self.screen, self.Queso, [
                        (self.ancho)*columna+5, (self.alto)*fila+5,
                        self.ancho-10, self.alto-10])

    # Se crea un "display" para dibujar los muebles.
    def muebles_disp(self):
        # Se dibuja la matriz muebles sobre el laberinto.
        for wall in self.muebles:
            # La funcion .draw dibuja, la rect(), dibuja rectangulos
            # requiere entrada de una superficie, en esta caso el Screen
            # como segunda entrada requiere color, por ultimo requiere
            # posicion y dimensiones.
            pygame.draw.rect(self.screen, self.Cafe, [
                (self.ancho)*wall[0], (self.alto)*wall[1],
                self.ancho, self.alto])

    # Se crea una función para reiniciar el juego cuando
    # se pierde una vida
    def reset_general(self):
        # Ancho de los cuadrados.
        self.ancho = 20
        # Alto de los cuadrados.
        self.alto = 20
        # Contador del puntaje.
        self.puntaje = 0
        # Contador de niveles.
        self.nivel = 1
        # Variable para pasar al nivel_1.
        self.nivel_1 = True
        # Variable para pasar al nivel_2.
        self.nivel_2 = None
        # Variable para pasar al nivel_3.
        self.nivel_3 = None
        # Variable para pasar al nivel_4.
        self.nivel_4 = None
        # Se crea una matriz base.
        self.matriz = []
        # Se crea una matriz para los muebles y paredes.
        self.muebles = []
        # Metodo para rellenar las matrices.
        self.make()
        # Tamano de ventana.
        self.size = [1200, 600]
        # Se le aplica el tamano de ventana.
        self.screen = pygame.display.set_mode(self.size)


# Se implementa una clase que especifique dónde se encuentra
# cada elemento del juego y qué implicaciones tiene
class posicion(Laberinto):
    # Se crea un metodo constructor, donde declaramos las
    # posiciones x y y en el tablero. Recibe x, y.
    def __init__(self, x, y):
        self.posicion_x = x
        self.posicion_y = y

    def posicion_mueble(self, x, y, W):
        # Si la posicion en la que se va hay un mueble.
        # Retorne True, de lo contrario False.
        if [x, y] in W:
            return True
        else:
            return False

    # Se crea una funcion o metodo para ir hacia la izquierda.
    def izquierda(self, W):
        # Revisa si esta en una posicion x mayor a 0.sino
        # esta al borde izquierdo del tablero.
        if self.posicion_x > 0:
            # LLama la funcion posicion_mueble.
            # Si retorna True no puede moverse.
            if self.posicion_mueble(self.posicion_x-1, self.posicion_y, W):
                self.posicion_x = self.posicion_x
            # Si retorna False puede moverse hacia la izquierda.
            else:
                self.posicion_x = (self.posicion_x)-1
        return self

    # Se crea una funcion o metodo para ir hacia la derecha.
    def derecha(self, W):
        # Revisa si esta en una posicion x menor a 39.sino
        # esta al borde derecho del tablero.
        if self.posicion_x < 39:
            # LLama la funcion posicion_muuebles.
            # Si retorna True no puede moverse.
            if self.posicion_mueble(self.posicion_x + 1, self.posicion_y, W):
                self.posicion_x = self.posicion_x
            # Si retorna False puede moverse hacia la izquierda.
            else:
                self.posicion_x = (self.posicion_x) + 1
        return self

    # Se crea una funcion o metodo para ir hacia arriba.
    def arriba(self, W):
        # Revisa si esta en una posicion y mayor a 0.sino
        # esta al borde arriba del tablero.
        if self.posicion_y > 0:
            # LLama la funcion posicion_muuebles.
            # Si retorna True no puede moverse.
            if self.posicion_mueble(self.posicion_x, self.posicion_y - 1, W):
                self.posicion_y = self.posicion_y
            # Si retorna False puede moverse hacia la izquierda.
            else:
                self.posicion_y = (self.posicion_y) - 1
        return self

    # Se crea una funcion o metodo para ir hacia abajo.
    def abajo(self, W):
        # Revisa si esta en una posicion y menor a 39.sino
        # esta al borde abajo del tablero.
        if self.posicion_y < 29:
            # LLama la funcion posicion_muuebles.
            # Si retorna True no puede moverse.
            if self.posicion_mueble(self.posicion_x, self.posicion_y + 1, W):
                self.posicion_y = self.posicion_y
            # Si retorna False puede moverse hacia la izquierda.
            else:
                self.posicion_y = (self.posicion_y) + 1
            return self


# Se crea la clase para jerry (jugador).
class Jerry(posicion):

    # Se inicia en una posicion establecida al iniciar el juego.
    def __init__(self):
        x = 0
        y = 2
        posicion.__init__(self, x, y)

    # Se inicia en una posicion establecida arbitrariamente
    # al reiniciar el juego.
    def reset_jerry(self):
        x = 0
        y = 2
        posicion.__init__(self, x, y)

    # Funcion para la recoleccion de los quesos.
    def recoleccion_quesos(self, Wa):
        # Si en la matriz esta un 0, habra un queso.
        if Wa.matriz[self.posicion_y][self.posicion_x] == 0:
            return True
        else:
            return False

    # Se define el movimiento de jerry hacia la izquierda para
    # recolectar los quesos.
    def jerry_izq(self, Wa):
        # Se llama a la funcion del movimiento izquierda.
        posicion.izquierda(self, Wa.muebles)
        # Si hay quesos, entonces, quitar el dibujo de queso,
        # aumentar el contador.
        if self.recoleccion_quesos(Wa):
            # Al poner un 1 en la matriz, elimina el dibujo
            # hecho de queso.
            Wa.matriz[self.posicion_y][self.posicion_x] = 1
            # Se aumenta el contador de quesos.
            Wa.puntaje += 1
        return self

    # Se define el movimiento de jerry hacia la derecha para
    # recolectar los quesos.
    def jerry_der(self, Wa):
        # Se llama a la funcion del movimiento derecha.
        posicion.derecha(self, Wa.muebles)
        # Si hay quesos, entonces, quitar el dibujo de queso,
        # aumentar el contador.
        if self.recoleccion_quesos(Wa):
            # Al poner un 1 en la matriz, elimina el dibujo
            # hecho de queso.
            Wa.matriz[self.posicion_y][self.posicion_x] = 1
            # Se aumenta el contador de quesos.
            Wa.puntaje += 1
        return self

    # Se define el movimiento de jerry hacia arriba para
    # recolectar los quesos.
    def jerry_arr(self, Wa):
        # Se llama a la funcion del movimiento arriba.
        posicion.arriba(self, Wa.muebles)
        # Si hay quesos, entonces, quitar el dibujo de queso,
        # aumentar el contador.
        if self.recoleccion_quesos(Wa):
            # Al poner un 1 en la matriz, elimina el dibujo
            # hecho de queso.
            Wa.matriz[self.posicion_y][self.posicion_x] = 1
            # Se aumenta el contador de quesos.
            Wa.puntaje += 1
        return self

    # Se define el movimiento de jerry hacia arriba para
    # recolectar los quesos.
    def jerry_abj(self, Wa):
        # Se llama a la funcion del movimiento abajo.
        posicion.abajo(self, Wa.muebles)
        # Si hay quesos, entonces, quitar el dibujo de queso,
        # aumentar el contador.
        if self.recoleccion_quesos(Wa):
            # Al poner un 1 en la matriz, elimina el dibujo
            # hecho de queso.
            Wa.matriz[self.posicion_y][self.posicion_x] = 1
            # Se aumenta el contador de quesos.
            Wa.puntaje += 1
        return self

    # Se crea display para mostrar el movimiento de jerry que cambia,
    # dependiendo de las teclas presionadas y la posicion que senalen.
    def mov_jerry(self, G):
        # La funcion .draw dibuja, la rect(), dibuja rectangulos
        # requiere entrada de una superficie, en esta caso el Screen
        # como segunda entrada requiere color, por ultimo requiere
        # posicion y dimensiones.
        pygame.draw.rect(G.screen, G.cafecito, [
            (G.ancho)*self.posicion_x, (G.alto)*self.posicion_y,
            G.ancho, G.alto])

    # Se crea una funcion para revisar si la posicion a la que iba Tom,
    # Se encuentra jerry. Recibe a un tom.
    def muere(self, T):
        # Si se encuentran hacia la misma direccion.
        if [self.posicion_x, self.posicion_y] == [T.posicion_x, T.posicion_y]:
            # Retorne True
            return True
        # De lo contrario devuelva False.
        else:
            return False

    # Se establece la conexion de las teclas arriba, abajo.
    # izquierda y derecha con la funcion del movimiento.
    def jerry_movimiento(self, G):
        # Se llama a la funcion key.get_pressed(),
        # si el boton es apretado, haga:
        keys = pygame.key.get_pressed()
        # Si la flecha de la izquierda es apretada:
        if keys[pygame.K_LEFT]:
            # Llama a la funcion de jerry.izq
            self.jerry_izq(G)
        # Si la flecha de la derecha es apretada:
        elif keys[pygame.K_RIGHT]:
            # Llama a la funcion de jerry.der
            self.jerry_der(G)
        # Si la flecha de arriba es apretada:
        elif keys[pygame.K_UP]:
            # Llama a la funcion de jerry.arr
            self.jerry_arr(G)
        # Si la flecha de abajo es apretada:
        elif keys[pygame.K_DOWN]:
            # Llama a la funcion de jerry.arr
            self.jerry_abj(G)


# Se crea una clase para los Toms.  usando sprite.sprite,
# crea una clase base para los objetos del juego (Tom).
class Tom(posicion, pygame.sprite.Sprite):

    # Se crea un metodo constructor, donde se establece,
    # La posicion del Tom aleatoriamente.
    # Esto es modificable dependiendo de donde se quiere que inicien.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = randint(20, 27)
        y = randint(15, 22)
        posicion.__init__(self, x, y)

    # Se crea un reset de la posicion de los Tom.
    def reset_Tom(self):
        x = randint(20, 27)
        y = randint(15, 22)
        # Se llama a la funcion posicion, que recibe la posicion en x,
        # de tom y la y.
        posicion.__init__(self, x, y)
        return self

    # Al igual que jerry los tom se deben mover, pero sin comandos de un
    # usuario.
    # Se define el movimiento de tom hacia la izquierda.
    def tom_izq(self, Wa):
        # Se llama a la fucnion posicion, para que se muevan en
        # los espacios que no son los muebles
        posicion.izquierda(self, Wa.muebles)
        return self

    # Se define el movimiento de tom hacia la derecha.
    def tom_der(self, Wa):
        # Se llama a la funcion posicion, para que se muevan en
        # los espacios que no son los muebles
        posicion.derecha(self, Wa.muebles)
        return self

    # Se define el movimiento de tom hacia arriba.
    def tom_arr(self, Wa):
        # Se llama a la funcion posicion, para que se muevan en
        # los espacios que no son los muebles
        posicion.arriba(self, Wa.muebles)
        return self

    # Se define el movimiento de tom hacia abajo.
    def tom_abj(self, Wa):
        # Se llama a la funcion posicion, para que se muevan en
        # los espacios que no son los muebles
        posicion.abajo(self, Wa.muebles)
        return self

    # Se crea display para mostrar el movimiento de tom que cambia,
    # aleatoriamente.
    def tom_movimiento(self, G):
        # La funcion .draw dibuja, la rect(), dibuja rectangulos
        # requiere entrada de una superficie, en esta caso el Screen
        # como segunda entrada requiere color, por ultimo requiere
        # posicion y dimensiones.
        # Basicmente va dibujano cada posicion aleatorio que
        # genere el tom_posicion.
        pygame.draw.rect(G.screen, G.Gris, [
            (G.ancho)*self.posicion_x, (G.alto)*self.posicion_y,
            G.ancho, G.alto])

    # Se define una funcion para hacer el movimiento aleatorio de los toms.
    def tom_posicion(self, G):
        # Se elige una direccion aleatoria para tom.
        direccion = randint(0, 3)
        # Si es 0, se mueve a la izquierda (si no hay un mueble).
        if direccion == 0:
            self.tom_izq(G)
        # Si es 1, se mueve a la derecha (si no hay un mueble).
        elif direccion == 1:
            self.tom_der(G)
        # Si es 2, se mueve hacia arriba (si no hay un mueble).
        elif direccion == 2:
            self.tom_arr(G)
        # Si es 3, se mueve hacia abajo (si no hay un mueble).
        elif direccion == 3:
            self.tom_abj(G)


if __name__ == "__main__" or __name__ == "Tom_Jerry":

    pygame.init()           # Todos los módulos de pygame se inicializan
    juego = Laberinto()     # Se crea el laberinto
    jerry = Jerry()         # Se crea el jugador
    Tom_1 = Tom()           # Se crea el primer enemigo
    Tom_2 = Tom()           # Se crea el segundo enemigo
    Tom_3 = Tom()           # Se crea el tercer enemigo
    Tom_4 = Tom()           # Se crea el cuarto enemigo
    Tom_5 = Tom()           # Se crea el quinto enemigo
    Tom_6 = Tom()           # Se crea el sexto enemigo
    # Se crea el texto de la puntuación
    juego.scorefont = pygame.font.Font(None, 30)
    salir = False           # El juego se inicia hasta indicar lo contrario
    # Se crea un contador de tiempo para controlar los cuadros que pueden
    # pasar por minuto
    clock = pygame.time.Clock()

    # Este es principal ciclo de implemtnación del juego.
    # En él se establece que mientras no haya una indicación
    # de terminación debe continuar
    while salir is False:
        # Se utilizan los eventos de pygame para definir acciones
        for event in pygame.event.get():
            # Se define la primera condición de salida que
            # es cuando se salga algún evento con atributo
            # None
            if event.type == pygame.QUIT:
                # Si pasa, se sale del juego
                salir = True
            # Si se presiona la tecla de abajo
            elif event.type == KEYDOWN:
                # Si se presiona q se sale del juego
                if event.key == pygame.K_q:
                    salir = True
                # Si se presiona r se reinicia el juego sin salirse
                if event.key == pygame.K_r:
                    juego = Laberinto()
                    jerry = Jerry()
                    Tom_1 = Tom()
                    Tom_2 = Tom()
                    Tom_3 = Tom()
                    Tom_4 = Tom()
                    pygame.init()
                    juego.scorefont = pygame.font.Font(None, 30)
                    salir = False
                    clock = pygame.time.Clock()

        # Se le da al jugador la capacidad de moverse
        jerry.jerry_movimiento(juego)
        juego.screen.fill(juego.Lila)     # Se asigna color lila a la pantalla
        direccion = randint(0, 3)         # Se crea una dirección aleatoria
        juego.laberinto_disp()            # Se muestra el laberinto
        juego.muebles_disp()              # Se muestran los muebles
        jerry.mov_jerry(juego)            # Se muestra el movimiento de Jerry
        # Se define el nivel 1
        if juego.nivel_1 is True:
            # Se inicializan a los enemigos
            Tom_1.tom_posicion(juego)
            Tom_2.tom_posicion(juego)
            Tom_1.tom_movimiento(juego)
            Tom_2.tom_movimiento(juego)
            # Se llama a la función muere para bajar el contador de vidas
            if jerry.muere(Tom_1) or jerry.muere(Tom_2):
                juego.vidas -= 1         # Se resta una vida
                juego.reset_general()    # Se reinicia el juego
                # Se vuelven a crear los elementos del juego nuevamente
                jerry = Jerry()
                Tom_1 = Tom()
                Tom_2 = Tom()
                pygame.init()
                juego.scorefont = pygame.font.Font(None, 30)
                salir = False
                clock = pygame.time.Clock()
                # Si se acaban las vidas se sale del juego
                if juego.vidas == 0:
                    salir = True

        # Se define el nivel 2
        if juego.nivel_2 is True:
            # Se declara que el primer nivel acabó para no repetir
            juego.nivel_1 = False
            # Se le da la habilidad a los enemigos de verse en
            # el juego y moverse
            Tom_1.tom_posicion(juego)
            Tom_1.tom_movimiento(juego)
            Tom_2.tom_posicion(juego)
            Tom_2.tom_movimiento(juego)
            Tom_3.tom_posicion(juego)
            Tom_3.tom_movimiento(juego)
            Tom_4.tom_posicion(juego)
            Tom_4.tom_movimiento(juego)
            # Se define la condición de finalización del juego, que
            # es cuando muere a causa del choque con algún enemigo
            if (jerry.muere(Tom_1) or
                    jerry.muere(Tom_2) or jerry.muere(Tom_3)
                    or jerry.muere(Tom_4)):
                # Se resta una vida y se vuelven a crear los elementos
                # del juego
                juego.vidas -= 1
                juego.reset_general()
                jerry = Jerry()
                Tom_1 = Tom()
                Tom_2 = Tom()
                Tom_3 = Tom()
                Tom_4 = Tom()
                pygame.init()
                juego.scorefont = pygame.font.Font(None, 30)
                salir = False
                clock = pygame.time.Clock()
                # Se sale del juego al perder las vidas
                if juego.vidas == 0:
                    salir = True

        # Se define el nivel 3, que es que el juego funciona
        # sin que Jerry pueda perder
        if juego.nivel_3 is True:
            # Se define el juego normalmente sin restar vidas
            juego.nivel_1 = False
            juego.nivel_2 = False
            Tom_3.tom_movimiento(juego)
            Tom_3.tom_posicion(juego)
            Tom_4.tom_movimiento(juego)
            Tom_4.tom_posicion(juego)
            Tom_5.tom_movimiento(juego)
            Tom_5.tom_posicion(juego)
            Tom_6.tom_movimiento(juego)
            Tom_6.tom_posicion(juego)

        # El último nivel es similar al 1 y 2, pero tiene 6 enemigos
        if juego.nivel_4 is True:
            juego.nivel_1 = False
            juego.nivel_2 = False
            juego.nivel_3 = False
            Tom_1.tom_movimiento(juego)
            Tom_1.tom_posicion(juego)
            Tom_2.tom_movimiento(juego)
            Tom_2.tom_posicion(juego)
            Tom_3.tom_movimiento(juego)
            Tom_3.tom_posicion(juego)
            Tom_4.tom_movimiento(juego)
            Tom_4.tom_posicion(juego)
            Tom_5.tom_movimiento(juego)
            Tom_5.tom_posicion(juego)
            Tom_6.tom_movimiento(juego)
            Tom_6.tom_posicion(juego)
            # Se crea el mismo ciclo utilizado anteriormente que define
            # que el juegofinaliza al chocar con un enemigo
            if (jerry.muere(Tom_1) or jerry.muere(Tom_2) or jerry.muere(Tom_3)
                    or jerry.muere(Tom_4) or jerry.muere(Tom_5)
                    or jerry.muere(Tom_6)):
                juego.vidas -= 1
                juego.reset_general()
                jerry = Jerry()
                Tom_1 = Tom()
                Tom_2 = Tom()
                Tom_3 = Tom()
                Tom_4 = Tom()
                Tom_5 = Tom()
                Tom_6 = Tom()
                pygame.init()
                juego.scorefont = pygame.font.Font(None, 30)
                salir = False
                clock = pygame.time.Clock()
                if juego.vidas == 0:
                    salir = True

        # Se definen las condiciones para pasar de un nivel a otro
        if juego.puntaje == 100:
            Tom_1.reset_Tom()          # Se reinicia el primer enemigo
            Tom_2.reset_Tom()          # Se reinicia el segundo enemigo
            juego.nivel_2 = True       # Condición de inicio de nivel 2
            juego.nivel += 1           # Se le dice al juego que ha subido

        # Si se llega a 200 quesos pasa al nivel 3 (nivel de poder de jugador)
        if juego.puntaje == 200:
            Tom_1.reset_Tom()          # Se reinicia el primer enemigo
            Tom_2.reset_Tom()          # Se reinicia el segundo enemigo
            Tom_3.reset_Tom()          # Se reinicia el tercer enemigo
            Tom_4.reset_Tom()          # Se reinicia el cuarto enemigo
            juego.nivel_3 = True       # Condición de inicio de nivel 2
            juego.nivel += 1           # Se le dice al juego que ha subido

        #Si se llega a 300 quesos se pasa al nivel 4
        if juego. puntaje == 300:
            Tom_1.reset_Tom()          # Se reinicia el primer enemigo
            Tom_2.reset_Tom()          # Se reinicia el segundo enemigo
            Tom_3.reset_Tom()          # Se reinicia el tercer enemigo
            Tom_4.reset_Tom()          # Se reinicia el cuarto enemigo
            juego.nivel_4 = True
            juego.nivel += 1

        # Se define la condición de victoria del jugador
        if juego.puntaje == 918:  # 918 es la puntuación máxima
            juego.Ganador()       # Se imprime que ha ganado el juego
            salir = True
            clock = pygame.time.Clock()

        juego.titulo_juego()      # Se muestra en pantalla el título
        juego.puntaje_disp()      # Se muestra en pantalla el puntaje
        juego.nivel_disp()        # Se muestra en pantalla el nivel
        juego.vidas_disp()        # Se muestra en pantalla las vidas
        # Se usa tick para que pasen 10 cuadros por segundo
        clock.tick(10)

        # Muestra los cambios realizados a la pantalla
        pygame.display.flip()
pygame.quit()
