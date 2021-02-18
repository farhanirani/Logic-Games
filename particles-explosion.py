import pygame, sys, random
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("particle-explosion")
screen = pygame.display.set_mode((1000, 800),0,32)

particles = []
x_vel = 7
y_vel = 7
mx = 130
my = 300

#main game
counter = 0
while True:
    screen.fill((0,0,0))
    
    # 1st method
    mx, my = pygame.mouse.get_pos()

    # 2nd method
    # mx = random.randint(200,600)
    # my = random.randint(200,600)

    # 3rd method
    # if mx < 0 or mx > 1000:
    #     x_vel *= -1 
    # if my < 0 or my > 800:
    #     y_vel *= -1 
    # mx+=x_vel
    # my+=y_vel

    #                  spawn x,y                   speed x, speed y               life timer and radius                        
    for _ in range(20):
        # particles.append([ [mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4,8)])
        particles.append([ [mx, my], [random.randint(-100, 100)/10 , random.randint(-100, 100)/10 ], random.randint(4,10), ((random.randint(100,255)),(random.randint(10,80)),(random.randint(1,13))) ])

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
