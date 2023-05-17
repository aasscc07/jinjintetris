PLAYING_FIELD_WIDTH = 16
PLAYING_FIELD_HEIGHT = 32

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

Block_EXIST = []
for i in range(PLAYING_FIELD_HEIGHT):
    Block_EXIST.append([])
    for j in range(PLAYING_FIELD_WIDTH):
        Block_EXIST[i].append([])
        Block_EXIST[i][j] = 0
    print(Block_EXIST[i])
class BlockInArray:
    def __init__(self,x,y,block,Direction):
        self.x = x
        self.y = y
        self.Direction = Direction
        self.block = block

block1 = BlockInArray(0,2,I_BLOCK,0)

for i in range(PLAYING_FIELD_HEIGHT):
    for j in range(PLAYING_FIELD_WIDTH):
        for y_ in range(4):
            for x_ in range(4):
                # block1.block[y_][x_]
                if i == (block1.x + x_) & j == (block1.y + y_):
                    Block_EXIST[i][j] += block1.block[x_][y_]


# print(Block_EXIST)