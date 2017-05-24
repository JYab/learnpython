from sys import exit
import random
from random import randint
from random import choice
import time

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


            # Starts game out
        current_scene.enter()


class Death(Scene):

        death =  [
        "You make me sick!",
        "You died from an overdose of pure cringe",
        "My grandma can play this better than you. And she's dead.",
        "Wow, that was bad. Guess you were meant to die"
    ]
        def enter(self):
            print Death.death[randint(0, len(self.death)-1)]
            exit(1)

class CentralCorridor(Scene):
    global choice
    def enter(self):
        print "Narrator: As you enter the room a gothon looks back at you and "
        print "realizes that you're ready to punch him right in the balls."
        raw_input()
        print "He says \"Whoa, wait! Let's just have a roast battle."
        print "If I win I get to capture you and get promoted."
        print "When you win i'll let you pass. Deal or Nah?"
        raw_input()
        print "Cuz i'm meeting my mother after my shift.\""
        print "You: Fine, but i'm only doing this because i'm nice!"
        raw_input()
        print "Thank the goodness from your heart. OK, you want to start or..."
        print "you know what i'll just start first. You know the saying"
        print "'Gothons go first.'\n\nYou: I've nev-\n\nGothon: Oh, just thought of something really roasty to say!"
        raw_input()
        print "Narrator: (Little did you know that this particular gothon was"
        print "waiting to say this roast his whole life.)"
        raw_input()
        print "Gothon: If you were my sibling, I would poison your coffee"
        print "Narrator: Oh, it's not even that good..."
        raw_input()
        print "Narrator: Do you say something from the top of your head[1]\n"
        print "OR do you think about it and risk wasting time[2]"
        True
        while True:
            choice = raw_input("1 OR 2\n")
            if "1" in choice:
                print "You: Uh...if I was your mom I would make sure you're grounded"
                print "Narrator: Ouch...That hurt inside"

                return 'death'

            elif "2" in choice:
                print "You: If I was your sibling, I would drink it!"
                print "Narrator: * flicks hand * BOI, WHERE U LEARN DAT FROM"
                raw_input()
                return 'laser_weapon_armory'
            else:
                print "!!! FOLLOW DIRECTIONS DINGUS !!!"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Narrator: When you enter the  Weapon Armory door directly across"
        print "from the hall, the door quickly shuts behind you. It is pitch black."

        print "What do you do?: [T]urn on the lights"
        print "[A]sk if there's someone in the room with you"

        print "or do you [G]rab the nearest weapon you touch and light the room to a"
        print "\nblaze in fear that you might not be alone in the room?"

        while True:
            print "Type T, A, or G"
            choice = raw_input()

            if choice == 'T':
                print "After you turn on the lights, you immediatly regret the"
                print "decision. You see that there are a whole battalion of Gothons"
                print "pointing guns to your head. Your head is blown off"
                print "and the guts and pieces of brain shower the Weapon Armory!"

                print "Narrator: Priceless! I love this game!"
                return 'death'
            if choice == 'A':
                print "Narrator: Wow, I never thought you would ever do that!"
                print "I just gave you that choice to be funny, but it's obvious that"
                print "you're kinda stupid!"
                raw_input()
                print "\nI think you deserve to die"

                return 'death'

            if choice == 'G':
                print "You pick the nearest gun and light the whole room on fire!"
                raw_input()
                print "You can see that there are hundreds of gothons cramped in the"
                print "room as it is being lit. "
                raw_input()
                print "Narrator: Oh, I forgot to tell you that there's a bomb in here!"
                raw_input()
                print "You quickly realize that you forgot that the neutron bomb"
                print "had been placed in the burning room you are standing in right now. welp"
                raw_input()
                print "The explosion from the bomb bursts a hole in the ship and kills"
                print "most of the gothons in the room before they are thrown into"
                print "the vacuum of space. You struggle to hold on to the"
                print "fried up wires that hang from the ship as a gothon tries"
                print "to climb up your leg."
                raw_input()
                print "You're able to kick him off and get to the door and close it before anyone else."
                raw_input()
                print "Narrator: um...how did you do that."
                raw_input()
                print "I only see that in that in the movies. Well, we have to"
                print "keep moving then. * mumbles *Off to the bridge of the ship I guess*"
                return 'the_bridge'
            else:
                print "That's not a choice. Try again."

class TheBridge(Scene):

    def enter(self):

        print "Narrator: Wait a minute...Nobody can ever be that good...unless..."
        print "Narrator: HAAAA! I BET YOU'RE CHEATING. BOI, ARE YOU CHEATING!!"
        raw_input()
        print "Narrator: Well, I bet you can't get past this! *snaps finger*"
        print "Hundreds of gothons suddenly appear and circle around in confusion."
        raw_input()
        print "You figure that this the perfect moment to make a break for it"
        print "while the gothons are all distracted. You pass the bridge and off"
        print "to the escape pod latches."
        raw_input()
        return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        global keypad
        print "Narrator: HEY!! NOT SO FAST!!! * erases part of script from paper *"
        print "Narrator: OOPSY DAISIES!!! LOOKS LIKE YOU FORGOT THE KEYPAD PASS"
        print "FOR THE ESCAPE PODS."
        raw_input()
        print "Oh, boohoo cheater.You have to guess all four of the numbers of the password."
        print "WOOPS! But I'm nice so you get to choose from numbers 5-9 to make it easier"

        keypad = random.sample(range(5, 9), 4)





        global nine_secs
        nine_secs = 0
        while True:
            # Only run if the user types in "start"
            while nine_secs != 4:
                # Sleep for 9 seconds
                time.sleep(9)
                # Increment the minute total
                nine_secs += 1

                # Loop until we reach 20 seconds
                if nine_secs == 1:
                    print keypad[0]
                    print "What does %d mean? Where did that number show up?" % keypad[0]
                    print "I mean...yep, you have %d seconds left to press in the" % keypad[0]
                    print "right password. You better get going...he...he..."
                if nine_secs == 2:
                    print keypad[1]
                    print "Yeah, now you have %d seconds before the ship blows up." % keypad[1]
                    print "* narrator whispers to himself * I don't think he's catching on."
                    print "What an idiot."
                if nine_secs == 3:
                    print keypad[2]
                    print "Uh..."
                if nine_secs == 4:
                    print keypad[3]
                    print "Should I keep trying?"
                    print "Narrator of Narrator?: Guess the combination"

                    global choice
                    keypad = map(str, keypad)
                    choice = raw_input()
                    choice = (" ".join(choice))
                    choice = choice.split()

                    if choice == keypad:
                        print "Narrator of Narrater: You 'guessed' the right combination of numbers for the launch"
                        print "and shoot your escape pod towards your home planet!"
                        return 'finished'


                    else:
                        print "Wow, you're an idiiot!"
                        return 'death'
                else:
                    pass


class Finished(Scene):

    def enter(self):
        print "Narrator: WAIT WHAAT!? WELL I EXPECT NOTHING LESS FROM A CHEA-"

        global nine_secs
        nine_secs = 0

        # Only run if the user types in "start"
        while True:
            # Sleep for 5 seconds
            time.sleep(5)
            # Increment the minute total
            nine_secs += 1



            # Loop until we reach 20 seconds
            if nine_secs == 1:
                print"         __   __  _______  __   __    _     _  ___   __    _  __           "
                print"        |  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  |          "
                print"        |  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  |          "
                print"        |       ||  | |  ||  |_|  |  |       ||   | |       ||  |          "
                print"        |_     _||  |_|  ||       |  |       ||   | |  _    ||__|          "
                print"          |   |  |       ||       |  |   _   ||   | | | |   | __           "
                print"          |___|  |_______||_______|  |__| |__||___| |_|  |__||__|          "
                print" _______  _______  __   __  _______    _______  __   __  _______  ______   "
                print"|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  "
                print"|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  "
                print"|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ "
                print"|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |"
                print"|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |"
                print"|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|"
            	print "WAIT, I'M NOT DONE HERE! YOU HEAR MEEE! I'M THE NARRATOR!"
            elif nine_secs == 2:
                print "I SHOULD DECIDE WHO WINS AND LOSES!"
            elif nine_secs == 3:
                print "You still here?"
                print "Ah, forget it"


                exit(0)






class Map(object):
    scenes = {
    'death': Death(),
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'finished': Finished()
    }
    def next_scene(self, scene_name):
        self.next_scene = self()
        #self.next scene calls the roomFunction
    def __init__(self, start_scene):
        self.start_scene = start_scene
        #self.start_scene shortens to start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        # gets the scenes[] list and the scene_name
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
