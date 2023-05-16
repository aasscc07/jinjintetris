
import pygame
import sys

# 창 만들기
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')
PLAYING_FIELD_WIDTH = 10
PLAYING_FIELD_HEIGHT = 20
BLOCK_SIZE = 30
playing_field = [[0] * PLAYING_FIELD_WIDTH for _ in range(PLAYING_FIELD_HEIGHT)]

shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]]
]

# 테트리스 블럭 타입

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




# I_BLOCK 그리기 함수

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_O_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range():
        for j in range():
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)

def draw_I_block (x, y, n)
    #블록 색상 
    color = (0, 255, 255)
    #블록 입력
    for i in range(4):
        for j in range(4):
            if I_block[n][x][y]:
                rect = pygame.rect(x+j*20, y+i*20, 20, 20)






)


# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면 클리어
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (0, 0, PLAYING_FIELD_WIDTH * BLOCK_SIZE, PLAYING_FIELD_HEIGHT * BLOCK_SIZE), 5)

    # I_BLOCK 그리기
    draw_I_block(100, 100, 0)



    # 화면 업데이트
    pygame.display.update()
