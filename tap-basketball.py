import pygame,os,random
os.chdir('files/tapballfiles')
pygame.init()  

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tap BasketBall")
ballimg = pygame.image.load("basketball.png")
rightb = pygame.image.load('rightbasket.png')
leftb = pygame.image.load('leftbasket.png')

pygame.display.set_icon(ballimg)
clock = pygame.time.Clock()


#min = 50, max = 750


class ball:
    x = 200
    y = 500
    
    def draw(self):
        if left:
            if self.x - vel > 40:
                self.x -= vel
            else:
                self.x = 750
        elif right:
            if self.x + vel + 32 < 765:
                self.x += vel
            else:
                self.x = 50

        win.blit(ballimg,(self.x,self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x,self.y,32,32), 1)


class basket:
    x = 42
    y = random.randint(100,420)
    def draw(self):
        if left:
            self.x = 80
            win.blit(leftb,(self.x,self.y))
        elif right:
            self.x = 640
            win.blit(rightb,(self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.x,self.y+40,128,20), 1)


def redraw():
    win.fill((255, 123, 0))
    b.draw()
    bask.draw()

    pygame.display.update()


#main game

neg = 1
jumpcount = 10
delayNum = 0
bask = basket()
b = ball()
vel = 5
left = False
right = True
bounce = 0

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if delayNum > 0:
        delayNum += 1
    if delayNum > 10:
        delayNum = 0

    if keys[pygame.K_SPACE] and delayNum == 0:
        bounce = 1
        delayNum = 1
        jumpcount = 10

    if bounce > 0:
        if jumpcount >= -100:
            neg = 1
            if jumpcount < 0:
                neg = -1
            if b.y - (jumpcount ** 2) * 0.4 * neg < 550:
                b.y -= (jumpcount ** 2) * 0.4 * neg
            jumpcount -= 1
        else:
            jumpcount = 10
            bounce = 0


    if b.x + 16 > bask.x and b.x + 16 < bask.x + 128 and  neg == -1:
        if b.y + 32 > bask.y + 20 and b.y + 32 < bask.y + 80:
            if left:
                left = False
                right = True
                bask.y = random.randint(100,420)
            elif right:
                left = True
                right = False
                bask.y = random.randint(100,420)
            if vel < 4:
                vel += 1

    redraw()

pygame.quit()