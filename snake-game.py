import pygame,os,random
from pygame.locals import *
pygame.init()
os.chdir("files/snakegamefiles")

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
snakeimg = pygame.image.load("snake.png")
pygame.display.set_icon(snakeimg)


class snakehead:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        if gdirection == 1:
            self.x = (self.x + 1) % columns
        elif gdirection == 2:
            self.y = (self.y + 1) % columns
        elif gdirection == 3:
            self.x = (self.x - 1) % columns
        elif gdirection == 4:
            self.y = (self.y - 1) % columns
        else:
            gameover()
        pygame.draw.rect(screen, (0, 255, 0), ( (self.x)*(600/rows), (self.y)*(600/columns), (600/columns), (600/rows) ))


class snakebody:
    def __init__(self,x,y,directiond):
        self.x = x
        self.y = y
        self.direction = directiond
    
    def draw(self):
        if self.direction == 1:
            self.x = (self.x + 1) % columns
        elif self.direction == 2:
            self.y = (self.y + 1) % columns
        elif self.direction == 3:
            self.x = (self.x - 1) % columns
        elif self.direction == 4:
            self.y = (self.y - 1) % columns
        else:
            gameover()
        pygame.draw.rect(screen, (0,150,0), ( (self.x)*(600/rows)+2, (self.y)*(600/columns)+2, (600/columns)-4, (600/rows)-4 ))


class foood:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), ( (self.x)*(600/rows)+2, (self.y)*(600/columns)+2, (600/columns)-4, (600/rows)-4 ))


def gameover():
    font = pygame.font.SysFont('franklingothicheavy', 60)
    text = font.render('GAME OVER ', 1, (255,0,0))
    screen.blit(text, (100,210))
    pygame.display.update()
    i = 0
    while i < 350:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    pygame.quit()
    exit()



def redraw():
    screen.fill((0,0,0))
    food.draw()
    snake.draw()

    nextdirection = int(previousgdirection)
    for b in snakearray:
        temp = int(b.direction)
        b.direction = int(nextdirection)
        b.draw()
        nextdirection = int(temp)
    pygame.display.update()


#main game
snakearray = []
snakearray.append(snakebody(1,10,1))
snakearray.append(snakebody(0,10,1))

previousgdirection = 1
gdirection = 1
appendflag = 0

snake = snakehead(2,10)
rows = 24
columns = 24
food = foood(random.randint(0, rows-1), random.randint(0, columns-1))


while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        

    keys = pygame.key.get_pressed()

    for s in snakearray:
        if s.x == snake.x and s.y == snake.y:
            gameover()

    if snake.x == food.x and snake.y == food.y:
        appendflag = 1
        tempx = snakearray[-1].x * 1
        tempy = snakearray[-1].y * 1
        tempdir = snakearray[-2].direction * 1

        food.x = random.randint(0, rows-1)
        food.y = random.randint(0, columns-1)
        flag = True
        while flag:
            flag = False
            for s in snakearray:
                if s.x == food.x and s.y == food.y:
                    flag = True
                    food.x = random.randint(0, rows-1)
                    food.y = random.randint(0, columns-1)
                    break

    previousgdirection = int(gdirection)
    if keys[pygame.K_LEFT] and gdirection != 3 and gdirection != 1:
        gdirection = 3
    if keys[pygame.K_RIGHT] and gdirection != 1 and gdirection != 3:
        gdirection = 1
    if keys[pygame.K_UP] and gdirection != 4 and gdirection != 2:
        gdirection = 4
    if keys[pygame.K_DOWN] and gdirection != 2 and gdirection != 4:
        gdirection = 2
    
    redraw()

    if appendflag == 1:
        snakearray.append(snakebody(tempx, tempy, tempdir))
        appendflag = 0


pygame.quit()
exit()
