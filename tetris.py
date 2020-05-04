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



def checkIMoveDOWNLEFT():
    c = 0
    for r in range(-1,2):
        if not(c==Lcol and r==Lrow):
            if board[curRow + r + 1][curCol + c - 1] == 1:
                return 0
    r = 1    
    for c in range(2):
        if not(c==Lcol and r==Lrow):
            if board[curRow + r + 1][curCol + c] == 1:
                return 0
    if board[curRow + Lrow][curCol + Lcol] == 1:
        return 0
    return 1

def checkIMoveDOWNRIGHT():
    c = 1
    for r in range(-1,2):
        if not(c==Lcol and r==Lrow):
            if board[curRow + r + 1][curCol + c + 1] == 1:
                return 0
    r = 1    
    for c in range(2):
        if not(c==Lcol and r==Lrow):
            if board[curRow + r + 1][curCol + c] == 1:
                return 0
    if board[curRow + Lrow][curCol + Lcol] == 1:
        return 0
    return 1


#main game

board = [[0 for col in range(10)] for row in range(20) ]
# for col in range(10):
#         if col != 4:
#             for row in range(15,20):
#                 board[row][col] = 1

Ltrue = False
Lrow = 0
Lcol = 0

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
                if (lineSleeping == 1 and board[curRow + 1][curCol] != 1) or (lineStanding == 1 and board[curRow][curCol+1] != 1):
                    lineSleeping, lineStanding = lineStanding, lineSleeping
                    if Ltrue:
                        if Lrow == 0 :
                            if Lcol == 0:
                                Lcol = 1
                            else:
                                Lrow = 1
                        else:
                            if Lcol == 0:
                                Lrow = 0
                            else:
                                Lcol = 0
            if event.key == K_UP and  lineSleeping == 0 and lineStanding == 1 and curCol == 9:
                lineSleeping, lineStanding = lineStanding, lineSleeping
                curCol = 8
    
    
    # #movement -------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    
    if moveTimer >= 0:
        incrementTimer = False

        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and not Ltrue:
            # to move bottom left
            if curCol > 0  and curRow+lineStanding  < 19 and board[curRow +1][curCol-1] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping-1] != 1 and board[curRow+lineStanding +1][curCol-1] != 1 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1: 
                curCol -= 1
                curRow += 1 
            # to move left
            elif curCol > 0 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1 : 
                curCol -= 1
            # to move down
            elif curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 : # to move down
                curRow += 1
            else:
                incrementTimer = True
        
        # for L shape
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and Ltrue:
            # to move bottom left
            if curCol > 0  and curRow+lineStanding  < 19 and checkIMoveDOWNLEFT() == 1 :
                curCol -= 1
                curRow += 1 
            # to move left
            elif curCol > 0 and Lcol == 0 and board[curRow + (Lrow+1)%2][curCol-1] != 1 and board[curRow + Lrow][curCol] != 1 :
                curCol -= 1
            elif curCol > 0 and board[curRow][curCol-1] != 1 and board[curRow+1][curCol-1] != 1 :
                curCol -= 1
            # to move down
            elif Lrow == 1 and Lcol == 0 and (not (curRow+lineStanding  >= 19 or board[curRow +1][curCol] == 1 or board[curRow + 2][curCol + 1] == 1)) : 
                curRow += 1
            elif Lrow == 1 and Lcol == 1 and (not (curRow+lineStanding  >= 19 or board[curRow + 2][curCol] == 1 or board[curRow + 1][curCol + 1] == 1)) :
                curRow += 1
            elif not (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
                curRow += 1
            else:
                incrementTimer = True

        
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and not Ltrue:
            #move bottom right
            if curCol+lineSleeping < 9 and curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol+1] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping +1] != 1 and  board[curRow+lineStanding +1][curCol+lineSleeping +1] != 1 and board[curRow][curCol+lineSleeping +1] != 1 and board[curRow+lineStanding][curCol+ lineSleeping+1] != 1 :
                curCol += 1
                curRow += 1
            # move right
            elif curCol+lineSleeping < 9 and board[curRow][curCol+lineSleeping +1] != 1 and board[curRow+lineStanding][curCol+ lineSleeping+1] != 1 : 
                curCol += 1
            # to move down
            elif curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 :
                curRow += 1
            else:
                incrementTimer = True

        # for L shape
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and Ltrue:
            # move bottom right
            if curCol+lineSleeping < 9 and curRow+lineStanding  < 19 and checkIMoveDOWNRIGHT() == 1 :
                curCol += 1
                curRow += 1
            # move right
            elif curCol+lineSleeping < 9 and Lcol == 1 and board[curRow + (Lrow+1)%2][curCol+2] != 1 and board[curRow + Lrow][curCol+1] != 1 :
                curCol += 1
            elif curCol+lineSleeping < 9 and board[curRow][curCol+2] != 1 and board[curRow+1][curCol+2] != 1 :
                curCol += 1
            # to move down
            elif Lrow == 1 and Lcol == 0 and (not (curRow+lineStanding  >= 19 or board[curRow +1][curCol] == 1 or board[curRow + 2][curCol + 1] == 1)) : 
                curRow += 1
            elif Lrow == 1 and Lcol == 1 and (not (curRow+lineStanding  >= 19 or board[curRow + 2][curCol] == 1 or board[curRow + 1][curCol + 1] == 1)) :
                curRow += 1
            elif not (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
                curRow += 1
            else:
                incrementTimer = True


        elif keys[pygame.K_LEFT]:
            if Ltrue and curCol > 0:
                if Lcol == 0 and board[curRow + (Lrow+1)%2][curCol-1] != 1 and board[curRow + Lrow][curCol] != 1 :
                    curCol -= 1
                elif board[curRow][curCol-1] != 1 and board[curRow+1][curCol-1] != 1 :
                    curCol -= 1
                else:
                    incrementTimer = True
            elif curCol > 0 and board[curRow][curCol-1] != 1 and board[curRow+lineStanding ][curCol-1] != 1 :
                curCol -= 1
            else:
                incrementTimer = True

        elif keys[pygame.K_RIGHT] :
            if Ltrue and curCol + 1 < 9:
                if Lcol == 1 and board[curRow + (Lrow+1)%2][curCol+2] != 1 and board[curRow + Lrow][curCol+1] != 1 :
                    curCol += 1
                elif board[curRow][curCol+2] != 1 and board[curRow+1][curCol+2] != 1 :
                    curCol += 1
                else:
                    incrementTimer = True
            elif curCol+lineSleeping < 9 and board[curRow][curCol+ lineSleeping+1] != 1 and board[curRow+lineStanding ][curCol+ lineSleeping+1] != 1 :
                curCol += 1
            else:
                incrementTimer = True
        
        elif keys[pygame.K_DOWN] :
            if Ltrue:
                if Lrow == 1 and Lcol == 0 and (not (curRow+lineStanding  >= 19 or board[curRow +1][curCol] == 1 or board[curRow + 2][curCol + 1] == 1)) :
                    curRow += 1
                elif Lrow == 1 and Lcol == 1 and (not (curRow+lineStanding  >= 19 or board[curRow + 2][curCol] == 1 or board[curRow + 1][curCol + 1] == 1)) :
                    curRow += 1
                elif not (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
                    curRow += 1
                else:
                    incrementTimer = True
            elif curRow+lineStanding  < 19 and board[curRow+lineStanding +1][curCol] != 1 and board[curRow+lineStanding +1][curCol+lineSleeping] != 1 :
                curRow += 1
            else:
                incrementTimer = True

        else:
            incrementTimer = True
    else:
            incrementTimer = True

    # #movement -------------------------------------------------------------------

    # check if it should stop falling
    if incrementTimer:
        if Ltrue:
            if Lrow == 1 and Lcol == 0:
                if (curRow+lineStanding  >= 19 or board[curRow +1][curCol] == 1 or board[curRow + 2][curCol + 1] == 1) :
                    isFalling = False
            elif Lrow == 1 and Lcol == 1:
                if (curRow+lineStanding  >= 19 or board[curRow + 2][curCol] == 1 or board[curRow + 1][curCol + 1] == 1) :
                    isFalling = False
            else:
                if (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
                    isFalling = False
        else:
            if (curRow+lineStanding  >= 19 or board[curRow+lineStanding +1][curCol] == 1 or board[curRow+lineStanding +1][curCol+lineSleeping] == 1) :
                isFalling = False
    if Ltrue:
        if Lrow==1 and board[curRow + Lrow][curCol + Lcol] == 1:
            isFalling = False


    # if its falling normally check if you can increase curRow
    if isFalling and incrementTimer:
        if moveTimer == 5:
            curRow += 1
            moveTimer = 0
        else:
            moveTimer += 1

    
    #set current position to 1
    for stand in range(lineStanding+1):
        for sleep in range(lineSleeping+1):
            if not Ltrue or not (Lrow == stand and Lcol == sleep):
                board[curRow+ stand][curCol+ sleep] = 1
    
    drawBoard()

    # if it is not falling, set the value and reset currow and curcol
    if not isFalling:
        curRow = 0
        curCol = 4
        isFalling = True
        checkIfRowIsFull()
        moveTimer = -5

        # set next shape
        veryTemp = random.randint(0, 3)
        if veryTemp == 0: # for line
            lineStanding = 1
            lineSleeping = 0
            Ltrue = False
        elif veryTemp == 1 or veryTemp == 2: # for L shape 50%
            lineStanding = 1 
            lineSleeping = 1
            Ltrue = True
            Lrow = random.randint(0,1)
            Lcol = random.randint(0,1)
        else:  # for square
            lineSleeping = 1
            lineStanding = 1
            Ltrue = False

        for stand in range(lineStanding+1):
            for sleep in range(lineSleeping+1):
                if not Ltrue or not (Lrow == stand and Lcol == sleep):   # to not draw the piece of L if its L or if its L and the same Lrow and Lcol
                    board[curRow+ stand][curCol+ sleep] = 1

    elif isFalling:
        for stand in range(lineStanding+1):
            for sleep in range(lineSleeping+1):
                if not Ltrue or not (Lrow == stand and Lcol == sleep):
                    board[curRow+ stand][curCol+ sleep] = 0

    mainClock.tick(10)
