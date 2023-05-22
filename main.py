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
WINDOW_HEIGHT = 900
    
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
C_WALL = (255,255,255)
C_BLACK = (0,0,0)

COLOR_TYPE = [C_RED,C_MINT,C_P,C_B]
BLOCK_TYPE_LIST = [I_BLOCK,L1_BLOCK,L2_BLOCK,T_BLOCK,O_BLOCK,Z1_BLOCK,Z2_BLOCK]

MainCmArr = []

def MainCmArrSetting(width,height):
    for y in range(height + 2 + 0):
        MainCmArr.append([])
        for x in range(width + 2):
            MainCmArr[y].append([0,C_BLACK])
            if x <= 0:
                MainCmArr[y][x][0] = 1
            if x == width + 1:
                MainCmArr[y][x][0] = 1

            if y <= 0:
                MainCmArr[y][x][0] = 1
            if y == height + 1 or y == height + 1:
                MainCmArr[y][x][0] = 1
        print(MainCmArr[y])

def PrintMCA():
    for i in range(len(MainCmArr)):
        print(MainCmArr[i])

    


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
        self.BackGroundBlock1 = pygame.image.load("PlayGroundBlock1.png")

        
    def Draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, self.FIELD_WIDTH * self.BLOCK_SIZE + self.LineSize * 2, self.FIELD_HEIGHT * self.BLOCK_SIZE + self.LineSize * 2), self.LineSize)
        # for i in range(self.FIELD_HEIGHT + 2):
        #     screen.blit(self.BackGroundBlock1,(0,i * self.BLOCK_SIZE))
        #     screen.blit(self.BackGroundBlock1,((self.FIELD_WIDTH + 1) * self.BLOCK_SIZE,i * self.BLOCK_SIZE))

        # for j in range(self.FIELD_WIDTH + 2):
        #     screen.blit(self.BackGroundBlock1,(j * self.BLOCK_SIZE,0))
        #     screen.blit(self.BackGroundBlock1,(j * self.BLOCK_SIZE,(self.FIELD_HEIGHT + 1) * self.BLOCK_SIZE))


pgd = PlayGround(16,32,24,24)
MainCmArrSetting(pgd.FIELD_WIDTH,pgd.FIELD_HEIGHT)

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
        self.BlockFile = pygame.image.load("PlayGroundBlock1.png")

    def Draw(self):
        for i in range(len(self.Block[self.CurrentDirt])):
            for j in range(len(self.Block[self.CurrentDirt][i])):
                if self.Block[self.CurrentDirt][i][j]:
                    rect_ = pygame.Rect(pgd.LineSize + ((self.Pos.x + j) * pgd.BLOCK_SIZE), pgd.LineSize + ((self.Pos.y + i) * pgd.BLOCK_SIZE), pgd.BLOCK_SIZE, pgd.BLOCK_SIZE)
                    pygame.draw.rect(screen, self.Color, rect_)
                    # screen.blit(self.BlockFile,(pgd.LineSize + self.Pos.x + ((self.Pos.x + j) * pgd.BLOCK_SIZE), pgd.LineSize + ((self.Pos.y + i) * pgd.BLOCK_SIZE)))

    def Check_Crush(self):
        for y in range(len(self.Block[self.CurrentDirt])):
            for x in range(len(self.Block[self.CurrentDirt][y])):
                if (MainCmArr[self.Pos.y + y + 1][self.Pos.x + x + 1][0] + self.Block[self.CurrentDirt][y][x]) == 2:
                    return 1
                
                if (MainCmArr[self.Pos.y + y + 1][self.Pos.x + x + 1][0] + self.Block[self.CurrentDirt][y][x]) == 3:
                    return 2
                
        return 0
    
    def UpdateMainCmArr(self):
        for y in range(len(self.Block[self.CurrentDirt])):
            for x in range(len(self.Block[self.CurrentDirt][y])):
                if self.Block[self.CurrentDirt][y][x] == 1:
                    MainCmArr[self.Pos.y + y + 1][self.Pos.x + x + 1][0] = 1
                
    
    # def UpdateMainCmArr():

def DrawBlocks():
    for y in range(len(MainCmArr)):
        for x in range(len(MainCmArr[y])):
            if (MainCmArr[y][x][0] == 1) and (y != 0) and (x != 0) and (y != len(MainCmArr) - 1) and (x != len(MainCmArr[y]) - 1):
                tblock = pygame.Rect(pgd.LineSize + (x * pgd.BLOCK_SIZE), pgd.LineSize + (y * pgd.BLOCK_SIZE), pgd.BLOCK_SIZE, pgd.BLOCK_SIZE)
                pygame.draw.rect(screen,MainCmArr[y][x][1],tblock)

    



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

def OneLineIsCheck():
    for y in range(len(MainCmArr)):
        for x in range(len(MainCmArr[y])):
            pass




#==============================< Various List >============================#
Block_State = True
B_type = 0
B_direction = 0

BlockDownSpeed = 0
#==========================================================================#

BlockChain = BlockList()

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
                    NewBlock.Pos.x -= 1
                    if NewBlock.Check_Crush() == 1:
                        NewBlock.Pos.x += 1
                    elif NewBlock.Check_Crush() == 2:
                        NewBlock.Pos.x += 1
                        
                elif event.key == pygame.K_RIGHT:
                    NewBlock.Pos.x += 1
                    if NewBlock.Check_Crush() == 1:
                        NewBlock.Pos.x -= 1
                    elif NewBlock.Check_Crush() == 2:
                        NewBlock.Pos.x -= 1

                elif event.key == pygame.K_DOWN:
                    NewBlock.Pos.y += 1
                    if NewBlock.Check_Crush() == 1:
                        NewBlock.Pos.y -= 1
                    elif NewBlock.Check_Crush() == 2:
                        NewBlock.Pos.y -= 1
                        
                elif event.key == pygame.K_r:
                    NewBlock.CurrentDirt += 1
                    if NewBlock.CurrentDirt > 3:
                        NewBlock.CurrentDirt -= 4
                    if NewBlock.Check_Crush() == 1:
                        NewBlock.CurrentDirt -= 1
                    
                    
                if event.key == pygame.K_g:
                    Block_State = True
                
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()

    if NewBlock.CurrentDirt > 3:
        NewBlock.CurrentDirt -= 4

    if NewBlock.Check_Crush() == True:
        NewBlock.Pos.y -= 1
        BlockChain.AddBlock(NewBlock)
        NewBlock.UpdateMainCmArr()
        Block_State = True
        PrintMCA()

    # if OneLineIsComplete():
    #     pass
    temp = 0

    for i in range(len(MainCmArr)):
        for j in range(len(MainCmArr[i])):
            if MainCmArr[i][j][0] == 1:
                temp += 1
        if temp == 16:
            # lineBreak
            for j in range(len(MainCmArr[i])):
                if j != (0 and len(MainCmArr[i] - 1)):
                    MainCmArr[i][j][0] = 0
            for j in range(len(MainCmArr)):
                for k in range(len(MainCmArr[j])):
                    if j <= i:
                        temp_ = MainCmArr[j][k]
                        MainCmArr[j][k] = [0,(0,0,0)]
                        if len(MainCmArr) - 1 != i:
                            MainCmArr[j + 1][k] = temp_
    


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
    
    # BlockChain.UpdateMainCmArr()
    # DrawBlocks()
    NewBlock.Draw()
    DrawBlocks()
    # BlockChain.DrawAll()
    # NewBlock.Draw()
    


    # 화면 업데이트
    pygame.display.update()

    