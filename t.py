# -*- coding: euc-kr -*
import pygame
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# 파이게임 초기화
pygame.init()

# 게임 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 500
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("테트리스")

# 색상 정의 (RGB)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# 테트리스 블록 색상 매핑
COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, ORANGE]




# 테트리스 블록 모양 정의
SHAPES = [
    np.array([[1, 1, 1, 1]]),
    np.array([[1, 1, 1], [1, 0, 0]]),
    np.array([[1, 1, 1], [0, 0, 1]]),
    np.array([[1, 1, 0], [0, 1, 1]]),
    np.array([[0, 1, 1], [1, 1, 0]]),
    np.array([[1, 1], [1, 1]]),
    np.array([[1, 1, 1], [0, 1, 0]])
]

# 테트리스 게임 환경
class TetrisEnv:
    def __init__(self):
        self.grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)
        self.current_piece = None
        self.current_x, self.current_y = 0, 0
        self.score = 0
        self.game_over = False
        self.spawn_piece()

    def spawn_piece(self):
        self.current_piece = np.random.choice(SHAPES)
        self.current_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0

    # def is_collision(self, piece, x, y):
    #     for i in range(len(piece)):
    #         for j in range(len(piece[0])):
    #             if piece[i][j] and self.grid[x + i][y + j]:
    #                 return True
    #     return False
    def is_collision(self, piece, x, y):
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j]:
                    new_x, new_y = x + i, y + j
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
                        return True
                    if self.grid[new_x][new_y]:
                        return True
        return False


    def rotate_piece(self, piece):
        return np.rot90(piece)

    def drop_piece(self):
        while not self.is_collision(self.current_piece, self.current_x, self.current_y + 1):
            self.current_y += 1
        self.place_piece()

    def place_piece(self):
        for i in range(len(self.current_piece)):
            for j in range(len(self.current_piece[0])):
                if self.current_piece[i][j]:
                    self.grid[self.current_x + i][self.current_y + j] = 1

        self.check_lines()
        self.spawn_piece()

        if self.is_collision(self.current_piece, self.current_x, self.current_y):
            self.game_over = True

    def check_lines(self):
        full_lines = [i for i, row in enumerate(self.grid) if all(row)]
        for line in full_lines:
            self.grid = np.delete(self.grid, line, axis=0)
            self.grid = np.insert(self.grid, 0, np.zeros(GRID_WIDTH), axis=0)
        self.score += len(full_lines)

    def move(self, direction):
        new_x = self.current_x + direction
        if not self.is_collision(self.current_piece, new_x, self.current_y):
            self.current_x = new_x

    def step(self, action):
        if action == 0:  # 왼쪽으로 이동
            self.move(-1)
        elif action == 1:  # 오른쪽으로 이동
            self.move(1)
        elif action == 2:  # 회전
            rotated_piece = self.rotate_piece(self.current_piece)
            if not self.is_collision(rotated_piece, self.current_x, self.current_y):
                self.current_piece = rotated_piece
        elif action == 3:  # 빠르게 내리기
            self.drop_piece()

        self.current_y += 1

        if self.is_collision(self.current_piece, self.current_x, self.current_y):
            self.current_y -= 1
            self.place_piece()

        return self.grid, self.score, self.game_over

# DQN 에이전트
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # 할인율
        self.epsilon = 1.0  # 탐색 확률
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = self.build_model()

    def build_model(self):  
        model = tf.keras.Sequential()
        model.add(layers.Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(24, activation='relu'))
        model.add(layers.Dense(self.action_size, activation='linear'))
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)  # 수정된 부분
        model.compile(loss='mse', optimizer=optimizer)
        return model
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return
        import random
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# 게임 루프 실행
env = TetrisEnv()
state_size = GRID_WIDTH * GRID_HEIGHT
action_size = 4  # 4개의 액션 (왼쪽으로 이동, 오른쪽으로 이동, 회전, 빠르게 내리기)

agent = DQNAgent(state_size, action_size)

running = True
batch_size = 32


def draw_block(screen, color, row, col):
    pygame.draw.rect(screen, color, pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

def draw_tetris_board(screen, grid):
    for row in range(GRID_WIDTH):
        for col in range(GRID_HEIGHT):
            if grid[row][col]:
                draw_block(screen, COLORS[grid[row][col]], row, col)

def draw_game(screen, grid):
    screen.fill(BLACK)
    draw_grid(screen)
    draw_tetris_board(screen, grid)


while running:
    state = env.grid.reshape(1, -1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = agent.act(state)
    next_state, reward, done = env.step(action)
    next_state = next_state.reshape(1, -1)
    agent.remember(state, action, reward, next_state, done)
    state = next_state

    if done:
        print(f"Score: {env.score}")
        env = TetrisEnv()

    if len(agent.memory) > batch_size:
        agent.replay(batch_size)

    draw_game(screen, env.grid)
    pygame.display.flip()

pygame.quit()
