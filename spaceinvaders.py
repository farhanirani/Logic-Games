import pygame,os
os.chdir("spaceinvadersfiles")
pygame.init()

win = pygame.display.set_mode((600,500))
pygame.display.set_caption("Space Invaders")

shooterimg = pygame.image.load("shooter.png")
bulletimg = pygame.image.load("bullet.png")
alienimg = pygame.image.load("alien1.png")
alienimg2 = pygame.image.load("alien2.png")
pygame.display.set_icon(shooterimg)

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("bgsong.wav")
pygame.mixer.music.play(-1)

class spaceship:
    def __init__(self,x,y,vel,initx):
        self.x = x
        self.y = y
        self.vel = vel
        self.initx = initx

    def draw(self):
        win.blit(alienimg, (self.x,self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32),2)


class spaceship2:
    def __init__(self,x,y,vel,initx):
        self.x = x
        self.y = y
        self.vel = vel
        self.initx = initx

    def draw(self):
        win.blit(alienimg2, (self.x,self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32),2)


class shooter:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 6
    
    def draw(self):
        win.blit(shooterimg, (self.x,self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32),2)


class bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 30

    def draw(self):
        win.blit(bulletimg , (self.x,self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x+4,self.y,8,16),2)


def redraw():
    win.fill((9, 27, 61))
    player.draw()
    for a in aliens:
        a.draw()
    for b in bullets:
        b.draw()
        
    pygame.display.update()


def gameover():
    font = pygame.font.SysFont('franklingothicheavy', 60)
    text = font.render('GAME OVER ', 1, (0, 63, 252))
    win.fill((9, 27, 61))
    win.blit(text, (120,210))
    pygame.display.update()
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.quit()


def roundover():
    global alienspeed
    global roundno
    global bullettimertime
    bullettimertime -= 1

    font = pygame.font.SysFont('franklingothicheavy', 60)
    text = font.render('ROUND '+ str(roundno), 1, (0, 63, 252))
    win.fill((9, 27, 61))
    win.blit(text, (180,210))
    pygame.display.update()

    alienspeed += 1
    roundno += 1
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.quit()
            
    for i in range(8):
        aliens.append( spaceship2(500/8*(i+1)+5, 40, alienspeed, 500/8*(i+1)+5) )
        aliens.append( spaceship(500/8*(i+1)+5, 80, alienspeed, 500/8*(i+1)+5) )
        aliens.append( spaceship2(500/8*(i+1)+5, 120, alienspeed, 500/8*(i+1)+5) )



bullettimertime = 12
moveflag = False
movedown = 0
alienspeed = 1
roundno = 1
bullets = []
aliens = []
player = shooter(280,420)
bullettimer = 0

run=True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(aliens) == 0:
        player.x = 280
        bullets.clear()
        roundover()

    if bullettimer > 0:
        bullettimer += 1
    if bullettimer > bullettimertime:
        bullettimer = 0

    
    for b in bullets:
        if b.y > 0:
            b.y -= b.vel
        else:
            if bullets.count(b):
                del bullets[bullets.index(b)]

    for a in aliens:
        if a.y + 40 > player.y:
            gameover()

        if a.x + a.vel > a.initx + 40 or a.x + a.vel < a.initx - 40:
            a.vel *= -1
        a.x += a.vel

    if a.x + a.vel > a.initx + 40 or a.x + a.vel < a.initx - 40:
        moveflag = True
    else:
        moveflag = False
    if moveflag:
        movedown += 1
        if movedown == 5:
            moveflag = False
            for a in aliens:
                a.y += 50  
            movedown = 0 
            moveflag = False

    for b in bullets:
        for a in aliens:
            if b.y - 10 <= a.y and b.y - 10 >= a.y - 32:
                if b.x + 12 > a.x and b.x + 4 < a.x + 32:
                    if bullets.count(b):
                        del bullets[bullets.index(b)]
                    del aliens[aliens.index(a)]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x - player.vel > 0:
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x + player.vel < 570:
        player.x += player.vel

    if keys[pygame.K_SPACE] and bullettimer == 0:
        bullets.append(bullet(player.x,player.y))
        bullettimer = 1

    redraw()

    


pygame.quit()