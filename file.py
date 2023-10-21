# import tkinter as tk

# def find_overlap():
# overlapping_items = canvas.find_overlapping(50, 50, 300, 300)
# print("Overlapping items:", overlapping_items)

# root = tk.Tk()
# canvas = tk.Canvas(root, width=300, height=300)
# canvas.pack()

# # Create some items on the canvas
# rect2 = canvas.create_rectangle(50, 50, 100, 100, fill='blue')
# rect3 = canvas.create_rectangle(200, 200, 250, 250, fill='green')
# rect1 = canvas.create_rectangle(100, 100, 150, 150, fill='red')

# # Call find_overlap() to find items overlapping with the rectangle
# find_overlap()

# root.mainloop()
#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from typing import Self
# from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7
TIMED_LOOP = 6

#============================ VARIABLES ============================

keyPressed = []

#============================ GLOBAL ============================
score=0


#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)

start_img = PhotoImage(file="Images/start-button.png")
help_btn = PhotoImage(file="Images/help-button.png")
exit_img = PhotoImage(file="Images/exit-button.png")
home_bg = PhotoImage(file='Images/bg-defualt.png')
level_img = PhotoImage(file="Images/level.png")
winter_bg = PhotoImage(file="Images/summer1.png")
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
level3_bg = PhotoImage(file="Images/level3_bg.png")
player_img = PhotoImage(file="Images/player.png")


canvas.create_image(1, 0, image=summer_bg, anchor="nw")
canvas.create_image(300,180, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(430,280, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(150,330, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(680,380, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(990,430, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(710,230, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(980,300, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(130,500, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(330,630, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(480,530, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(980,630, image = grass_img, anchor="nw", tags = "platform")
canvas.create_image(10,650, image = grass_img, anchor="nw", tags = "platform")
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

# _______ MONEY IMAGES _________
canvas.create_image(240,280, image = money_img, anchor = 'nw')
canvas.create_image(730,330, image = money_img, anchor = "nw")

# _______ DIMOND IMAGES _________
canvas.create_image(470,350, image = dimond_img, anchor = 'nw')
canvas.create_image(820,500, image = dimond_img, anchor = 'nw')

# _______ COIN IMAGES _________
canvas.create_image(410,600, image = coin_img, anchor = 'nw')
canvas.create_image(980,420, image = coin_img, anchor = 'nw')
canvas.create_image(1170,380, image = coin_img, anchor = 'nw')

# _______ MONSTER IMAGES _________
canvas.create_image(270,450, image =monster_img, anchor = 'nw')
canvas.create_image(510,240, image =monster_img, anchor = 'nw')
canvas.create_image(800,340, image =monster_img, anchor = 'nw')

# _______ THORN IMAGES _________
canvas.create_image(770,130, image =thorn_img, anchor = 'nw')
canvas.create_image(550,430, image =thorn_img, anchor = 'nw')
canvas.create_image(1060,530, image =thorn_img, anchor = 'nw')

# ==================  PLAYER ===============
player = canvas.create_image(10,150, image =player_img, anchor="nw")

def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    # print(coord)
    platforms = canvas.find_withtag("platform")
    # if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
    #     return False
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ player_img.width(), coord[1] + player_img.height())
    print(overlap)
    for platform in platforms:
        if platform in overlap:
            return False
    return True
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) >= 1:
            move()
            
def move():
    global player
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
            
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement():
            canvas.move(player, x, 0)
        window.after(TIMED_LOOP, move)
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)



#========================= REMOTES =================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

gravity()

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()