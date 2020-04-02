import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

run = True
while run:
    screen.fill((20,0,0))
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()