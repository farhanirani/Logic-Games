import pygame,os
os.chdir('first')
pygame.init()  

walkRight = [pygame.image.load('R%s.png' % frame) for frame in range(1, 10)]
walkLeft = [pygame.image.load('L%s.png' % frame) for frame in range(1, 10)]
gwalkRight = [pygame.image.load('R%sE.png' % frame) for frame in range(1, 12)]
gwalkLeft = [pygame.image.load('L%sE.png' % frame) for frame in range(1, 12)]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#*****
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("first game")

clock = pygame.time.Clock()


class player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))


class projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy():
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 8
        self.path = [self.x,self.end]

    def draw(self,win):
        self.move()
        
        if self.walkCount+1 > 33:
            self.walkCount = 0
        
        if self.vel < 0:
            win.blit(gwalkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(gwalkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.path[1] > self.vel + self.x:
                self.x += self.vel
                self.walkCount += 1
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.path[0] < self.x + self.vel:
                self.x += self.vel
                self.walkCount += 1
            else:
                self.vel *= -1
                self.walkCount = 0


def redrawGameWindow():
    win.blit(bg,(0,0))
    goblin.draw(win)
    man.draw(win)
    for bullet in  bullets:
        bullet.draw(win)
    pygame.display.update()


# main
goblin = enemy(20,410,64,64,300)
man = player(200, 410, 64,64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x<500 and bullet.x>0:
            bullet.x += bullet.vel
        else:
            del bullets[bullets.index(bullet)]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
