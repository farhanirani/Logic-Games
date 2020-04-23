import pygame, sys, random
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("particle-explosion")
screen = pygame.display.set_mode((1000, 800),0,32)

particles = []

#main game

while True:
    screen.fill((0,0,0))
    
    mx, my = pygame.mouse.get_pos()
    #                  spawn x,y                   speed x, speed y               life timer and radius                        
    
    for _ in range(30):
        # particles.append([ [mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4,8)])
        particles.append([ [mx, my], [random.randint(-10, 10) , random.randint(-10, 10)], random.randint(4,8), ((random.randint(1,255),0,0))])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        
        # gravity
        # particle[1][1] += 0.1
        
        pygame.draw.circle(screen, particle[3], [ int(particle[0][0]), int(particle[0][1]) ], int(particle[2]))

    for particle in particles:
        if particle[2] <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key ==K_ESCAPE:
                pygame.quit()
                sys.exit()


    pygame.display.update()
    mainClock.tick(60)
