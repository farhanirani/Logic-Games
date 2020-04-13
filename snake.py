import pygame,os,random
pygame.init()
os.chdir("files/snakegamefiles")

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake(ie. neel) game")
clock = pygame.time.Clock()
snakeimg = pygame.image.load("snake.png")
pygame.display.set_icon(snakeimg)


class snakehead:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        if self.x < columns-1 and gdirection == 1:
            self.x += 1
        elif self.y < rows-1 and gdirection == 2:
            self.y += 1
        elif self.x > 0 and gdirection == 3:
            self.x -= 1
        elif self.y > 0 and gdirection == 4:
            self.y -= 1
        else:
            gameover()
        pygame.draw.rect(screen, (8, 115, 20), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))


class snakebody:
    def __init__(self,x,y,directiond):
        self.x = x
        self.y = y
        self.direction = directiond
    
    def draw(self):
        if self.x < columns-1 and self.direction == 1:
            self.x += 1
        elif self.y < rows-1 and self.direction == 2:
            self.y += 1
        elif self.x > 0 and self.direction == 3:
            self.x -= 1
        elif self.y > 0 and self.direction == 4:
            self.y -= 1
        else:
            gameover()
        pygame.draw.rect(screen, (0,0,0), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))


class foood:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))


def drawBoard():
    global rows
    global columns
    for i in range(rows):
        pygame.draw.line(screen, (110, 73, 13), ((i+1)*(500/rows), 0), ((i+1)*(500/rows), 500), 1)
    for i in range(columns):
        pygame.draw.line(screen, (110, 73, 13), (0, (i+1)*(500/rows)), (500, (i+1)*(500/rows)), 1)


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
    pygame.quit()



def redraw():
    screen.fill((100,10,10))
    drawBoard()
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
rows = 20
columns = 20
food = foood(random.randint(0, rows-1), random.randint(0, columns-1))


while True:
    clock.tick(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

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
