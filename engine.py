from enum import Enum

class RoomState(Enum):
	NORTH = 1
	SOUTH = 2

class PlayerState(Enum):
	QUIT = 1
	IDLE = 2
	MOVE_NORTH = 3
	MOVE_SOUTH = 4
	MOVE_EAST = 5
	MOVE_WEST = 6
	
	
class Room():
	def __init__(self):
		self.options["quit"] = PlayerState.QUIT

	def print_options(self):
		print("----- Options -----")
		for option in self.options.keys():
			print(option)
		
class NorthRoom(Room):
	def __init__(self):
		self.name = "Northern Room"
		self.description = "You are in the northern room... It is cold here I guess."
		self.options = {
			"south" : PlayerState.MOVE_SOUTH
		}
		super().__init__()

class SouthRoom(Room):
	def __init__(self):
		self.name = "Southern Room"
		self.description = "You are in the southern room... it's warm here I guess."
		self.options = {
			"north" : PlayerState.MOVE_NORTH
		}
		super().__init__()
		
class CentralRoom(Room):
	def __init__(self):
		self.name = "Central Room"
		self.description = "You are in the central room... it's lukewarm here I guess."
		self.options = {
			"north" : PlayerState.MOVE_NORTH,
			"south" : PlayerState.MOVE_SOUTH
		}
		super().__init__()
	
class StateMachine():
	def __init__(self):
		self.cur_state = PlayerState.IDLE	
		self.map = [
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, NorthRoom(), None, None, None, None, None,
			None, None, None, None, CentralRoom(), None, None, None, None, None,
			None, None, None, None, SouthRoom(), None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None,
			None, None, None, None, None, None, None, None, None, None]
		
		self.cur_room = 44
	
	def get_user_input(self):
		userin = input("Please choose an option\n> ")
		while userin not in self.map[self.cur_room].options.keys():
			print("Please choose from one of the given options")
			userin = input("> ")
		return self.map[self.cur_room].options[userin]
	
	def change_state(self, player_state):
		if player_state == PlayerState.MOVE_SOUTH and self.cur_room + 10 < len(self.map):
			self.cur_room += 10
		elif player_state == PlayerState.MOVE_NORTH and self.cur_room - 10 >= 0:
			self.cur_room -= 10
	
	def run(self):
		userinput = PlayerState.IDLE
		while userinput != PlayerState.QUIT:
			print(self.map[self.cur_room].name)
			print(self.map[self.cur_room].description)
			self.map[self.cur_room].print_options()
			userinput = self.get_user_input()
			self.change_state(userinput)
		
sm = StateMachine()
sm.run()