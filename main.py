from tkinter import *
import random
from tkinter import Button

window = Tk()
window.title("Rock, Paper, Scissor")
window.geometry("400x400")
window.resizable(False,False)

Label(text = "Rock Paper Scissor", fg = "Blue",  font = "Times 20 italic").pack(anchor = N)

match_result = ""
player_score = 0
computer_score = 0

computer_value = ["Rock", "Paper", "Scissor"]
def isrock():
    c_v = random.choice(computer_value)
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Computer Wins"
        global computer_score
        computer_score += 1
    else:
        match_result = "Player Wins"
        global player_score
        player_score += 1
    l4.config(text = match_result)
    player.config(text = "Rock")
    computer.config(text = c_v)
    score_player.config(text = player_score)
    score_computer.config(text = computer_score)
    button_disable()

def ispaper():
    c_v = random.choice(computer_value)
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Wins"
        global computer_score
        computer_score += 1
    else:
        match_result = "Player Wins"
        global player_score
        player_score += 1
    l4.config(text=match_result)
    player.config(text="Paper")
    computer.config(text=c_v)
    score_player.config(text=player_score)
    score_computer.config(text=computer_score)
    button_disable()

def isscissor():
    c_v = random.choice(computer_value)
    if c_v == "Scissor":
        match_result = "Match Draw"
    elif c_v == "Rock":
        match_result = "Computer Wins"
        global computer_score
        computer_score += 1
    else:
        match_result = "Player Wins"
        global player_score
        player_score += 1
    l4.config(text=match_result)
    player.config(text="Scissor")
    computer.config(text=c_v)
    score_player.config(text=player_score)
    score_computer.config(text=computer_score)
    button_disable()

def reset_game():
    rock["state"] = ACTIVE
    paper["state"] = ACTIVE
    scissor["state"] = ACTIVE
    player.config(text = "Player              ")
    computer.config(text = "Computer")
    l4.config(text = "")

def button_disable():
    rock["state"] = DISABLED
    paper["state"] = DISABLED
    scissor["state"] = DISABLED

def reset_score():
    global player_score
    global computer_score
    player_score = 0
    computer_score = 0
    score_player.config(text=player_score)
    score_computer.config(text=computer_score)
'''
Player Labels
'''
score_player = Label(window,
           text = "0",
           font = "normal 20 bold",
           bg = "grey",
           width = 2 ,
           borderwidth = 3,
           relief = "solid")
score_player.place(x= 90, y = 50)

score_computer = Label(window,
           text = "0",
           font = "normal 20 bold",
           bg = "grey",
           width = 2 ,
           borderwidth = 3,
           relief = "solid")
score_computer.place(x= 265, y = 50)

player = Label(text= "Player", font = "Times 12 bold")
player.place(x = 90, y = 100)

vs = Label(text= "VS", font = "Times 12 bold")
vs.place(x = 185, y = 100)

computer = Label(text= "Computer", font = "Times 12 bold")
computer.place(x= 260, y = 100)

l4 = Label(window,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 3,
           relief = "solid")
l4.pack(pady = 100)

rock = Button(window, text = "Rock", font = "20", command = lambda :isrock())
rock.place(x= 110, y = 200)

paper = Button(window, text = "Paper", font = "20", command = lambda :ispaper())
paper.place(x= 170, y = 200)

scissor = Button(window, text = "Scissor", font = "20", command = lambda :isscissor())
scissor.place(x= 240, y = 200)

resetgame = Button(window, text = "Reset Game", font = "20", command = lambda :reset_game())
resetgame.place(x= 150, y = 250)

resetscore = Button(window, text = "Reset Score", font = "20", command = lambda :reset_score())
resetscore.place(x=150, y = 350)
''' 
'''
window.mainloop()