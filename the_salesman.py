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
cont=True

# ESSENTIAL FUNCTION; as if the terminal is talking.
def message(text:str,delay:float|int):
    print(text)
    wait(delay)

### Increments a new round
def round_shift():
    global round
    round+=1
    print(f"Proceeding to ROUND {round}.\n==================================\n\nROUND {round}")

def roll():
    global bullet
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
        message(text="The bot wins this round.",delay=2)
        message(text="You will decide this outcome.",delay=1)
        roulette(True)
    else:
        message(text="The player wins this round.",delay=2)
        message(text="The bot will decide this outcome.",delay=1)
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
    bot_choice=""
    for bot_option in bot_choices:
        match player_choice:
            case "rock" if bot_option==choices[1]: bot_choice=choices[1] #paper
            case "paper" if bot_option==choices[2]: bot_choice=choices[2] #scissors
            case "scissors" if bot_option==choices[0]: bot_choice=choices[0] #rock
            case _: bot_choice=bot_choices[rand(0,1)] #to make things fair
    if (rand(1,10)==1):
        bot_choice=bot_choices[rand(0,1)] #to make things fair
    message(text=f"Bot pulled ({bot_choice}).",delay=2)
    if player_choice==bot_choice: return "Tie"
    is_winner=rps_victor(player_choice,bot_choice)
    if is_winner==True: return "Player"
    else: return "Bot"

### Bot's bersion of russian roulette
### atleast they know what's aware.
def bot_decision():
    message(text="Bot is making a decision.",delay=2)
    try: next_bullet=bullets[bullet+1]
    except IndexError: next_bullet=bullets[0]
    is_near=next_bullet==1
    if is_near and rand(1,2)==1:
        roll()
        message(text="Bot has re-rolled.",delay=1)
        message(text="The bullet is in a different chamber.",delay=1)
    message(text="Bot has fired the gun.",delay=3)
    if fire()==True:
        victory()
    else:
        message(text="The bot survived.",delay=1)
        round_shift()
    
### after ROCK, PAPER, SCISSORS, MINUS ONE
### russian roulette is 1/6 chance the player would lose.
### player_turn:true  = player's turn
### player_turn:false = bot's turn
def roulette(player_turn:bool):
    wait(1)
    if player_turn:
        chance=1/(len(bullets)-bullet)
        print(f"Player has a {chance*100}% chance they will lose.")
        resp="""Choose wisely. "roll" "fire"\n\n["roll"|"fire"]: """
        while True:
            user_response=input(resp)
            match user_response:
                case "roll": decision=2; break
                case "fire": decision=1; break
                case _: resp="""Try again.\n\n["roll"|"fire"]: """
        if decision==2:
            roll()
            message(text="Player has re-rolled.",delay=1)
            message(text="The bullet is in a different chamber.",delay=1)
        message(text="Player has fired the gun.",delay=3)
        if fire()==True:
            defeat()
        else:
            message(text="The player survived.",delay=1)
            round_shift()
    else:
        bot_decision()

def main():
    wait(2)
    print("""
                                -#+++++                             
                           ###############                          
                         ######+-..  .#####                         
                         ###+++-.......+####                        
                         ##++++-++ .++...+#                         
                         +#++---++. .    -.                         
                          --++++##-...                              
                            ++##++-.  ..                            
                             +###++.....                            
                        .-+#+.-+#+..... ++-.                        
                 ...-+++++###+++-.-+   -#+++++++-..                 
            ++++++++##########+-#####.+########++++++++#            
            ##################+ .##+.+##################            
            ###################++#######################            
           #####################+########################           
          ################################################""")
    message(text="\nYou're going to play a game now.",delay=2)
    message(text="Rock, Paper, Scissors, Minus One.",delay=2)
    message(text="I trust you know the rules.",delay=2)
    message(text="You form a choice with each input, then take one away.",delay=3)
    message(text="The game is decided by the remaining choices.",delay=3)
    message(text="Of course, there's a penalty for the loser.",delay=3)
    message(text="I'm sure you've seen this in movies. ̸/̸̅̅ ̆̅ ̅̅ ̅̅",delay=2)
    message(text="It's called Russian Roulette.",delay=2)
    message(text="I'll place one bullet into a revolver and close it.",delay=3)
    message(text="The loser can decide to roll, or fire the gun.",delay=3)
    message(text="After they roll, they'll fire immediately.",delay=3)
    message(text="Your odds of death are 1 in 6.",delay=2)
    message(text="Your odds of survival are 5 in 6.",delay=2)
    message(text="Not that bad, right?",delay=3)
    message(text="All right.",delay=1)
    message(text="Now, let's play.",delay=2)
    round_shift()
    while (cont):
        minus_one()
    message(text="Have a good rest of your day.",delay=1)
        
### called when the bot loses.
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
    global player_wins
    player_wins=True
    user_resp()
    player_wins=False

### called when the bot wins.
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
    user_resp()

### After the player receives the game status,
### they can decide using "y" or "n" as input.
def user_resp():
    global cont
    global round
    text="[y/n]: "
    while True:
        inp=input(text)
        if inp=="y" or inp=="n":
            cont=inp=="y"
            if cont:
                round=0
                round_shift()
            break
        else:
            text="Try again.\n[y/n]: "

### Runs the main program
main()
