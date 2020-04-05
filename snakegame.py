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
        pygame.draw.rect(win, (0,255,0), ( (self.x)*(500/rows), (self.y)*(500/columns), (500/columns), (500/rows) ))



def drawBoard():
    global rows
    global columns
    for i in range(rows):
        pygame.draw.line(win, (255,0,0), ((i+1)*(500/rows), 0), ((i+1)*(500/rows), 500), 1)
    for i in range(columns):
        pygame.draw.line(win, (255,0,0), (0, (i+1)*(500/rows)), (500, (i+1)*(500/rows)), 1)

def redraw():
    win.fill((100,10,10))
    drawBoard()
    snake.draw()
    pygame.display.update()


#main game
snake = snakehead(10,10)
rows = 20
columns = 20
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and snake.x > 0:
        snake.x -= 1    
    if keys[pygame.K_RIGHT] and snake.x < columns-1:
        snake.x += 1
    if keys[pygame.K_UP] and snake.y > 0:
        snake.y -= 1
    if keys[pygame.K_DOWN] and snake.y < rows-1:
        snake.y += 1


    redraw()


pygame.quit()