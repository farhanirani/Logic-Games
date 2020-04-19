import pygame, sys, os, random
os.chdir("files/dinosaurfiles")
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("dino")
logoIMG = pygame.image.load("logoIMG.jpg")
pygame.display.set_icon(logoIMG)

screen = pygame.display.set_mode((1000, 600),0,32)
bottomimg = pygame.image.load("bottom.png")


def drawTimer():
    global ShootTimer
    if ShootTimer > 0:
        ShootTimer -= 1
    
    tempLength = 60 / ShootTime * ( ShootTime - ShootTimer )
    pygame.draw.rect(screen, (0,0,0), (15,15,60,10))
    pygame.draw.rect(screen, (97, 169, 244), (15,15, int(tempLength),10))



def redraw():
    global movementCount
    drawTimer()

    

    screen.blit(bottomimg,(0,300))
    pygame.display.update()


def startGame():
    global isJump
    screen.fill((255,255,255))
    screen.blit(images[1], (int(xdino), int(ydino)))
    drawTimer()
    screen.blit(bottomimg,(0,300))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == K_SPACE:
                    isJump = True
                    return

#main game

images = []
for i in range(1,6):
    picture = pygame.image.load("image_part_00"+str(i)+".jpg").convert()
    picture.set_colorkey((255,255,255))
    picture = pygame.transform.scale(picture,(64,68))
    images.append(picture)

particles = []
ShootTimer = 0
ShootTime = 100
isJump = False
JumpTimer = 20

xdino = 80
ydino = 200

movementCount = 0

startGame()
while True:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():

        #exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        #jump
        if event.type == pygame.KEYDOWN and not isJump:
            if event.key == K_SPACE:
                isJump = True
                movementCount = 0

        # blast
        if event.type == pygame.KEYDOWN and ShootTimer == 0:
            if event.key == K_RIGHT:
                ShootTimer = ShootTime                   
                particles.append([ [50+xdino-16, 35+ydino-3], [8 , 0], 16, 2])
                for _ in range(15):
                    particles.append([ [50+xdino, 35+ydino], [random.randint(6,8) , random.randint(6, 10) / 10 ], random.randint(6,8), 1])
                for _ in range(15):
                    particles.append([ [50+xdino, 35+ydino], [random.randint(6,8) , -1 * random.randint(6, 10) / 10 ], random.randint(6,8), 1])

    #-------------------end of key pressed

    #jump
    if isJump:
        if JumpTimer >= -20:
            neg = 1
            if JumpTimer < 0:
                neg = -1
            ydino -= (JumpTimer ** 2) * 0.04 * neg
            JumpTimer -= 1
        else:
            isJump = False
            JumpTimer = 20
        screen.blit(images[0], (int(xdino), int(ydino)))
    else: # else move right obviously
        movementCount += 1
        # animation
        if movementCount % 20 < 10:
            screen.blit(images[2], (int(xdino), int(ydino)))
        else:
            screen.blit(images[3], (int(xdino), int(ydino)))

        # pygame.draw.rect(screen, (255,0,0), (xdino+4,ydino+4,56,60), 1)


    # blast
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        if particle[3] == 1:
            pygame.draw.circle(screen, (86, 150, random.randint(150,255)), [ int(particle[0][0]), int(particle[0][1]) ], int(particle[2]))
        else:
            pygame.draw.rect(screen, (97, 169, 244), [ int(particle[0][0]), int(particle[0][1]), 40, 6 ] )
            # pygame.draw.rect(screen, (255,0,0), [ int(particle[0][0]), int(particle[0][1]), 40, 6 ], 1)

    for particle in particles:
        if particle[2] <= 0:
            particles.remove(particle)



    
    redraw()
    mainClock.tick(60)
