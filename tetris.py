import pygame, os
from pygame.locals import *
os.chdir('files/tetrisfiles')
pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption("TETRIS")
win = pygame.display.set_mode((400, 700),0,32)
tetri = pygame.image.load("tetris.png")
rowflash = pygame.image.load("rowflash.png")


# def drawBoard():
#     global isFalling
#     global curCol 
#     global curRow

#     board[curRow][curCol] = 1

#     for col in range(10):
#         for row in range(20):
#             if board[row][col] == 1:
#                 win.blit(tetri, (50+ 30*col, 50+ 30*row) )

#     if not isFalling:
#         curRow = 0
#         curCol = 4
#         isFalling = True
#         board[curRow][curCol] = 1
#     else:
#         board[curRow][curCol] = 0


def redraw():
    win.fill((0,0,0))
    pygame.draw.rect(win, (83,83,83), (50,50,300,600))
    # drawBoard()
    pygame.display.update()

#main game

board = [[0 for col in range(10)] for row in range(20) ]

curCol = 4
curRow = 0
moveTimer = 0

isFalling = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    
    # #movement
    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT] and curCol > 0 and board[curRow][curCol-1] != 1 :
    #     board[curRow][curCol] = 0
    #     curCol -= 1

    # if keys[pygame.K_RIGHT] and curCol < 9 and board[curRow][curCol+1] != 1 :
    #     board[curRow][curCol] = 0
    #     curCol += 1
    
    # if keys[pygame.K_DOWN] and curRow < 19 and board[curRow+1][curCol] != 1 :
    #     board[curRow][curCol] = 0
    #     curRow += 1

    # if isFalling:
    #     if moveTimer == 5:
    #         curRow += 1
    #         moveTimer = 0
    #     else:
    #         moveTimer += 1

    #     if curRow == 19 or board[curRow+1][curCol] == 1 :
    #         isFalling = False
        
    
    
    redraw()
    mainClock.tick(10)