from time import sleep as wait
from random import randint as rand
from random import choice as choose

# improvised accurate roulette version
# instead of just using rand(0,5)==0
bullets=[0,0,0,0,0,1]
choices=["rock","paper","scissors"]
bullet=0     # special value
round=0      # special value
player_wins=False
def roll():
    bullets=[0 for _ in range(6)]
    bullets[rand(0,len(bullets)-1)]=1
    bullet=0
    
def fire():
    global bullet
    if bullets[bullet]==1:
        return True
    else:
        bullet+=1
        return False

### checks if the response exists from the choices array.
def find_exist(response:str):
    return any(choice in response for choice in choices)

### checks if the user inputted the double str responses correctly.
def is_valid(user_response:str):
    if " " in user_response:
        user_choices=user_response.split(" ")
        if find_exist(user_choices[0]) and find_exist(user_choices[1]):
            return True
    return False

### rock_paper_scissors_victor decider for player vs. bot
### True (player wins), False (player loses)
def rps_victor(
        player_choice:str,
        bot_choice:str
        ):
    match player_choice:
        case "rock": return bot_choice==choices[1]
        case "paper": return bot_choice==choices[2]
        case "scissors": return bot_choice==choices[0]
    return

# ROCK, PAPER, SCISSORS, MINUS ONE
def minus_one():
    resp=""" "rock", "paper", "scissors"
Three choices for each box:
[____]  [____]
choose wisely.\n\n[Player]: """
    while True:
        user_response=input(resp)
        if is_valid(user_response):
            break
        else:
            resp="Try again.\n\n[Player]: "
    bot_response=f"{choose(choices)} {choose(choices)}"
    print(f"[Bot]: {bot_response}")
    user_choices=user_response.split(" ")
    bot_choices=bot_response.split(" ")
    result=decide_loser(user_choices,bot_choices)
    if result=="Tie":
        print("The result is a tie. Try again.")
        minus_one()
    elif result=="Player":
        print("The bot wins this round.\nYou will decide this outcome.")
        roulette(True)
    else:
        print("The player wins this round.\nThe bot decides this outcome.")
        roulette(False)

### player decides which of the two choices to choose
### against the bot's choices simultaneously.
def decide_loser(
        user_choices:list[str],
        bot_choices:list[str]
        ):
    resp="Choose 1 or 2.\n\n[Player]: "
    wait(2)
    while True:
        user_response=input(resp)
        if user_response=="1" or user_response=="2":
            number=int(user_response)-1
            break
        else:
            resp="Try again.\n\n[Player]: "
    player_choice=user_choices[number]
    print(f"Player pulled ({player_choice}).")
    for bot_option in bot_choices:
        match player_choice:
            case "rock" if bot_option==choices[1]: bot_choice=choices[1] #paper
            case "paper" if bot_option==choices[2]: bot_choice=choices[2] #scissors
            case "scissors" if bot_option==choices[0]: bot_choice=choices[0] #rock
            case _: bot_choice=bot_choices[rand(0,1)] #to make things fair
    if (rand(1,10)==1):
        bot_choice=bot_choices[rand(0,1)] #to make things fair
    print(f"Bot pulled ({bot_choice}).")
    wait(2)
    if player_choice==bot_choice: return "Tie"
    is_winner=rps_victor(player_choice,bot_choice)
    if is_winner==True: return "Player"
    else: return "Bot"

### Bot's bersion of russian roulette
### atleast they know what's aware.
def bot_decision():
    print("Bot is making a decision.")
    is_near=(bullets[bullet+1]==1)
    if is_near:
        print("Bot has re-rolled.\nThe bullet is in a different chamber.")
        roll()
        wait(2)
    print("Bot has fired the gun.")
    wait(2)
    if fire()==True:
        victory()
    
### after ROCK, PAPER, SCISSORS, MINUS ONE
### russian roulette is 1/6 chance the player would lose.
### player_turn:true  = player's turn
### player_turn:false = bot's turn
def roulette(player_turn:bool):
    # if fire()==True:
    #     print("GAME OVER")
    # else:
    #     print("Player is [SAFE]")
    #     wait(2)
    wait(2)
    if player_turn:
        chance=1/(len(bullets)-bullet)
        print(f"Player has a {chance*100}% chance they will lose.")
        resp="""Choose wisely. "roll" "fire"\n\n["roll"|"fire"]: """
        while True:
            user_response=input(resp)
            match user_response:
                case "roll":
                    decision=2
                    break
                case "fire":
                    decision=1
                    break
                case _:
                    resp="Try again.\n\n[roll|fire]: "
        if decision==2:
            print("Player has re-rolled.\nThe bullet is in a different chamber.")
            roll()
            wait(2)
        print("Player has fired the gun.")
        wait(2)
        if fire()==True:
            defeat()
    else:
        bot_decision()
    

def main():
    while (True):
        minus_one()
        

def victory():
    print(""" 
_____________________________________________________________
|===========================================================|
|  ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗  |
|  ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝  |
|  ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝   |
|  ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝    |
|   ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║     |
|    ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝     |
|___________________________________________________________|
|==========|         You've won the game.        |==========|
|==========|_________Shall we try again?_________|==========|
|===========================================================|""")
    return user_resp()

def defeat():
    print(""" 
_____________________________________________________
|===================================================|
|  ▓█████▄ ▓█████   █████▒▓█████ ▄▄▄     ▄▄▄█████▓  |
|  ▒██▀ ██▌▓█   ▀ ▓██   ▒ ▓█   ▀▒████▄   ▓  ██▒ ▓▒  |
|  ░██   █▌▒███   ▒████ ░ ▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░  |
|  ░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░   |
|  ░▒████▓ ░▒████▒░▒█░    ░▒████▒▓█   ▓██▒ ▒██▒ ░   |
|  ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░    ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░      |
|  ░ ▒  ▒  ░ ░  ░ ░       ░ ░  ░ ▒   ▒▒ ░   ░       |
|  ░ ░  ░    ░    ░ ░       ░    ░   ▒    ░         |
|  ░       ░  ░           ░  ░     ░  ░             |
|__░________________________________________________|
|==========|  The bot has won the game.  |==========|
|==========|_____Shall we try again?_____|==========|
|===================================================|""")
    return user_resp()

def user_resp():
    inp=input("[y/n]: ")
    if input=="y" or input=="n":
        return input=="y"

main()
