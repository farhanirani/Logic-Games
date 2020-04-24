import pygame, sys, os, random
os.chdir("files/dinosaurfiles")
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("dino")
logoIMG = pygame.image.load("logoIMG.jpg")
pygame.display.set_icon(logoIMG)
#pygame.mixer.music.load("walk.mp3")
#pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1000, 600),0,32)
bottomimg = pygame.image.load("bottom.png")

cactusIMG = pygame.image.load("cactus.jpg").convert()
cactusIMG.set_colorkey((255,255,255))

groundx = 500
groundx2 = 500

class cactus:
    def __init__(self):
        self.scalelen = random.randint(30, 90)
        self.IMG = pygame.transform.scale(cactusIMG,( int(self.scalelen / 2), self.scalelen))
        if random.randint(1,2) == 1:
            pass
        else:
            self.IMG = pygame.transform.flip(self.IMG, True, False)
        self.num = random.randint(1,3)
        self.x = 970
    
    def draw(self):
        global movementSpeed
        for i in range(self.num):
            screen.blit(self.IMG, ( int(self.x + (i* self.IMG.get_size()[0] )) , int(310 - self.IMG.get_size()[1]) ) )
        # pygame.draw.rect(screen, (255,0,0), (self.x+20, 310-self.IMG.get_size()[1], self.num*self.IMG.get_size()[0], self.IMG.get_size()[1] ), 1)
        self.x -= movementSpeed
        


def drawTimer():
    global ShootTimer
    if ShootTimer > 0:
        ShootTimer -= 1
    
    tempLength = 60 / ShootTime * ( ShootTime - ShootTimer )
    pygame.draw.rect(screen, (83, 83, 83), (75,330,60,10))
    pygame.draw.rect(screen, (97, 169, 244), (75,330, int(tempLength),10))


def gameover():
    global score
    global groundx
    global groundx2
    global movementSpeed
    
    screen.fill((255,255,255))
    pygame.draw.line(screen, (83, 83, 83), (groundx, 250+60), (groundx2,250+60), 1)

    for gp in groundparticles:
        pygame.draw.rect(screen, (83, 83, 83), (gp[0], gp[1], gp[2], gp[3]) )

    for cac in cactusobjects:
        cac.draw()

    screen.blit(bottomimg,(0,350))
    drawTimer()

    text = font.render("Shoot-O-meter", 1, (97, 169, 244))
    screen.blit(text, (55,345))
    text = font.render("Right Arrow to shoot, Keep Ducking to load the Shoot-O-meter", 1, (97, 169, 244))
    screen.blit(text, (80,425))
    text = font.render("SCORE : "+str(score), 1, (0,0,0))
    screen.blit(text, (800,10))

    gameoverIMG = pygame.image.load("gameover.jpg")
    restartIMG = pygame.image.load("restart.jpg")
    screen.blit(gameoverIMG, (280, 50))
    screen.blit(restartIMG, (440, 100))
    
    screen.blit(images[4], (int(xdino), int(ydino)))
    pygame.display.update()
    run = True
    i=0
    while i < 200:
        pygame.time.delay(10)
        i+=1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    run = False
                    # to reset all
                    groundparticles.clear()
                    cactusobjects.clear()
                    blastparticles.clear()
                    particles.clear()
                    groundx = 500
                    groundx2 = 500
                    movementSpeed = 8
                    score = 0


def redraw():
    screen.blit(bottomimg,(0,350))
    drawTimer()
    text = font.render(str(score), 1, (0,0,0))
    screen.blit(text, (900,10))
    pygame.display.update()


def startGame():
    global isJump
    screen.fill((255,255,255))
    screen.blit(images[1], (int(xdino), int(ydino)))
    drawTimer()
    screen.blit(bottomimg,(0,350))

    text = font.render("Shoot-O-meter", 1, (97, 169, 244))
    screen.blit(text, (55,345))
    text = font.render("Right Arrow to shoot, Keep Ducking to load the Shoot-O-meter", 1, (97, 169, 244))
    screen.blit(text, (80,425))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            #exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == K_SPACE:
                    isJump = True
                    return

#main game
duckimages = []
for i in range(1,3):
    picture = pygame.image.load("duck_"+str(i)+".png").convert()
    picture.set_colorkey((255,255,255))
    picture = pygame.transform.scale(picture,(86,70))
    duckimages.append(picture)
images = []
for i in range(1,6):
    picture = pygame.image.load("image_part_00"+str(i)+".jpg").convert()
    picture.set_colorkey((255,255,255))
    picture = pygame.transform.scale(picture,(64,68))
    images.append(picture)

particles = []
groundparticles = []
blastparticles = []
cactusobjects = []

cactustimer = 0
groundparticlestimer = 0
ShootTimer = 0
ShootTime = 200
isJump = False
isDuck = False
JumpTimer = 20

score = 0
font = pygame.font.SysFont('comicsans', 30)

xdino = 80
ydino = 250
ydinotemp = 250

movementCount = 0
movementSpeed = 8
neg = 0
veryTempVar = 4
cactusDecreaseInterval = 0

