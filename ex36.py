#key is not working

from sys import exit


#variables
prompt = "> "
key = False
buildings = ['blacksmith', 'inn', 'gate', 'go back']

#functions
def dead(cause):
    print cause, "Better luck next time!"
    exit(0)


def gate():
    print "You are at the gate."
    print "What would you like to do?"
    print "\t*Go back\n\t*Open the gate"
    
    next = str(raw_input(prompt).lower())
    
    if "go back" in next or "back" in next:
        print "You are heading back to the square."
        square()
    elif "open" in next or "open the gate" in next:
        if key == True:
            print "You open the gate."
            print "A troll sees you and tries to kills you with his mace."
            #fight()
        else:
            print "It is locked."
            dead("A thief stabs you and takes your money.")
    else:
        dead("A dragon attacked you and ripped open you chest.")
    
 
def square():
    print "You are at the square."
    print "You see different buildings."
    
    for building in buildings:
        print "\t*", building
        
    print "To which building would you like to go?"
    
    next = str(raw_input(prompt).lower())
    
    if "blacksmith" in next:
        print "The blacksmith wont let you enter."
        print "You try to go in through the window."
        dead("The guard dog bites your neck and you die.")
    elif "inn" in next:
        print "You meet an old nemesis."
        dead("The nemesis kills you with his gun.")
    elif "gate" in next:
        print "You are heading to the gate."
        gate()
    elif "go back" in next or "back" in next:
        print "You are heading back."
        village()
    else:
        dead("The guard wonders what you are doing and throws you in jail to be safe.")


def home():
    print "You are home."
    
    if key == False:
        print "There is a key on the table."
        print "What would you like to do?"
        print "\t* Grab key\n\t* Leave the house"
    
        next = str(raw_input(prompt).lower())
    
        if "grab key" in next or "grab" in next or "key" in next:
            print "You take the key, put it in your pocket and are heading outside."
            key = True
            return key
            village()
        elif "leave the house" in next or "leave" in next:
            print "You leave the house."
            village()
        else:
            dead("You trip and break your neck.") 
    else:
        print "There is nothing here."
        village()


def village():
    print "You are in the village"
    print "Where would you like to go?"
    print "\t*My home\n\t*The square"
    
    next = str(raw_input(prompt).lower())
    
    if "my home" in next or "home" in next:
        print "You are heading to your home."
        home()
    elif "the square" in next or "square" in next:
        print "You are heading to the square."
        square()
    else:
        dead("You wander around aimlessly and die by dehydration.")
    
    
village()
    

