import os
import sys
import pygame
from pygame.locals import *

class Juego:
    def __init__(self):
        pygame.init() # Inicializar Pygame
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)

        self.altura, self.ancho = 640, 640
        self.screen = pygame.display.set_mode((self.altura,self.ancho)) # Inicializar la superficie
        
        rb = pygame.image.load(os.path.join('pieces', 'RB.png')).convert_alpha()
        rw = pygame.image.load(os.path.join('pieces', 'RW.png')).convert_alpha()
        pb = pygame.image.load(os.path.join('pieces', 'PB.png')).convert_alpha()
        pw = pygame.image.load(os.path.join('pieces', 'PW.png')).convert_alpha()
        kb = pygame.image.load(os.path.join('pieces', 'KB.png')).convert_alpha()
        kw = pygame.image.load(os.path.join('pieces', 'KW.png')).convert_alpha()
        knb = pygame.image.load(os.path.join('pieces', 'KnB.png')).convert_alpha()
        knw = pygame.image.load(os.path.join('pieces', 'KnW.png')).convert_alpha()
        bb = pygame.image.load(os.path.join('pieces', 'BB.png')).convert_alpha()
        bw = pygame.image.load(os.path.join('pieces', 'BW.png')).convert_alpha()
        qb = pygame.image.load(os.path.join('pieces', 'QB.png')).convert_alpha()
        qw = pygame.image.load(os.path.join('pieces', 'QW.png')).convert_alpha()

        self.estado = [
            [rb,knb,bb,qb,kb,bb,knb,rb,],
            [pb,pb,pb,pb,pb,pb,pb,pb,pb,],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            [None,None,None,None,None,None,None,None,],
            [pw,pw,pw,pw,pw,pw,pw,pw,pw,],
            [rw,knw,bw,qw,kw,bw,knw,rw,],
        ]

        self.de = None
        self.a = None
        
        self.loop()

    def dibujarTablero(self): # Dibujar el tablero
        color1, color2 = (235,236,208), (119,149,86) # Inicializar los colores
        pygame.display.set_caption("Ajedrez")

        for y in range(8):
            for x in range(8):
                if ((x+y)%2) == 0:
                    pygame.draw.rect(self.screen, color1, pygame.Rect(x*self.ancho//8, y*self.altura//8, 80, 80))
                else:
                    pygame.draw.rect(self.screen, color2, pygame.Rect(x*self.ancho//8, y*self.altura//8, 80, 80))
                
                if self.de:
                    x2,y2 = self.de
                    x2,y2 = x2//80, y2//80
                    pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(x2*self.ancho//8, y2*self.altura//8, 80, 80),4)

                pieza = self.estado[y][x]
                if pieza:
                    self.screen.blit(pieza, (((x*80)+10), ((y*80)+10)))

        pygame.display.flip()

    def moverPieza(self,de,a):
        deX, deY = de
        aX, aY = a
        deX, deY, aX, aY = deX//80, deY//80, aX//80, aY//80

        if deX == aX and deY == aY:
            self.de = None
            self.a = None
            return
        
        pieza = self.estado[deY][deX]
        self.estado[deY][deX] = None
        self.estado[aY][aX] = pieza
        self.de = None
        self.a = None

        self.estado = self.estado[::-1]
        
    def loop(self):
        while True: # el bucle principal del juego
            self.dibujarTablero()
            
            for event in pygame.event.get(): # Posibles entradas del teclado y mouse
                if event.type == pygame.MOUSEBUTTONUP:
                    if not self.de:
                        self.de = pygame.mouse.get_pos()
                    else:
                        self.a = pygame.mouse.get_pos()
                        self.moverPieza(self.de,self.a)

                if event.type == pygame.QUIT:
                    sys.exit()

def main():
    Juego()

if __name__ == "__main__":
    main()
