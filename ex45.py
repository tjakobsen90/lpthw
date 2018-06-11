# - character with hp, atk and def, he also has a bag
# - monsters with hp, atk and def

# Import modules
from sys import exit
from random import randint

# I dont fcking know
#class Scene(object):
#
#	def enter(self):
#		print "WTF does this do?"
#	exit(1)

# 
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n","-" * 10
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

# When you die you get a small text, the text is chosen at random. After that exit the game.
class Death(object):

	rip = [
		"You died. Is your name Marijn?",
		"You died. No SS? TEAM?",
		"You died. Kar98k to the face.",
		"You died. Follow the plan, HP > 0."
		]

	def enter(self):
		print Death.rip[randint(0, len(self.rip)-1)]
		exit(1)


class Home(object):

	def enter(self):
		print "Im home."
		return 'square'

class Square(object):

	def enter(self):
		print "Im at the square."
		return 'death'

class Map(object):

	scenes = {
		'home': Home(),
		'square': Square(),
#		'inn': Inn(),
#		'gate': Gate(),
#		'forest': Forest(),
#		'cave': Cave(),
#		'underwater_lake': Lake(),
#		'monster_room': Monster(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

# This actually starts the game
a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
