import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 10 # настройка кадров в секунду
fpsClock = pygame.time.Clock()

# настройка окна
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLUE=(0,0,255)
catImg = pygame.image.load('dvd.png')
catx = 10
caty = 10
direction = 'right'
direction="d"
while True: # основной цикл игры
   DISPLAYSURF.fill(BLUE)
   if direction == "d":
      catx+=15
      caty+=10
   
   DISPLAYSURF.blit(catImg, (catx, caty))

   for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

   pygame.display.update()
   fpsClock.tick(FPS)
