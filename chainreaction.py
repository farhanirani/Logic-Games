import pygame
pygame.init()

win = pygame.display.set_mode((600,700))
pygame.display.set_caption("Chain Reaction")
clock = pygame.time.Clock()

#color 1 = red,   2 = blue  0 = default
class ball:
    def __init__(self,x,y,number,color):
        self.x = x
        self.y = y
        self.number = number
        self.color = color

    def draw(self):
        if self.color == 1:
            if self.number == 1:
                pygame.draw.rect(win, (79, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 2:
                pygame.draw.rect(win, (120, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 3:
                pygame.draw.rect(win, (190, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 4:
                pygame.draw.rect(win, (255, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
        
        elif self.color == 2:
            if self.number == 1:
                pygame.draw.rect(win, (0, 0, 80), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 2:
                pygame.draw.rect(win, (0, 0, 120), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 3:
                pygame.draw.rect(win, (0, 0, 190), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 4:
                pygame.draw.rect(win, (0, 0, 255), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            

def drawboard():
    global sizeofboard
    global sizeofboard
    for i in range(sizeofboard):
        pygame.draw.line(win, (40, 59, 4), ((i+1)*(600/sizeofboard), 0), ((i+1)*(600/sizeofboard), 600), 1)
    for i in range(sizeofboard):
        pygame.draw.line(win, (40, 59, 4), (0, (i+1)*(600/sizeofboard)), (600, (i+1)*(600/sizeofboard)), 1)


def redraw():
    win.fill((87, 125, 16))
    drawboard()
    for i in range(sizeofboard):
        for j in range(sizeofboard):
            board[i][j].draw()
    pygame.display.update()



# main game

sizeofboard = 12
board = [[ball(i,j,0,0) for i in range(sizeofboard)] for j in range(sizeofboard) ]
playernumber = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            y,x = pygame.mouse.get_pos()
            x = int(x//(600/sizeofboard))
            y = int(y//(600/sizeofboard))
            if x < sizeofboard and y <sizeofboard:
                #code now
                if board[x][y].color == ((playernumber%2)+1) or board[x][y].color == 0 :
                    board[x][y].color = playernumber%2+1
                    board[x][y].number += 1
                    playernumber += 1
                    print(x," ",y)

    redraw()
    

pygame.quit()
            
