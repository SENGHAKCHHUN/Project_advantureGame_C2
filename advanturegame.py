#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
# from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800

#============================ GLOBAL ============================
score=0


#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)


#============================ IMAGES ============================
start_img = PhotoImage(file="Images/start-button.png")
help_btn = PhotoImage(file="Images/help-button.png")
exit_img = PhotoImage(file="Images/exit-button.png")
home_bg = PhotoImage(file='Images/bg-defualt.png')
level_img = PhotoImage(file="Images/level.png")
winter_bg = PhotoImage(file="Images/winter_bg.png")
summer_bg = PhotoImage(file="Images/summer_bg.png")
back_img = PhotoImage(file="Images/back.png")
help_board = PhotoImage(file="Images/help.png")
grass_img = PhotoImage(file="Images/grass.png",)
stone_img = PhotoImage(file="Images/stone.png")
coin_img = PhotoImage(file="Images/coin.png")
door_img = PhotoImage(file="Images/door.png")
key_img = PhotoImage(file="Images/key.png")
flower_img = PhotoImage(file="Images/flower.png")
money_img = PhotoImage(file="Images/money.png")
thorn_img = PhotoImage(file="Images/thorn.png")
dimond_img = PhotoImage(file="Images/dimond.png")
monster_img = PhotoImage(file="Images/monster.png")
#============================= BACKGROUND =====================




#=========================== ALL LEVELS =======================

def level1(event):
    canvas.delete("all")
    # =============   GRASS IMAGES =========
    canvas.create_image(1, 0, image=summer_bg, anchor="nw")
    canvas.create_image(320,150, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(450,250, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(170,300, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(700,350, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,400, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(730,200, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1000,270, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(150,470, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(350,600, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(500,500, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1000,600, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(100,620, image = grass_img, anchor="nw", tags = "platform")
    # ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(380,100, image = door_img, anchor = "nw")
    canvas.create_image(1120,250, image = key_img, anchor = "nw")
    # ==================  STONE IMAGES ===============
    canvas.create_image(650,600, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(450,400, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(800,550, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(950,450, image = stone_img, anchor="nw", tags = "platform")
    # ==================  FLOWERS ===============
    canvas.create_image(950,200, image = flower_img, anchor = "nw")
    canvas.create_image(900,520, image = flower_img, anchor = "nw")
    canvas.create_image(100,390, image = flower_img, anchor = "nw")

    # ==================  COINS, DIMOND, THORN, MONEY ===============

    canvas.create_image(240,280, image = money_img, anchor = 'nw')
    canvas.create_image(730,330, image = money_img, anchor = "nw")

    canvas.create_image(470,350, image = dimond_img, anchor = 'nw')
    canvas.create_image(820,500, image = dimond_img, anchor = 'nw')

    canvas.create_image(410,600, image = coin_img, anchor = 'nw')
    canvas.create_image(980,420, image = coin_img, anchor = 'nw')
    canvas.create_image(1170,380, image = coin_img, anchor = 'nw')


    canvas.create_image(270,450, image =monster_img, anchor = 'nw')
    canvas.create_image(510,240, image =monster_img, anchor = 'nw')
    canvas.create_image(800,340, image =monster_img, anchor = 'nw')

    canvas.create_image(770,130, image =thorn_img, anchor = 'nw')
    canvas.create_image(550,430, image =thorn_img, anchor = 'nw')
    canvas.create_image(1060,530, image =thorn_img, anchor = 'nw')

    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

def level2(event):
    canvas.create_image(1, 0, image=summer_bg, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

def level3(event):
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")




# ======================= HOME_PAGE =============================
def home():
    canvas.create_image(0,0, image=home_bg, anchor="nw")
    canvas.create_image(630, 300, image=start_img, anchor="nw", tags="start")
    canvas.create_image(630, 370, image=help_btn, anchor="nw", tags="help")
    canvas.create_image(630, 440, image=exit_img, anchor="nw", tags="exit")

# ======================= BACK TO LEVELS PAGE =============================
def backTolevel(event):
    allLevels()

def help(event):
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
    canvas.create_image(380,100, image = help_board, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
def start(event):
    allLevels()
def backHome(event):
    home()

#============================ EXIT ============================
def exit(event):
    window.destroy()


#============================ ALL LEVELS BUTTON ============================
def allLevels():
    
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
                            #==== LEVEL 1 =====
    canvas.create_image(620, 300, image=level_img, anchor="nw", tags="level1")
    canvas.create_text(695, 330, text="Level 1", font=("arsenal", 20, "bold"), fill="white",tags="level1")
                            #==== LEVEL 2 =====
    canvas.create_image(620, 370, image=level_img, anchor="nw", tags="level2")
    canvas.create_text(695, 400, text="Level 2", font=("arsenal", 23, "bold"), fill="white",tags="level2")
                            #==== LEVEL 3 =====
    canvas.create_image(620, 440, image=level_img, anchor="nw", tags="level3")
    canvas.create_text(695, 470, text="Level 3", font=("arsenal", 23, "bold"), fill="white",tags="level3")
                            #==== BACK BUTTON=====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    
#=========================== FUNCTIONS MOVE PLAYER =======================
# MOVE RIGHT
def moveRight(event):
    pass
    
# MOVE LEFT
def moveLeft(event):
    pass
    
# MOVE UP
def moveUp(event):
    pass

# MOVE DOWN
def moveDown(event):
    pass 



#============================ WIN & LOSE ============================


#============================ KEY EVENT ============================
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("help","<Button-1>",help)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
canvas.tag_bind("back_all_levels","<Button-1>",backTolevel)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)
#========================= REMOTES =================


home()

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()