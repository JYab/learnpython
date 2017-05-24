import random

health = 5 # Character health
skillp = 0 # skill points


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def selskill():
    global skillp
    while True:

        select = raw_input("Choose what skill you want to customize.")

        if RepresentsInt(select) == True:
            print "Those are not words. Try again"
        if skillp == 5:
            print "You have reached the max amount of skill points."
            print "Do you want to [continue] or [redo]?"
            redo = raw_input(">")
            if redo == "redo":
                skillp -= skillp
                if redo == "continue":
                    pass # start game
        elif select == "health":
            hpmake()
        elif select == "agility":
            agility()
        elif select == "attack":
            attack()
        else:
            print "You have to choose from health, agility, and attack"
        if __name__ == "__main__":
                selskill()
def hpprint():
    print "Here you can customize your character's stats!"
    print "You have 5 skill points to start out with."
    print "Here is the list of skills your character will have: Health, Agility, and Attack"
    selskill()

hpprint()

def hpmake():

    while True:
        global skillp

        hbonus = raw_input("Type in your bonus health (you start out with 5 already)")

        if RepresentsInt(hbonus) == True:
            hbonus = int(hbonus)
            skillp += hbonus

            if skillp >= 6:
                print "You cannot have more than 5 skill points! Retry"
                skillp -= skillp

                # this is if the skill points have more than 5
            elif skillp <= 5:
                hbonus = int(hbonus)
                print "Are you sure you want %d bonus health?" % hbonus
                print "Hit enter if you are sure. Type redo to change your skill points."
                redo = raw_input(">") # this is an "are you sure step"
                if redo == "redo":
                    skillp -= skillp

                if redo != "redo":
                    selskill()



            else:
                pass
        else:
            print "That's not a number. Try again"


if __name__ == "__main__":
    hpmake()

def agility():

    while True:
        global skillp
        agility = raw_input("Type in how much agility you want(you have used %d/5 skillpoints)" % skillp)

        if RepresentsInt(agility) == True:
            agility = int(agility)
            skillp += agility

            if skillp >= 6:
                print "You cannot have more than 5 skill points! Retry"
                skillp -= skillp

                # this is if the skill points have more than 5
            elif skillp <= 5:
                agility = int(agility)
                print "Are you sure you want %d agility?" % agility
                print "Hit enter if you are sure. Type redo to change your skill points."
                redo = raw_input(">") # this is an "are you sure step"
                if redo == "redo":
                    skillp -= agility

                if redo != "redo":
                    skillp += agility
                    selskill()


            else:
                pass
        else:
            print "That's not a number. Try again"

if __name__ == "__main__":
    agility()

def attack():

    while True:
        global skillp
        attack = raw_input("Type in how much attack you want(you have used %d/5 skillpoints)" % skillp)

        if RepresentsInt(attack) == True:
            attack = int(attack)
            skillp += attack

            if skillp >= 6:
                print "You cannot have more than 5 skill points! Retry"
                skillp -= skillp

                # this is if the skill points have more than 5
            elif skillp <= 5:
                agility = int(agility)
                print "Are you sure you want %d attack?" % attack
                print "Hit enter if you are sure. Type redo to change your skill points."
                redo = raw_input(">") # this is an "are you sure step"
                if redo == "redo":
                    skillp -= attack

                if redo != "redo":
                    skillp += attack
                    selskill()


            else:
                pass
        else:
            print "That's not a number. Try again"

if __name__ == "__main__":
    attack()



def dead():
    if health <= 0:
        print "   ____                                 ___                        "
        print "  / ___|   __ _   _ __ ___     ___     / _ \  __   __   ___   _ __ "
        print " | |  _   / _` | | '_ ` _ \   / _ \   | | | | \ \ / /  / _ \ | '__|"
        print " | |_| | | (_| | | | | | | | |  __/   | |_| |  \ V /  |  __/ | |   "
        print "  \____|  \__,_| |_| |_| |_|  \___|    \___/    \_/    \___| |_| "
        quit()



def bat():

    damg = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
    return random.choice(damg)
