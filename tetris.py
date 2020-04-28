import pygame, os, random
from pygame.locals import *
os.chdir('files/tetrisfiles')
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("TETRIS")
win = pygame.display.set_mode((400, 700),0,32)
tetri = pygame.image.load("tetris.png")
rowflash = pygame.image.load("rowflash.png")
pygame.display.set_icon(rowflash)

score = 0

def checkIfRowIsFull():
    global board
    global score
    tempTimer = False
    rowNum = []

    for row in range(20):
        isFull = True
        for col in range(10):
            if board[row][col] == 0:
                isFull = False

        if isFull:
            rowNum.append(row)
            if not tempTimer:
                pygame.time.delay(500)
            tempTimer = True
            
            for col in range(10):
                win.blit(rowflash,( 50+ 30*col, 50+ 30*row ))
            pygame.display.update()
            
            for col in range(10):
                board[row][col] = 0

    if tempTimer:
        pygame.time.delay(500)
        for num in rowNum:
            score += 1
            for col in range(10):
                board[0][col] = 0
            for row in reversed(range(num)):
                board[row+1] = board[row] * 1
        


def checkIfGameover():
    for col in range(10):
        if board[0][col] == 1:
            text = font.render('GAME OVER ', 1, (200,200,200))
            win.blit(text, (140,210))
            pygame.display.update()
            i = 0
            while i < 350:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key ==K_ESCAPE:
                            pygame.quit()
                            exit()
            pygame.quit()



def drawBoard():
    global score
    win.fill((0,0,0))
    pygame.draw.rect(win, (83,83,83), (50,50,300,600))

    text = font.render("SCORE : "+str(score), 1, (200,200,200))
    win.blit(text, (150,10))

    for col in range(10):
        for row in range(20):
            if board[row][col] == 1:
                win.blit(tetri, (50+ 30*col, 50+ 30*row))
    pygame.display.update()



#main game

board = [[0 for col in range(10)] for row in range(20) ]
# for col in range(10):
#         if col != 4:
#             for row in range(15,20):
#                 board[row][col] = 1

font = pygame.font.SysFont('franklingothicheavy', 20)

curCol = 4
curRow = 0
moveTimer = 0

lineSleeping = 0
lineStanding = 0

isFalling = False

while True:
    #quit game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_UP and curCol != 9:
                if lineSleeping == 1 or board[curRow][curCol+1] != 1:
                    lineSleeping, lineStanding = lineStanding, lineSleeping
    
    
    # #movement -------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    
    if moveTimer >= 0:
        incrementTimer = False

        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            if curCol > 0  and curRow+lineStanding  < 19 and board[curRow +1][curCol-1] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping-1] != 1 and board[curRow+lineStanding +1][curCol-1] != 1 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1: # to move bottom left
                board[curRow][curCol] = 0
                curCol -= 1
                curRow += 1 
            elif curCol > 0 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1 : # to move left
                board[curRow][curCol] = 0
                curCol -= 1
            elif curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 : # to move down
                board[curRow][curCol] = 0
                curRow += 1
            else:
                incrementTimer = True

        
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            if curCol+lineSleeping < 9 and curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol+1] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping +1] != 1 and  board[curRow+lineStanding +1][curCol+lineSleeping +1] != 1 and board[curRow][curCol+lineSleeping +1] != 1 and board[curRow+lineStanding][curCol+ lineSleeping+1] != 1 :  #move bottom right
                board[curRow][curCol] = 0
                curCol += 1
                curRow += 1
            elif curCol+lineSleeping < 9 and board[curRow][curCol+lineSleeping +1] != 1 and board[curRow+lineStanding][curCol+ lineSleeping+1] != 1 : # move right
                board[curRow][curCol] = 0
                curCol += 1
            elif curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 : # to move down
                board[curRow][curCol] = 0
                curRow += 1
            else:
                incrementTimer = True


        elif keys[pygame.K_LEFT]:
            if curCol > 0 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1 :
                board[curRow][curCol] = 0
                curCol -= 1
            else:
                incrementTimer = True

        elif keys[pygame.K_RIGHT] :
            if curCol+lineSleeping < 9 and board[curRow][curCol+ lineSleeping+1] != 1 and board[curRow+lineStanding ][curCol+ lineSleeping+1] != 1 :
                board[curRow][curCol] = 0
                curCol += 1
            else:
                incrementTimer = True
        
        elif keys[pygame.K_DOWN] and curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 :
            board[curRow][curCol] = 0
            curRow += 1

        else:
            incrementTimer = True
    else:
            incrementTimer = True

    # #movement -------------------------------------------------------------------

    if incrementTimer and (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
        isFalling = False
        
    if isFalling and incrementTimer:
        if moveTimer == 5:
            curRow += 1
            moveTimer = 0
        else:
            moveTimer += 1

    
    

    #set current position to 1
    for stand in range(lineStanding+1):
        for sleep in range(lineSleeping+1):
            board[curRow+ stand][curCol+ sleep] = 1
    
    drawBoard()

    # pygame.draw.rect(win, (255,0,0), (50+ 30*curCol, 50+ 30*curRow, 30*(1+lineSleeping), 30*(1+lineStanding) ), 1 )
    # pygame.display.update()
    
    # os.system('cls')
    # for i in range(20):
    #     print(board[i])

    # if it is not falling, set the value and reset currow and curcol
    if not isFalling:
        curRow = 0
        curCol = 4
        isFalling = True
        checkIfRowIsFull()
        moveTimer = -5

        veryTemp = random.randint(0,2)
        if veryTemp == 0:
            lineStanding = 1
            lineSleeping = 0
        elif veryTemp == 1:
            lineStanding = 0
            lineSleeping = 1
        else:
            lineSleeping = 1
            lineStanding = 1

        for stand in range(lineStanding+1):
            for sleep in range(lineSleeping+1):
                board[curRow+ stand][curCol+ sleep] = 1

    else:
        for stand in range(lineStanding+1):
            for sleep in range(lineSleeping+1):
                board[curRow+ stand][curCol+ sleep] = 0

    mainClock.tick(15)