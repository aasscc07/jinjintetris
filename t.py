# -*- coding: euc-kr -*
import pygame
import sys

# Pygame 초기화
pygame.init()


screen_width = 416  # 16 * 24 + 2 * 5
screen_height = 744  # 32 * 24 + 2 * 5
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 내부 영역 설정
inner_width = 384  # 16 * 24
inner_height = 704  # 32 * 24
inner_x = (screen_width - inner_width) // 2
inner_y = (screen_height - inner_height) // 2

# 테두리 크기
border_size = 5

def check_collision(x, y, block_shape):
    for i in range(len(block_shape)):
        for j in range(len(block_shape[0])):
            if block_shape[i][j] == 1:
                block_x = inner_x + x + j * 24
                block_y = inner_y + y + i * 24

                # 벽과의 충돌 검사
                if block_x < inner_x + border_size or block_x >= inner_x + inner_width - 24 - border_size:
                    return True
                if block_y >= inner_y + inner_height - 24 - border_size:
                    return True

    return False


border_color = (255, 255, 255)
def draw_tetris_block(x, y, block_shape):
    # 블록 색상
    RandomBlockColor = (0, 255, 255)

    # 블록 그리기
    for i in range(len(block_shape)):
        for j in range(len(block_shape[0])):
            if block_shape[i][j] == 1:
                block_x = inner_x + x + j * 24
                block_y = inner_y + y + i * 24
                block_rect = pygame.Rect(block_x, block_y, 24, 24)
                pygame.draw.rect(screen, RandomBlockColor, block_rect)


    pygame.draw.rect(screen, border_color, (inner_x - 5, inner_y - 5, inner_width + 10, inner_height + 10), 5)

def move_tetris_block(dx, dy):
    global block_x, block_y
    new_x = block_x + dx
    new_y = block_y + dy
    if not check_collision(new_x, new_y, I_BLOCK):
        block_x = new_x
        block_y = new_y

# 키 입력 처리
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_tetris_block(-24, 0)  # 왼쪽으로 24px 이동
            elif event.key == pygame.K_RIGHT:
                move_tetris_block(24, 0)  # 오른쪽으로 24px 이동
            elif event.key == pygame.K_DOWN:
                move_tetris_block(0, 24)  # 아래로 24px 이동
block_x = 0  # 블록의 시작 x 좌표
block_y = 0  # 블록의 시작 y 좌표
# 게임 루프
while True:
    handle_input()

    # 화면 클리어
    screen.fill((0, 0, 0))

    # 테트리스 블록 그리기 (예시로 I 블록 사용)
    I_BLOCK = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    if check_collision(block_x, block_y, I_BLOCK):
        print("블록이 벽에 닿았습니다.")

    # 테트리스 블록 그리기
    draw_tetris_block(block_x, block_y, I_BLOCK)

    # 화면 업데이트
    pygame.display.update()
