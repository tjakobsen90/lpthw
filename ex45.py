#Own made game for excersise 45 of LPTHW by Zed Shaw.

# Import modules
from sys import exit
from random import randint, choice

# I dont fcking know
#class Scene(object):
#
#	def enter(self):
#		print "WTF does this do?"
#	exit(1)

# This selects and prints out the scene
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

# All environments
class Home(object):

	def enter(self):
		print "Im home."
		return 'square'

class Square(object):

	def enter(self):
		print "Im at the square."
		return 'death'

class Inn(object):
	print "I'm inside the inn."
	pass

class Gate(object):
	print "I'm at the gate."
	pass

class Forest(object):
	print "I'm in the forest."
	pass

class Cave(object):
	print "I'm inside the cave."
	pass

class Underwater_lake(object):
	print "I'm at the underwater lake."
	pass

class Monster_room(object):
	print "I'm in the room with the monster."
	pass

# Monsters and player
class Player(object):
	pass

# added
class Troll(Monster):

	def troll():
		hp = 100
		atk = 10
		print "A troll appears!"

	def gnoll():
		hp = 50
		atk = 20
		print "A gnoll appears!"

	def wolf():
		hp = 25
		atk = 40
		print "A wolf appears!"

	def bear():
		hp = 75
		atk = 15
		print "A bear appears!"

	choice([troll, gnoll, wolf, bear])()

class Monster_boss(object):
	pass

# Map selection and follow-up
class Map(object):

	scenes = {
		'home': Home(),
		'square': Square(),
		'inn': Inn(),
		'gate': Gate(),
		'forest': Foest(),
		'cave': Cave(),
		'underwater_lake': Underwater_lake(),
		'monster_room': Monster_room(),
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
