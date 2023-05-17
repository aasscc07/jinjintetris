# -*- coding: euc-kr -*
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
    
# PLAYING_FIELD_WIDTH = 16
# PLAYING_FIELD_HEIGHT = 32
# BLOCK_SIZE = 24
# playing_field = [[0] * PLAYING_FIELD_WIDTH for _ in range(PLAYING_FIELD_HEIGHT)]
global screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

C_RED = (255,0,0)
C_MINT = (9,247,164)
C_P = (176,18,237)
C_B = (0,128,255)

COLOR_TYPE = [C_RED,C_MINT,C_P,C_B]
BLOCK_TYPE_LIST = [I_BLOCK,L1_BLOCK,L2_BLOCK,T_BLOCK,O_BLOCK,Z1_BLOCK,Z2_BLOCK]

MainCmArr = []

def MainCmArrSetting():
    for y in range(32 + 2):
        MainCmArr.append([])
        for x in range(16 + 2):
            MainCmArr[y].append(0)
            if x == 0:
                MainCmArr[y][x] = 1
            if x == 17:
                MainCmArr[y][x] = 1

            if y == 0:
                MainCmArr[y][x] = 1
            if y == 33:
                MainCmArr[y][x] = 1
        print(MainCmArr[y])

MainCmArrSetting()
    


#Good Kim
def RandomBlockColor():
    B_color = random.randrange(4)
    color_ = [C_RED,C_MINT,C_P,C_B]  
    for i in range(len(color_)):
         if B_color == i:
            return color_[i]
         
def CheckBlockTypeAsNum(BlockTypeNum):
    v1_ = [I_BLOCK,L1_BLOCK,L2_BLOCK,T_BLOCK,O_BLOCK,Z1_BLOCK,Z2_BLOCK] # 7개 요소
    for i in range(len(v1_)):
         if BlockTypeNum == i:
            return v1_[i]         



def Log(Msg : str):
    print(f"LOG : {Msg}")


def PyGameInit(WIDTH : int,HEIGHT : int,Title : str):
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(Title)

class PlayGround:
    def __init__(self,FIELD_WIDTH : int,FIELD_HEIGHT : int,BLOCK_SIZE : int,LineSize):
        self.FIELD_WIDTH = FIELD_WIDTH
        self.FIELD_HEIGHT = FIELD_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.LineSize = LineSize
        self.playing_field = [[0] * self.FIELD_WIDTH for _ in range(self.FIELD_HEIGHT)]
        
    def Draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, self.FIELD_WIDTH * self.BLOCK_SIZE + self.LineSize * 2, self.FIELD_HEIGHT * self.BLOCK_SIZE + self.LineSize * 2), self.LineSize)

pgd = PlayGround(16,32,24,5)

class POS:
    def __init__(self,x : int,y : int):
        self.x = x
        self.y = y
    
    def __add__(self,pos):
        self.x += pos.x
        self.y += pos.y

    def __sub__(self,pos):
        self.x -= pos.x
        self.y -= pos.y
    


class Block:
    def __init__(self,BlockType,Pos : POS,Color):
        self.Block = BlockType
        self.Pos = Pos
        self.CurrentDirt = int(0)
        self.Color = Color

    def Draw(self):
        for i in range(len(self.Block[self.CurrentDirt])):
            for j in range(len(self.Block[self.CurrentDirt][i])):
                if self.Block[self.CurrentDirt][i][j]:
                    rect_ = pygame.Rect(pgd.LineSize + self.Pos.x + ((self.Pos.x + j) * pgd.BLOCK_SIZE), pgd.LineSize + ((self.Pos.y + i) * pgd.BLOCK_SIZE), pgd.BLOCK_SIZE, pgd.BLOCK_SIZE)
                    pygame.draw.rect(screen, self.Color, rect_)

    def CheckCollisionWithBlocks(self,blocklist):
        for i in range(len(self.Block)):
            for j in range(len(self.Block[i])):
                if self.Block[i][j] == 1:
                    self.Pos.x = pgd.LineSize + j #Relatively Position
                    self.Pos.y = pgd.LineSize + i # //

                    for block in blocklist:
                        if block.Pos.x == self.Pos.x and block.Pos.y == self.Pos.y:
                            return True
        return False
    
    def Check_Crush(self):
        for i in range(4):
            for j in range(4):
                if self.Block[i][j] == 1 and MainCmArr[self.Pos.y + i][self.Pos.y + j] > 0:
                    return False
        
        return True
    



class BlockList:
    def __init__(self):
        self.BlockList = []

    def AddBlock(self,block : Block):
        self.BlockList.append(block)

    def DrawOne(self,ListNum : int):
        if len(self.BlockList) >= ListNum:
            self.BlockList[ListNum].Draw()
        else:
            Log(f"BlockList[{ListNum}] is not exist")

    def DrawAll(self):
        for i in range(len(self.BlockList)):
            self.BlockList[i].Draw()

    def DownOneAll(self):
        for i in range(len(self.BlockList)):
            self.BlockList[i].Pos.y -= 1

def Check_Crush(bx,by,b_rotation,block : Block):
    block.CurrentDirt = b_rotation
    for i in range(len(block.Block[block.CurrentDirt])):
        for j in range(len(block.Block[block.CurrentDirt][i])):
            if block.Block[block.CurrentDirt][i][j] == 1 and MainCmArr[by + i][bx + j] > 0:
                return False
    
    return True

#==============================< Various List >============================#
Block_State = True
B_type = 0
B_direction = 0

BlockDownSpeed = 0
#==========================================================================#

Block_Stack = []

#Main Loop
while True:
    if Block_State == True:
        NewBlock = Block(CheckBlockTypeAsNum(random.randrange(7)), POS(7,1), RandomBlockColor())
        NewBlock.CurrentDirt = int(random.randrange(4))
        Block_State = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if Check_Crush(NewBlock.Pos.x + 4,NewBlock.Pos.y,NewBlock.CurrentDirt,NewBlock) == True:      
                        NewBlock.Pos.x -= 1
                        
                elif event.key == pygame.K_RIGHT:
                    if Check_Crush(NewBlock.Pos.x + 2,NewBlock.Pos.y,NewBlock.CurrentDirt,NewBlock) == True:  
                        NewBlock.Pos.x += 1

                elif event.key == pygame.K_DOWN:
                    if Check_Crush(NewBlock.Pos.x,NewBlock.Pos.y + 1,NewBlock.CurrentDirt,NewBlock) == True:  
                        NewBlock.Pos.y += 1
                        
                elif event.key == pygame.K_r:
                    # if Check_Crush(NewBlock.Pos.x,NewBlock.Pos.y,(NewBlock.CurrentDirt + 1) % 4,NewBlock) == True:
                    #     NewBlock.Pos.y -= 1
                    NewBlock.CurrentDirt += 1
                    
                if event.key == pygame.K_g:
                    Block_State = True
                
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

    if NewBlock.Pos.x < 0:
        NewBlock.Pos.x = 0    

    if NewBlock.Pos.y > 29:
        NewBlock.Pos.y = 29
        Block_State = True





    #화면 초기화
    screen.fill((0, 0, 0))



    pgd.Draw()


    
    if NewBlock.CurrentDirt > 3:
        NewBlock.CurrentDirt -= 4

    BlockDownSpeed += 1
    if BlockDownSpeed > 500:
        NewBlock.Draw()
        NewBlock.Pos.y += 1
        BlockDownSpeed = 0
    

    NewBlock.Draw()


    # 화면 업데이트
    pygame.display.update()

    
