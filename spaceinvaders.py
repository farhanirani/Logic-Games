import pygame,os
os.chdir("spaceinvadersfiles")
pygame.init()

win = pygame.display.set_mode((600,500))
pygame.display.set_caption("Space Invaders")

shooterimg = pygame.image.load("shooter.png")
bulletimg = pygame.image.load("bullet.png")
alienimg = pygame.image.load("alien1.png")
pygame.display.set_icon(shooterimg)

clock = pygame.time.Clock()

class spaceship:
    def __init__(self,x,y,vel):
        self.x = x
        self.y = y
        self.vel = vel

    def draw(self):
        win.blit(alienimg, (self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32),2)

class shooter:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 5
    
    def draw(self):
        win.blit(shooterimg, (self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32),2)


class bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10

    def draw(self):
        win.blit(bulletimg , (self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.x+4,self.y,8,16),2)


def redraw():
    win.fill((9, 27, 61))
    player.draw()
    aliens.draw()
    for b in bullets:
        b.draw()
        
    pygame.display.update()


bullets = []
aliens = spaceship(50,40,3)
player = shooter(280,420)
bullettimer = 0

run=True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if bullettimer > 0:
        bullettimer += 1
    if bullettimer > 10:
        bullettimer = 0

    
    for b in bullets:
        if b.y > 0:
            b.y -= b.vel
        else:
            del bullets[bullets.index(b)]

    
    if aliens.x + aliens.vel > 570 or aliens.x + aliens.vel < 0:
        aliens.vel *= -1
    aliens.x += aliens.vel

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