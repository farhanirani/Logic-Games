import pygame, sys, os
os.chdir("files/dinosaur")
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("dinosaur runner")
screen = pygame.display.set_mode((830, 500),0,32)

bottomimg = pygame.image.load("bottom.png")

# logoIMG = pygame.image.load("logoIMG.png")
# pygame.display.set_icon(logoIMG)


while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key ==K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(bottomimg,(0,250))
    pygame.display.update()
    mainClock.tick(60)