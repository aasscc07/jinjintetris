import pygame
import sys
import random
import time

# Pygame 초기화


I_BLOCK = [
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0]],

    [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0]],

    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0]]
]

L1_BLOCK = [
    [[1, 0, 0],
     [1, 1, 1],
     [0, 0, 0]],

    [[0, 1, 1],
     [0, 1, 0],
     [0, 1, 0]],

    [[0, 0, 0],
     [1, 1, 1],
     [0, 0, 1]],

    [[0, 1, 0],
     [0, 1, 0],
     [1, 1, 0]]
]


L2_BLOCK = [
    [[0, 0, 1],
     [1, 1, 1],
     [0, 0, 0]],

    [[0, 1, 0],
     [0, 1, 0],
     [0, 1, 1]],

    [[0, 0, 0],
     [1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
]


T_BLOCK = [
    [[0, 1, 0],
     [1, 1, 1],
     [0, 0, 0]],

    [[0, 1, 0],
     [0, 1, 1],
     [0, 1, 0]],

    [[0, 0, 0],
     [1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [0, 1, 0]]
]

O_BLOCK = [
    [[1, 1],
     [1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1],
     [1, 1]]
]

Z1_BLOCK = [
    [[0, 1, 1],
     [1, 1, 0],
     [0, 0, 0]],

    [[0, 1, 0],
     [0, 1, 1],
     [0, 0, 1]],

    [[0, 0, 0],
     [0, 1, 1],
     [1, 1, 0]],

    [[1, 0, 0],
     [1, 1, 0],
     [0, 1, 0]]
]

Z2_BLOCK = [
    [[1, 1, 0],
     [0, 1, 1],
     [0, 0, 0]],

    [[0, 0, 1],
     [0, 1, 1],
     [0, 1, 0]],

    [[0, 0, 0],
     [1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 0],
     [1, 1, 0],
     [1, 0, 0]]
]

# 게임창 만들기
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
LINE_SIZE_X = 5
LINE_SIZE_Y = 5
    
PLAYING_FIELD_WIDTH = 16
PLAYING_FIELD_HEIGHT = 32
BLOCK_SIZE = 24
playing_field = [[0] * PLAYING_FIELD_WIDTH for _ in range(PLAYING_FIELD_HEIGHT)]
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

C_RED = (255,0,0)
C_MINT = (9,247,164)
C_P = (176,18,237)
C_B = (0,128,255)

COLOR_TYPE = [C_RED]

# I_BLOCK 그리기 함수
def draw_block(x, y, block_direction,Block,Color):
    RectArray = []
    for i in range(len(Block[block_direction])):
        for j in range(len(Block[block_direction][i])):
            if Block[block_direction][i][j]:
                rect = pygame.Rect(x+j*BLOCK_SIZE, y+i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                RectArray.append(rect)
                # RectArray.append(Color)
                pygame.draw.rect(screen, Color, rect)

def draw_block_(rect,Color):
    for i in range(len(rect)):
        print('test')
        pygame.draw.rect(screen,Color,rect[i])
    
def Get_draw_block(x, y, block_direction,Block,Color):
    RectArray = []
    for i in range(len(Block[block_direction])):
        for j in range(len(Block[block_direction][i])):
            if Block[block_direction][i][j]:
                rect = pygame.Rect(x+j*BLOCK_SIZE, y+i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                RectArray.append(rect)
                # RectArray.append(Color)

    return RectArray

                

def block_color():
    B_color = random.randrange(4)
    color_ = [C_RED,C_MINT,C_P,C_B]  
    for i in range(len(color_)):
         if B_color == i:
            return color_[i]

def CheckBlockTypeNum(BlockTypeNum):
    v1_ = [I_BLOCK,L1_BLOCK,L2_BLOCK,T_BLOCK,O_BLOCK,Z1_BLOCK,Z2_BLOCK] # 7개 요소
    for i in range(len(v1_)):
         if BlockTypeNum == i:
            return v1_[i]COLOR_TYPE[0]
         

# def EmptyLineCheck(Block,Direction):
#     for i in range(len(Block[Direction])):
#         for j in range(len(Block[Direction][i])):
            


#==============================< Various List >============================#
Block_State = True
B_type = 0
B_direction = 0

BlockDownSpeed = 0
KeyBoardDownSpeed = 0

KBDS = 1

Block_Y_INC = 1
Block_X_Position = 7 #7
#==========================================================================#

Block_Stack = []

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if KeyBoardDownSpeed > KBDS:
                        Block_X_Position -= 1
                        KeyBoardDownSpeed = 0
                elif event.key == pygame.K_RIGHT:
                    if KeyBoardDownSpeed > KBDS:
                        Block_X_Position += 1
                        KeyBoardDownSpeed = 0
                elif event.key == pygame.K_DOWN:
                    if KeyBoardDownSpeed > KBDS:
                        Block_Y_INC += 1
                        KeyBoardDownSpeed = 0
                elif event.key == pygame.K_UP:
                    if KeyBoardDownSpeed > KBDS:
                        B_direction += 1
                        # Block_Y_INC -= 1
                        KeyBoardDownSpeed = 0
                if event.key == pygame.K_g:
                    Block_State = True
                
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

    if KeyBoardDownSpeed > 1000:
        KeyBoardDownSpeed = 0

    KeyBoardDownSpeed += 1

    #Wall Cheching
    if Block_X_Position < 0:
        Block_X_Position = 0

    if Block_Y_INC > 29:
        Block_Y_INC = 29
        Block_Stack.append(Get_draw_block(LINE_SIZE_X + BLOCK_SIZE * Block_X_Position , LINE_SIZE_Y + BLOCK_SIZE * (Block_Y_INC), B_direction , CheckBlockTypeNum(B_type),B_color))
        Block_State = True

    for i in range(len(Block_Stack)):
        draw_block_(Block_Stack[i],COLOR_TYPE[0])





    #화면 초기화
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, PLAYING_FIELD_WIDTH * BLOCK_SIZE + 10, PLAYING_FIELD_HEIGHT * BLOCK_SIZE + 10), 5)

    # 블록 생성

    if Block_State == True:
        B_type = random.randrange(7)
        B_direction = random.randrange(4)
        B_color = block_color()
        Block_X_Position = 7
        Block_Y_INC = 1
        Block_State = False
    
    if B_direction > 3:
        B_direction -= 4

    BlockDownSpeed += 1
    if BlockDownSpeed > 1000:
        draw_block(LINE_SIZE_X + BLOCK_SIZE * Block_X_Position , LINE_SIZE_Y + BLOCK_SIZE * (Block_Y_INC), B_direction , CheckBlockTypeNum(B_type),B_color)
        Block_Y_INC += 1COLOR_TYPE[0]
        BlockDownSpeed = 0
    
    draw_block(LINE_SIZE_X + BLOCK_SIZE * Block_X_Position , LINE_SIZE_Y + BLOCK_SIZE * (Block_Y_INC), B_direction , CheckBlockTypeNum(B_type),B_color)
    

    # 화면 업데이트
    pygame.display.update()
