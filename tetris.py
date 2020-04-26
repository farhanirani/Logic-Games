import pygame, os
from pygame.locals import *
os.chdir('files/tetrisfiles')
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("TETRIS")
win = pygame.display.set_mode((400, 700),0,32)
tetri = pygame.image.load("tetris.png")
rowflash = pygame.image.load("rowflash.png")


def checkIfRowIsFull():
    global board
    tempTimer = False

    for row in range(20):
        isFull = True
        for col in range(10):
            if board[row][col] == 0:
                isFull = False

        if isFull:
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
                

def drawBoard():
    win.fill((0,0,0))
    pygame.draw.rect(win, (83,83,83), (50,50,300,600))

    for col in range(10):
        for row in range(20):
            if board[row][col] == 1:
                win.blit(tetri, (50+ 30*col, 50+ 30*row))
    pygame.display.update()

#main game

board = [[0 for col in range(10)] for row in range(20) ]

curCol = 4
curRow = 0
moveTimer = 0

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
    
    
    # #movement -------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    
    incrementTimer = False

    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        if curCol > 0 and board[curRow+1][curCol-1] != 1 and curRow < 19 : # to move bottom left
            board[curRow][curCol] = 0
            curCol -= 1
            curRow += 1 
        elif curCol > 0 and board[curRow][curCol-1] != 1 : # to move left
            board[curRow][curCol] = 0
            curCol -= 1
        elif curRow < 19 and board[curRow+1][curCol] != 1 : # to move down
            board[curRow][curCol] = 0
            curRow += 1
        else:
            incrementTimer = True

    
    elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        if curCol < 9 and board[curRow+1][curCol+1] != 1 and curRow < 19 :  #move bottom right
            board[curRow][curCol] = 0
            curCol += 1
            curRow += 1
        elif curCol < 9 and board[curRow][curCol+1] != 1 : # move right
            board[curRow][curCol] = 0
            curCol += 1
        elif curRow < 19 and board[curRow+1][curCol] != 1 : # to move down
            board[curRow][curCol] = 0
            curRow += 1
        else:
            incrementTimer = True


    elif keys[pygame.K_LEFT]:
        if curCol > 0 and board[curRow][curCol-1] != 1 :
            board[curRow][curCol] = 0
            curCol -= 1
        else:
            incrementTimer = True

    elif keys[pygame.K_RIGHT] :
        if curCol < 9 and board[curRow][curCol+1] != 1 :
            board[curRow][curCol] = 0
            curCol += 1
        else:
            incrementTimer = True
    
    elif keys[pygame.K_DOWN] and curRow < 19 and board[curRow+1][curCol] != 1 :
        board[curRow][curCol] = 0
        curRow += 1

    else:
        incrementTimer = True

    # #movement -------------------------------------------------------------------

    
    if isFalling and incrementTimer:
        if moveTimer == 5:
            curRow += 1
            moveTimer = 0
        else:
            moveTimer += 1

    if curRow == 19 or board[curRow+1][curCol] == 1 :
        isFalling = False
    

    #set curr position to 1
    board[curRow][curCol] = 1
    
    drawBoard()
    
    
    # os.system('cls')
    # for i in range(20):
    #     print(board[i])

    # if it is not falling, set the value and reset currow and curcol
    if not isFalling:
        curRow = 0
        curCol = 4
        isFalling = True
        board[curRow][curCol] = 1
        checkIfRowIsFull()
    else:
        board[curRow][curCol] = 0
    

    mainClock.tick(20)