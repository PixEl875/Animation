import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 50 # настройка кадров в секунду
fpsClock = pygame.time.Clock()

# настройка окна
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLUE=(0,0,255)
catImg = pygame.image.load('cat.png')
catImg2 = pygame.image.load('cat.png')
image_width = catImg.get_width()
image_height = catImg.get_height()
catx =10
caty = 10
catx2 =300
caty2 = 10
direction = 'right'
direction2 = 'left'
k=4

while True: # основной цикл игры
   DISPLAYSURF.fill(BLUE)
   if catx<15 and caty<15:
      catImg = pygame.transform.flip(catImg, True, False)
      k+=1
   if direction == 'right':
      catx += k
      if catx >= 400-image_width:
         direction = 'down'
   elif direction == 'down':
      caty += k
      if caty >= 300-image_height:
         direction = 'left'
   elif direction == 'left':
       catx -= k
       
       if catx == 10:
         direction = 'up'
   elif direction == 'up':
       caty -= k
       if caty == 10:
         direction = 'right'
   
   
   if direction2 == 'right':
      catx2 += k
      if catx2 >= 400-image_width:
         direction2 = 'up'
   elif direction2 == 'down':
      caty2 += k
      if caty2 >= 300-image_height:
         direction2 = 'right'
   elif direction2 == 'left':
       catx2 -= k
       if catx2 <= 10:
         direction2 = 'down'
   elif direction2 == 'up':
       caty2 -= k
       if caty2 <= 10:
         direction2 = 'left'
        
   DISPLAYSURF.blit(catImg, (catx, caty))
   DISPLAYSURF.blit(catImg2, (catx2, caty2))
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
      elif event.type == KEYDOWN:
         if event.key == K_SPACE:
                # Мгновенно перемещаем кота в центр экрана
            catx = (400 - image_width) // 2
            caty = (300 - image_height) // 2
      elif event.type == MOUSEBUTTONDOWN:
        catx, caty = event.pos
        catx -= image_width // 2
        caty -= image_height // 2
   

   pygame.display.update()
   fpsClock.tick(FPS)
