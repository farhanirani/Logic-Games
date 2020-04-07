import pygame,os
os.chdir("chainreactionfiles")
pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Chain Reaction")
clock = pygame.time.Clock()




# main game


while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
            
