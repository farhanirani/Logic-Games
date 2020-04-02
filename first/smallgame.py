import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")

x=300
y=300
width = 20
height = 20
vel = 5

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
