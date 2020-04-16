import pygame, sys, os, random
os.chdir("files/dinosaur")
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("dinosaur runner")
screen = pygame.display.set_mode((830, 500),0,32)

bottomimg = pygame.image.load("bottom.png")

# logoIMG = pygame.image.load("logoIMG.png")
# pygame.display.set_icon(logoIMG)

#main game

particles = []
ShootTimer = 0

while True:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    # blast
    if ShootTimer > 0:
        ShootTimer += 1
        if ShootTimer > 10:
            ShootTimer = 0

    if event.type == pygame.MOUSEBUTTONDOWN and ShootTimer == 0:
        ShootTimer = 1
        mx, my = pygame.mouse.get_pos()                    
        
        
        particles.append([ [mx-15, my-3], [8 , 0], 8, 2])
        for _ in range(15):
            particles.append([ [mx, my], [random.randint(6,8) , random.randint(6, 10) / 10 ], random.randint(6,10), 1])
        for _ in range(15):
            particles.append([ [mx, my], [random.randint(6,8) , -1 * random.randint(6, 10) / 10 ], random.randint(6,10), 1])
        

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        if particle[3] == 1:
            pygame.draw.circle(screen, (186, 186, random.randint(186,240)), [ int(particle[0][0]), int(particle[0][1]) ], int(particle[2]))
        else:
            pygame.draw.rect(screen, (186, 186, 240), [ int(particle[0][0]), int(particle[0][1]), 35, 4 ], 4 )

    for particle in particles:
        if particle[2] <= 0:
            particles.remove(particle)



    screen.blit(bottomimg,(0,250))
    pygame.display.update()
    mainClock.tick(60)