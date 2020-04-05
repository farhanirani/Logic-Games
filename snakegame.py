import pygame
pygame.init()

pygame.display.set_mode((500,500))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()



run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()