import pygame
pygame.init()

screen = pygame.display.set_mode((600,700))
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
            if self.number == 1 and (self.x % (sizeofboard-1) == 0 and self.y % (sizeofboard-1) == 0):  #check 1 and corner
                pygame.draw.rect(screen, (255, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 1 and (self.x % (sizeofboard-1) == 0 or self.y % (sizeofboard-1) == 0):  #check 1 and edge
                pygame.draw.rect(screen, (190, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 1:  #check 1 for full board
                pygame.draw.rect(screen, (50, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            elif self.number == 2 and (self.x % (sizeofboard-1) == 0 or self.y % (sizeofboard-1) == 0):   #if 2 for edge
                pygame.draw.rect(screen, (255, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 2:  #2 for remaining board
                pygame.draw.rect(screen, (80, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            elif self.number == 3:
                pygame.draw.rect(screen, (190, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 4:
                pygame.draw.rect(screen, (255, 0, 0), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            font = pygame.font.SysFont('franklingothicheavy', 15)
            text = font.render(str(self.number), 1, (255,255,255))
            screen.blit(text, ((self.x)*(600/sizeofboard)+10, (self.y)*(600/sizeofboard)+10) )

            
        elif self.color == 2:
            if self.number == 1 and (self.x % (sizeofboard-1) == 0 and self.y % (sizeofboard-1) == 0):  #check 1 and corner
                pygame.draw.rect(screen, (0, 0, 255), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 1 and (self.x % (sizeofboard-1) == 0 or self.y % (sizeofboard-1) == 0):  #check 1 and edge
                pygame.draw.rect(screen, (0, 0, 190), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 1:  #check 1 for full board
                pygame.draw.rect(screen, (0, 0, 50), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            elif self.number == 2 and (self.x % (sizeofboard-1) == 0 or self.y % (sizeofboard-1) == 0):   #if 2 for edge
                pygame.draw.rect(screen, (0, 0, 255), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 2:  #2 for remaining board
                pygame.draw.rect(screen, (0, 0, 80), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            elif self.number == 3:
                pygame.draw.rect(screen, (0, 0, 190), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )
            elif self.number == 4:
                pygame.draw.rect(screen, (0, 0, 255), ( (self.x)*(600/sizeofboard), (self.y)*(600/sizeofboard), (600/sizeofboard), (600/sizeofboard) ) )

            font = pygame.font.SysFont('franklingothicheavy', 15)
            text = font.render(str(self.number), 1, (255,255,255))
            screen.blit(text, ((self.x)*(600/sizeofboard)+10, (self.y)*(600/sizeofboard)+10) )

#-------------------------------------
def beamsurroundingslots(x,y,playernumber):
    board[x][y].number = 0
    board[x][y].color = 0

    if x+1 < sizeofboard:
        beam(x+1,y,playernumber)
    if y+1 < sizeofboard:
        beam(x,y+1,playernumber)
    if x != 0:
        beam(x-1,y,playernumber)
    if y != 0:
        beam(x,y-1,playernumber)


def beam(x,y,playernumber):
    redraw()
    pygame.time.delay(80)
    if x % (sizeofboard-1) == 0 and y % (sizeofboard-1) == 0:   #corner max 1 then burst
        if board[x][y].number < 1:
            board[x][y].color = playernumber
            board[x][y].number += 1
        else:
            beamsurroundingslots(x,y,playernumber)

    elif x % (sizeofboard-1) == 0 or y % (sizeofboard-1) == 0: #for edges, max 2 then burst
        if board[x][y].number < 2:
            board[x][y].color = playernumber
            board[x][y].number += 1
        else:
            beamsurroundingslots(x,y,playernumber)
    
    else: #normal case
        if board[x][y].number < 4:
            board[x][y].color = playernumber
            board[x][y].number += 1
        else:
            beamsurroundingslots(x,y,playernumber)
    redraw()
#---------------------------------------------------


def drawboard():
    global sizeofboard
    for i in range(sizeofboard):
        pygame.draw.line(screen, (40, 59, 4), ((i+1)*(600/sizeofboard), 0), ((i+1)*(600/sizeofboard), 600), 1)
    for i in range(sizeofboard):
        pygame.draw.line(screen, (40, 59, 4), (0, (i+1)*(600/sizeofboard)), (600, (i+1)*(600/sizeofboard)), 1)


def redraw():
    screen.fill((87, 125, 16))
    drawboard()
    for i in range(sizeofboard):
        for j in range(sizeofboard):
            board[i][j].draw()
        #     print(board[i][j].number,end=" ")
        # print()
    pygame.display.update()


def decoration():
    font = pygame.font.SysFont('franklingothicheavy', 40)
    p = [0,0,0]
    for i in range(sizeofboard):
        for j in range(sizeofboard):
            p[board[i][j].color] += 1
    if p[1] == 0 and playernumber > 3:
        text = font.render('Player 2 wins!!!! ', 1, (0,0,255))
        screen.blit(text, (170,620))
        pygame.display.update()
        delayy()
    elif p[2] == 0 and playernumber > 3:
        text = font.render('Player 1 wins!!! ', 1, (255,0,0))
        screen.blit(text, (170,620))
        pygame.display.update()
        delayy()
    else:
        if playernumber%2+1 == 1:
            text = font.render('Player 1 ', 1, (255,0,0))
        else:
            text = font.render('Player 2 ', 1, (0,0,255))
    screen.blit(text, (170,620))
    pygame.display.update()

def delayy():
    i = 0
    while i < 350:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.quit()

    
# main game

sizeofboard = 10
board = [[ball(i,j,0,0) for i in range(sizeofboard)] for j in range(sizeofboard) ]
playernumber = 0

redraw()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            y,x = pygame.mouse.get_pos()
            x = int(x//(600/sizeofboard))
            y = int(y//(600/sizeofboard))
            if x < sizeofboard and y < sizeofboard:
                if board[x][y].color == ((playernumber%2)+1) or board[x][y].color == 0 :
                    # print((playernumber%2)+1,x,y)
                    beam(x,y,(playernumber%2)+1)
                    playernumber += 1
    decoration()                
pygame.quit()
            
