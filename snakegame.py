import pygame,os
pygame.init()
os.chdir("snakegamefiles")

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake(ie. neel) game")
clock = pygame.time.Clock()
snakeimg = pygame.image.load("snake.png")
pygame.display.set_icon(snakeimg)


class snakehead:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        if self.x < columns-1 and direction == 1:
            self.x += 1
        elif self.y < rows-1 and direction == 2:
            self.y += 1
        elif self.x > 0 and direction == 3:
            self.x -= 1
        elif self.y > 0 and direction == 4:
            self.y -= 1
        else:
            pass
        pygame.draw.rect(win, (0,255,0), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))


class snakebody:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def draw(self):
        if self.x < columns-1 and self.direction == 1:
            self.x += 1
        elif self.y < rows-1 and self.direction == 2:
            self.y += 1
        elif self.x > 0 and self.direction == 3:
            self.x -= 1
        elif self.y > 0 and self.direction == 4:
            self.y -= 1
        pygame.draw.rect(win, (13, 120, 13), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))



def drawBoard():
    global rows
    global columns
    for i in range(rows):
        pygame.draw.line(win, (110, 73, 13), ((i+1)*(500/rows), 0), ((i+1)*(500/rows), 500), 1)
    for i in range(columns):
        pygame.draw.line(win, (110, 73, 13), (0, (i+1)*(500/rows)), (500, (i+1)*(500/rows)), 1)

def redraw():
    win.fill((100,10,10))
    drawBoard()
    snake.draw()
    previousdir = direction
    for b in snakearray:
        temp = int(previousdir)
        b.direction = previousdir
        b.draw()
        previousdir = temp
    pygame.display.update()


#main game
snakearray = []
snakearray.append(snakebody(9,10,1)) 
snakearray.append(snakebody(8,10,1))
previousdir = 1
direction = 1
snake = snakehead(10,10)
rows = 20
columns = 20
run = True
while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and direction != 3 and direction != 1:
        direction = 3
    if keys[pygame.K_RIGHT] and direction != 1 and direction != 3:
        direction = 1
    if keys[pygame.K_UP] and direction != 4 and direction != 2:
        direction = 4
    if keys[pygame.K_DOWN] and direction != 2 and direction != 4:
        direction = 2

    redraw()


pygame.quit()