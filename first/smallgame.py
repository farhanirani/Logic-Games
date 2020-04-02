import pygame
pygame.init()

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")

x=50
y=425
width = 64
height = 64
vel = 5
left = False
right = False
walkcount = 0


isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and  x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x + width + vel <= 500:
        x += vel
    if keys[pygame.K_SPACE]:
        isJump = True
    if isJump:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit
