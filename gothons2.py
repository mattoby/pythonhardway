import numpy as np
import time

## additions: 
# exit(1)
# from sys import exit
# from random import randint

class Scene(object):
    def __init__(self):
        self.damage = 0
        self.escaped = False

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map
        self.alive = True
        self.max_damage = 8
        self.damage = 0
        self.scene = None # the cvurrent scene object.
        self.again = False

    def play(self):
        print "You have entered the gothons ship!"

        # enter first scene
        self.map.set_opening_scene()

        while True:

            self.scene = self.map.create_current_scene()
#            print "you have entered the %s" % self.map.scene_names[self.map.current_scene]


            self.scene.enter()

            # deal with damage:
            self.damage += self.scene.damage
            if self.max_damage/2 <= self.damage < self.max_damage:
                print "Be careful! Your squirting blood is ruining the carpet!\n"

            if self.damage >= self.max_damage:            
                self.alive = False

            if self.alive == False or self.scene.escaped == True:
                break
            else:
                self.map.set_next_scene()



        if self.alive == False:
            self.map.set_scene('death')            
            self.scene = self.map.create_current_scene()
            self.scene.enter()

        else:
            print "Good job! you made it out! you are floating in space. Sah-weet.\n"

        print "play again?"
        again = raw_input('yes or no:')
        if again == 'yes':
            self.again = True

        return self.again

class Map(object):

    def __init__(self, start_scene):

        self.current_scene = start_scene
        
                    }self.scenes = {'central' : CentralCorridor(),
                    'death' : Death(),
                    'laser' : LaserWeaponArmory(),
                    'bridge' : TheBridge(),
                    'escape' : EscapePod()
        self.scene_names = {'central':'central corridor',
                            'laser' : 'laser armory',
                            'bridge' : 'bridge',
                            'escape' : 'escape pod',
                            'death' : 'death state'
                            }

        # 2d map of the layout
#        layout = np.matrix([['laser','bridge'],
#                            ['corridor','bridge'],
#                            ['escape','bridge']]) 
        self.layout = ['central','laser','bridge','escape','death'];

    def set_next_scene(self):
        curr_ind = self.layout.index(self.current_scene)
        new_scene = self.layout[curr_ind + 1]
#        print "NOW ENTERING THE SCENE %s" % new_scene
        self.current_scene = new_scene

    def create_current_scene(self):
        scene = self.scenes[self.current_scene]
        return scene

    def set_scene(self, scene_name):
        self.current_scene = scene_namefa

    def set_opening_scene(self):
        self.current_scene = self.layout[0]

class Death(Scene):

    def enter(self):
        print "You die the most horrible death you can imagine."
        print "The end."

class CentralCorridor(Scene):

    def enter(self):
        print '''
        You have entered the central corridor!
        It is very pretty. There are high waisted pants everywhere.
        There is only one way forward. But lo, before your very eyes appears 
        a large, gorgeous Gazelle-like creature who leers at you with his
        enormous, almond-shaped eyes, pants, drools into a puddle on the floor, 
        and says:

        "If you wish to pass the central corridor, you must 
        answer me this riddle, lo the other side you'll see.
        What is your name?!"
                '''
        self.name = raw_input('> ')

        print "What is your quest?"

        self.quest = raw_input('> ')

        print "what is your favorite color?"

        self.color = raw_input('> ')


        print '\n"Your color is stupid, %s" he says.' % self.name
        raw_input(' ')    
        print '"%s?!?!' % self.color
        raw_input(' ')    
        print '"I mean, seriously, girl."\n'
        raw_input(' ')    


class LaserWeaponArmory(Scene):
    def __init__(self):
        super(LaserWeaponArmory, self).__init__()
        self.choice = None
        print "laser weapon armory initiated"

    def enter(self):

        print '''
        You now enter the laser armory. It smells funny in here.
        Then you see it! Zoe, apparently zombified by her new man, groaning and 
        shuffling towards you!

        To the left is a full bar, to the right is a set of turntables, and 
        straight ahead is Zombified Zoe! What do you do?

        (a) make her a drink
        (b) play her some music
        (c) sing to her
        (d) try to talk it out

        '''

        self.choice = raw_input('choose a, b, c, or d > ')

        if self.choice == 'a':
            print "you mix up some scotch and soda, and she seems to like it!"
            print "but no, she is too close. she bites off your neck. Ah, the pain!"
            print "quick, to the door. maybe you can escape before you fully zombify!"
            self.damage = 4
        elif self.choice == 'b':
            print "you bust out some bassnectar."
            print "and ho, she likes it! quick, to the door!"
        elif self.choice == 'c':
            print "you start to sing:"
            print "later on the other siiii,eyiiide!"
            print "never thought i'd get outta liiiii,vve!"
            print "\n quick, she seems to have lulled into a trance. You run to the door!"
        elif self.choice == 'd':
            print '"Heyyyy, Zoe, how\'s it going?" you say'
            print "it seems to be working! she is appeased!"
            raw_input()
            print '"Remember back in a capella?", you say, creeping forward'
            raw_input()
            print "oh no. she didn't like that. bad memories?"
            raw_input()
            print '"uh, I\'ve got some bassnectar here, i think," you say'
            raw_input()
            print "but no, it's too late. she lunges and bites your hand off. You Run!"
        else:
            print "yeah, that's right! who am *I* to follow the rules, you say?!"
            raw_input()
            print "you do the only obvious thing, which is to grab the airlock,"
            print "rip it off the wall,"
            print "and sing karaoke to the whishing sound of air from the chamber,"
            print "until there is no sound at all, "
            print "and you and Zoe both are floating in space."
            self.damage += 10
        raw_input()

    
class TheBridge(Scene):

    def enter(self):
        print "You're in the bridge!"
        print "it's really hot & getting hotter! run!"

        while True:
            self.mary = raw_input('> ')
            self.damage += 1
            print "Ah, gawd! the pain! quick, type out 'mary had a little lamb'!"

            if self.mary == 'mary had a little lamb':
                break

        print "phew, you escaped."
        raw_input()


class EscapePod(Scene):

    def enter(self):
        print "Wow, you made it to the escape pod!"
        raw_input()
        print "but lo, it is very smelly in here too!"
        print "it smells... amazing!"
        raw_input()
        print "uh oh. now you see it. a big mound of fried chicken!"
        print "what do you do?!"
        print "(a) eat it"
        print "(b) ignore it"
        self.chicken = raw_input('a, b, or other? >')

        if self.chicken == 'a':
            print "oh my god, you broke vegetarianism! You're in mortal pain!"
            self.damage += 2
        elif self.chicken == 'b':
            print "oh, oh no! it turned into a chicken monster, and it attacks you!"
            print "what do you do?"
            self.action = raw_input('run, fight, or other? > ')
            if self.action == 'run':
                print "aah, the only place to run is into the burning ship! the pain!"
                print "next time, think outside the box!"
                raw_input()
                self.damage += 10
            elif self.action == 'fight':
                print "seriously, you're going to fight the giant chicken monster?!"
                print "bad idea! "
                raw_input()
                self.damage += 10
            else:
                print "good idea! you make it out!"
                raw_input()
        else:
            print "alright! great idea! you make it!"
            raw_input()
        self.escaped = True






again = True
while again == True:
    a_map = Map('central')
    a_game = Engine(a_map)
    again = a_game.play()


