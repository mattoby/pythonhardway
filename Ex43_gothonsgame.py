import numpy as np

class Scene(object):

    def enter(self, scene_map):
        print "you have entered the %s" % scene_map.scene_names[scene_map.current_scene]


class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

#    def create_scene(self,scene_map):


    def play(self):

        # enter the current scene
#        scene.enter(self.map)

        # play the current scene

        # exit the current scene

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):

        self.current_scene = start_scene

        self.scenes = {'central' : CentralCorridor(),
                    'death' : Death(),
                    'laser' : LaserWeaponArmory(),
                    'bridge' : TheBridge(),
                    'escape' : EscapePod()
                    }

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


    def next_scene(self, scene_name):
        curr_ind = self.layout.index(scene_name)
        new_scene = self.layout[curr_ind + 1]
        self.current_scene = new_scene
        return self.current_scene 

    def opening_scene(self):
        self.current_scene = layout[0]
        return self.current_scene


a_map = Map('central')
a_game = Engine(a_map)
a_game.play()