startGame()
while True:
    score += int(movementSpeed)
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

        #duck
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if ShootTimer > 20:
                ShootTimer -= 20
            isDuck = True
        else:
            isDuck = False

        #jump
        if event.type == pygame.KEYDOWN and not isJump:
            if event.key == K_SPACE or event.key == K_UP:
                isJump = True
                isDuck = False
                movementCount = 0

        # blast
        if event.type == pygame.KEYDOWN and ShootTimer == 0:
            if event.key == K_RIGHT:
                movementSpeed += 0.5
                ShootTimer = ShootTime                   
                particles.append([ [50+xdino-16, 35+ydino-3], [8 , 0], 16, 2])
                for _ in range(15):
                    particles.append([ [50+xdino, 35+ydino], [random.randint(6,8) , random.randint(6, 10) / 10 ], random.randint(6,8), 1])
                for _ in range(15):
                    particles.append([ [50+xdino, 35+ydino], [random.randint(6,8) , -1 * random.randint(6, 10) / 10 ], random.randint(6,8), 1])

    #-------------------end of key pressed
    # draw ground
    if groundx > xdino - 50:
        groundx -= 10
    if groundx2 < 970:
        groundx2 += 10
    pygame.draw.line(screen, (83, 83, 83), (groundx, 250+60), (groundx2,250+60), 1)

    if groundparticlestimer == 0:
        groundparticles.append( [ 967 , random.randint(315,330) , random.randint(1,8) , random.randint(1,2) ])
        groundparticlestimer = random.randint(0,6)
    else:
        groundparticlestimer -= 1

    for gp in groundparticles:
        pygame.draw.rect(screen, (83, 83, 83), (gp[0], gp[1], gp[2], gp[3]) )
        gp[0] -= movementSpeed
    
    for gp in groundparticles:
        if gp[0] < 0:
            groundparticles.remove(gp)
    

    #jump
    if isJump:
        if JumpTimer >= -20:
            if neg != -6:
                neg = 1
                if JumpTimer < 0:
                    neg = -1
                    if isDuck:
                        neg = -6
            if ydino - (JumpTimer ** 2) * 0.05 * neg < ydinotemp:
                ydino -= (JumpTimer ** 2) * 0.05 * neg
            else:
                ydino = ydinotemp * 1
                isJump = False
                JumpTimer = 20
                neg = 1
            
            JumpTimer -= 1
        else:
            isJump = False
            JumpTimer = 20
            neg = 1

        screen.blit(images[0], (int(xdino), int(ydino)))
        # pygame.draw.rect(screen, (255,0,0), (xdino+4,ydino+4,50,50), 1)

    #duck    
    elif isDuck:
        movementCount += 1
        if movementCount % 20 < 10:
            screen.blit(duckimages[1], (int(xdino), int(ydino)))
        else:
            screen.blit(duckimages[0], (int(xdino), int(ydino)))

        # pygame.draw.rect(screen, (255,0,0), (xdino+4,ydino+30,80,20), 1)

    # else move right obviously
    else: 
        movementCount += 1
        # animation
        if movementCount % 20 < 10:
            screen.blit(images[2], (int(xdino), int(ydino)))
        else:
            screen.blit(images[3], (int(xdino), int(ydino)))

        # pygame.draw.rect(screen, (255,255,0), (xdino+4,ydino+4,50,50), 1)


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



    #cactus
    if cactustimer == 0:
        cactusobjects.append( cactus() )
        cactustimer = random.randint(30,200-cactusDecreaseInterval)
        if veryTempVar == 0:
            if 140 - cactusDecreaseInterval > 40:
                cactusDecreaseInterval += 10
            veryTempVar = 4
        else:
            veryTempVar -= 1
            
    else:
        cactustimer -= 1

    for cac in cactusobjects:
        cac.draw()
    for cac in cactusobjects:
        if cac.x < -100:
            cactusobjects.remove(cac)


    # check for collision
    # if isDuck:
    #     for cac in cactusobjects:
    #         if xdino+4+80 < cac.x  or xdino+4 > cac.x + cac.IMG.get_size()[0] or ydino+4+50 < 310-cac.IMG.get_size()[1] :
    #             pass
    #         else:
    #             gameover()
    # else:
    for cac in cactusobjects:
        if xdino+4+50 + movementSpeed < cac.x+20  or xdino+4 > cac.x + cac.num * cac.IMG.get_size()[0] or ydino+4+50 < 320-cac.IMG.get_size()[1] :
            pass
        else:
            gameover()


    # check for blast hit 
    run = 1
    for particle in particles:
        if run == 1:
            if particle[3] == 2:
                for cac in cactusobjects:
                    if particle[0][0] + 40 > cac.x and particle[0][0] + 40 < cac.x+cac.IMG.get_size()[0]+50  and particle[0][1] > 310-cac.IMG.get_size()[1] and run == 1:
                        for i in range(int(cac.num * cac.IMG.get_size()[1]/10)):
                            blastparticles.append([ [cac.x +( cac.IMG.get_size()[0] / 2), 310-cac.IMG.get_size()[1] +(cac.IMG.get_size()[1] / 2)], [random.randint(0, 10) , random.randint(0, 20) / 10 - 1], random.randint(4,8)])
                        cactusobjects.remove(cac)
                        particles.remove(particle)
                        run = 0
                    else:
                        break
        else:
            break
    

    # draw cactus explosion
    for blastparticle in blastparticles:
        blastparticle[0][0] += blastparticle[1][0]
        blastparticle[0][1] += blastparticle[1][1]
        blastparticle[2] -= 0.1
        pygame.draw.circle(screen, (83, 83, 83), [ int(blastparticle[0][0]), int(blastparticle[0][1]) ], int(blastparticle[2]))

    for blastparticle in blastparticles:
        if blastparticle[2] <= 0:
            blastparticles.remove(blastparticle)


    redraw()
    mainClock.tick(60)
