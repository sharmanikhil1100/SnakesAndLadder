import socket
import random
import sys
import time
import select

#a - sent message
#b - recv message
#index = 0

MAX_VAL = 100

global_var = True
Sleep = 0.5
dice = 6

port = 12301

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('',port))
#index += 1
buf = s.recv(2048) #b1
print buf

global index
while True:

	input_stream_list = [sys.stdin, s]

	# snake takes you down from 'key' to 'value'

	snakes = {

	    9: 5,

	    19: 2,

	    27: 11,

	    40: 6,

	    52: 7,

	    55: 35,

	    57: 4,

	    61: 24,

	    76: 28,

	    95: 88,

	    99: 64

	}

	# ladder takes you up from 'key' to 'value'

	ladders = {

	    3: 20,

	    6: 14,

	    11: 28,

	    15: 34,

	    17: 74,

	    22: 37,

	    38: 59,

	    73: 86,

	    81: 98,

	    88: 91

	}

	
	player_turn_text = [
	
	    "Your turn.",
	
	    "Let's go!"
	
	]
	
	snake_bite = [
	
	    "snake bite",
	
	    "oh no"
	
	]
	
	ladder_jump = [
	
	    "woohoo",
	
	    "wow"
	
	]

	def get_id(self):
	    self.id=id

	def getplayers_name():
		#s.send(str(index))
		Player1 = None
		Player2 = None
		read_sockets,write_sockets,error_sockets=select.select(input_stream_list,[],[])
		for sock in read_sockets:
			if sock == s:#b2
				Player2= None
			    	while not Player2:
					message = s.recv(2048)
					Player2= "kush"

			else:	
				while not Player1:
					message = "Enter player1 name... " 
					s.send(message) #a1
					message = raw_input("Enter your name ")
					Player1 = message
					s.send(str(Player1))#a2

	   

	    	print("\nMatch will be played between '" + str(Player1) + "' and '" + str(Player2)	 + "'\n")

	    	return Player1, Player2


	def get_valueofdice():
	    time.sleep(Sleep)

	    d_value = random.randint(1, dice)

	    print("Its a " + str(d_value))

	    return d_value


	def get_sb(old_value, c_value, player_name):
	    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")

	    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(c_value))


	def get_lj(old_value, c_value, player_name):
	    print("\n" + random.choice(ladder_jump).upper() + " ########")

	    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(c_value))


	def snake_ladder(player_name, c_value, d_value):
	    time.sleep(Sleep)

	    old_value = c_value

	    c_value = c_value + d_value

	    if c_value > MAX_VAL:
		print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")

		return old_value

	    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(c_value))

	    if c_value in snakes:

		f_value = snakes.get(c_value)

		get_sb(c_value, f_value, player_name)



	    elif c_value in ladders:

		f_value = ladders.get(c_value)

		get_lj(c_value, f_value, player_name)



	    else:

		f_value = c_value

	    return f_value


	def check_winnner(player_name, position):
	    time.sleep(Sleep)

	    if position == MAX_VAL:
		print("\n\n\nThats it.\n\n" + player_name + " won the game.")

		print("Congratulations " + player_name)

		print("\nThank you for playing the game. \n\n")

		sys.exit()


	def start():
	    
	    
	    time.sleep(Sleep)

	    Player1,Player2 = getplayers_name()

	    time.sleep(Sleep)

	    player1_cposition = 0

	    player2_cposition = 0

	    while True:
		time.sleep(Sleep)
		input_1 = raw_input("\n" + str(Player1) + ": " + random.choice(player_turn_text) + " Write next to roll dice: ")
		if input_1 == 'next':
			s.send("next")#a3
			print("\nRolling dice...")
		
			d_value = get_valueofdice()

			time.sleep(Sleep)

			print(str(Player1) + " moving....")

			player1_cposition = snake_ladder(str(Player1), player1_cposition, d_value)

			s.send(str(player1_cposition))#a4
			global_var = True
			check_winnner(str(Player1), str(player1_cposition))
			
		else:
			print ' Wrong Input'

		input_2 = s.recv(2048)#b3

		if input_2 == 'next': 
			print("\nRolling dice...")

			time.sleep(Sleep)

			print(str(Player2) + " moving....")

			player2_cposition = s.recv(2048)#b4

			check_winnner(str(Player2), str(player2_cposition))
			
		
		

	if __name__ == "__main__":
	    start()
s.close()

