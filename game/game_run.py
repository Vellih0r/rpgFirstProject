import player
import shop

# added decoration for welcome text; by artyom
# just stars)))
# get lost, that's just looks beautiful)
def decorator(insidefunc):
    def outfunc(arg):
        print('*' *  60)
        insidefunc(arg)
        print('*' *  60)
    return outfunc

# added beginning in game; by artyom
@decorator
def welcome(username):
    print(f'''
        Welcome to our game, {username}!
    Balance: {Hero.balance}
>> 1 [Statistics]
>> 2 [Store]
>> 3 [Your Inventory]
        ''')


# ALL anything below we can put in infinite game loop ↓ ↓ ↓


# added username var.; by artyom
username = input("Enter your username:\n")

# added creating new object and give one arg to another class; by artyom
Hero = player.Player(username)

# ************************************************************************************************************

# call the function 'welcome'
welcome(Hero.name)

# added choose var. for define where to go user  AND  check for errors; by artyom
try:
    choice = int(input("type 1,2 or 3 to choose...\n"))
    if choice == 1: Hero.display_stats()
    elif choice == 2: pass
    elif choice == 3: Hero.inv()
    else:
        print("Undefined choice.")
except:
    print("Error: you need just type 1,2 or 3")


# example of how we can use the base class

# Hero.add_item("Shield")
# Hero.update_stats()
# Hero.display_stats()