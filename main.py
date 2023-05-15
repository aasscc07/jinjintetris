from tkinter import *
from math import *
import pygame
# import pymysql
import socket as sock
import pickle
import ctypes


#=============================================> mysql <==========================================================#
# mysql = pymysql.connect(
#     user='asc07',
#     passwd='anchorong',
#     host='18.220.144.38',
#     db='chorong'
# )

# cursor = mysql.cursor(pymysql.cursors.DictCursor)

# mysql_command = "select score from ball_game where ID = \"admin\";"
# cursor.execute(mysql_command)
# ball_game_member_information = (str((cursor.fetchall())[0]))



class database_mysql:
    def __init__(self,member_ID):
        pass

    def join(ID):
        pass

    def select(ID):
        pass

        





# print(int(ball_game_member_information[10:int(len(ball_game_member_information)) - 1]))

# print(ball_game_member_information)

#================================================================================================================#


#=================================================> GUI <========================================================#
class member_ball_game:
    def __init__(self,ID):
        self.ID = ID
        self.PASSWD = 0
        self.join_running = True
    
    def join(self):
        
        
        self.root = Tk()
        self.root.title("anchorong")
        self.root.geometry("450x60")
        self.root.resizable(False,False)

        ID_label = Label(self.root,text="ID ")
        PASSWD_label = Label(self.root,text="PASSWD ")
        ID_label.pack()
        ID_label.place(x=0 , y=2)
        PASSWD_label.pack()
        PASSWD_label.place(x=0,y=30)
        
        exit_button = Button(self.root,text="E X I T ",command=self.EXIT)
        exit_button.pack()
        exit_button.place(x=380,y=30)
        
        login_button = Button(self.root,text="J O I N")
        login_button.pack()
        login_button.place(x=380,y=2)

        

        ID_text_box = Entry(self.root,width=40)
        PASSWD_text_box = Entry(self.root,width=40)
        ID_text_box.pack()
        ID_text_box.place(x=80,y=2)
        PASSWD_text_box.pack()
        PASSWD_text_box.place(x=80,y=30)
        self.root.mainloop()
        

    def EXIT(self):
        self.root.destroy()
    
    def join_button_command(self):
        pass

#================================================================================================================#



pygame.init()




screen_width = 480 * 1
screen_height = 720

clock = pygame.time.Clock()


#====================> console settings <====================#
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("tetris")
#============================================================#

class image_file_load:
    def __init__(self,file_address):
        self.file_address = file_address
        self.character = pygame.image.load(self.file_address)
        self.character_size = self.character.get_rect().size # ?´ë¯¸ì???˜ ?‚¬?´ì¦ˆë?? êµ¬í•´?˜¨?‹¤
        self.character_width = self.character_size[0] # ìºë¦­?„°?˜ ê°?ë¡? ?¬ê¸?
        self.character_height = self.character_size[1] # ìºë¦­?„°?˜ ?„¸ë¡? ?¬ë¦?
        self.character_x_pos = 0  # = (screen_width / 2 ) - (self.character_width / 2) # ?™”ë©? ê°?ë¡œì˜ ?¬ê¸°ì— ?•´?‹¹?•˜?Š” ê³³ì— ?œ„ì¹? (ê°?ë¡?)
        self.character_y_pos  = 0 # = screen_height - self.character_height # ?™”ë©? ?„¸ë¡? ?¬ê¸? ê°??ž¥ ?•„?ž˜?— (?„¸ë¡?)



class game_play:
    def __init__(self):
        self.running = True
        self.to_x = 0
        self.to_y = 0
        background = image_file_load("image/background.png")
        block_1 = image_file_load("image/block_1.png")
        block_1.character_y_pos = 300
        
        
        while self.running:
            dt = clock.tick(300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        exit()
                    if event.key == pygame.K_j:
                        member_ball_game("ID").join() 

                    if event.key == pygame.K_LEFT:
                        block_1.character_x_pos -= 1
                    elif event.key == pygame.K_RIGHT:
                        block_1.character_x_pos += 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0

                        
                        
            block_1.character_x_pos += self.to_x * dt / 2
            block_1.character_y_pos += self.to_y * dt / 2
            screen.blit(background.character,(background.character_x_pos,background.character_y_pos))
            screen.blit(block_1.character,(block_1.character_x_pos,block_1.character_y_pos))
            pygame.display.update()
    
    def crush_check(self):
        pass


start = game_play()