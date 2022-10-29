from enum import Enum

class GameState:
	def __init__(self):
		self.has_read_book = False

class PlayerState(Enum):
	QUIT = 1
	IDLE = 2
	MOVE_NORTH = 3
	MOVE_SOUTH = 4
	MOVE_EAST = 5
	MOVE_WEST = 6
	UPDATE_ROOMSTATE = 7 
	
class Room():
	def __init__(self):
		self.options["quit"] = (PlayerState.QUIT, None)
	
	def describe(self):
		print(self.description)

	def print_options(self):
		print("----- Options -----")
		for option in self.options.keys():
			print(option)
		
class NorthRoom(Room):
	def __init__(self):
		self.name = "Northern Room"
		self.description = "You are in the northern room... It is cold here I guess."
		self.options = {
			"south" : (PlayerState.MOVE_SOUTH, None)
		}
		super().__init__()

class SouthRoom(Room):
	
	class SRState(Enum):
		READ_BOOK = 1
		PENGUIN_TALK = 2 

	def __init__(self):
		self.name = "Southern Room"
		self.description = "You are in the southern room... it's warm here I guess."
		self.options = {
			"north" : (PlayerState.MOVE_NORTH, None),
			"book"  : (PlayerState.UPDATE_ROOMSTATE, self.SRState.READ_BOOK)
		}
		super().__init__()
		
		self.has_read_book = False
		self.has_penguin = False
	
	def update_roomstate(self, gamestate, update_state):
		if update_state == self.SRState.PENGUIN_TALK:
			print("The penguin talks about this book for quite literally hours. You will never get that time back.")
		if update_state == self.SRState.READ_BOOK:
			self.read_book(gamestate)
		if gamestate.has_read_book:
			self.options["talk"] = (PlayerState.UPDATE_ROOMSTATE, self.SRState.PENGUIN_TALK)
			
	def read_book(self, gamestate):
		print("you read the book. Someone seems to have noticed your interest in reading")
		self.has_read_book = True
		gamestate.has_read_book = True
		self.has_penguin = True
		
	def describe(self):
		print(self.description)
		if self.has_penguin:
			print("There is also a penguin here")
		if self.has_read_book:
			print("You notice the book that you read")
		
class CentralRoom(Room):
	def __init__(self):
		self.name = "Central Room"
		self.description = "You are in the central room... it's lukewarm here I guess."
		self.options = {
			"north" : (PlayerState.MOVE_NORTH, None),
			"south" : (PlayerState.MOVE_SOUTH, None)
		}
		super().__init__()
	
class StateMachine():
	def __init__(self):
		self.cur_state = (PlayerState.IDLE, None)	
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
	
	def change_state(self, gamestate, player_state):
		if player_state[0] == PlayerState.UPDATE_ROOMSTATE:
			self.map[self.cur_room].update_roomstate(gamestate, player_state[1])
		elif player_state[0] == PlayerState.MOVE_SOUTH and self.cur_room + 10 < len(self.map):
			self.cur_room += 10
		elif player_state[0] == PlayerState.MOVE_NORTH and self.cur_room - 10 >= 0:
			self.cur_room -= 10
	
	def run(self):
		gamestate = GameState()
		userinput = (PlayerState.IDLE, None)
		while userinput[0] != PlayerState.QUIT:
			print(self.map[self.cur_room].name)
			self.map[self.cur_room].describe()
			self.map[self.cur_room].print_options()
			userinput = self.get_user_input()
			self.change_state(gamestate, userinput)
		
sm = StateMachine()
sm.run()