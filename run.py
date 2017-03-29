import numpy as np
import turtle
import conway
import codecs, json
import sys

def draw_board():
	turtle.up()
	turtle.goto(-(window_width)/2,-(window_height/2))
	turtle.down()
	for row in range(BOARD_ROW):
	    for column in range(BOARD_COLUMN):
	        for i in range(4):
	            turtle.forward(box_size)
	            turtle.left(90)
	        if column<BOARD_COLUMN-1:
	            turtle.forward(box_size)
	        else:
	            turtle.up()
	            turtle.goto(-(window_width)/2, -(window_height)/2 + box_size*(row+1))
	            turtle.down()

def fill_box(i,j):
	game.up()
	#change scale to 1,2,...BOARD_ROW and 1,2,...,BOARD_COLUMN
	i+=1
	j+=1
	move_x=box_size*(j-BOARD_COLUMN/2) - box_size/2
	move_y=box_size*(i-BOARD_ROW/2) - box_size/2
	game.goto(move_x,-move_y)
	game.down()
	game.stamp()
	return

def display(current_board):
	game.clear()
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if(current_board[i,j]==1):
				fill_box(i,j)
	return

def start_game():
	conway.update_board(board)
	display(board)
	turtle.update()
	turtle.ontimer(start_game,1000)

if __name__=="__main__":
	###############LOAD BOARDS#################
	file_path=sys.argv[1]
	obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
	boards = json.loads(obj_text)
	patterns= list(boards.keys())
	patterns.sort()
	#print options
	print("Available patterns are:")
	for i in range(len(patterns)):
		print(i, ": ", patterns[i])

	board_index= int(input("Please select an option: "))
	while (board_index<0 or board_index>=len(patterns)):
		board_index= input("Please select a valid option: ")

	board= np.array(boards[patterns[board_index]])
	BOARD_ROW=board.shape[0]
	BOARD_COLUMN=board.shape[1]
	box_size=10
	############################################

	#########INITIALIZE DISPLAY###########
	turtle.reset()
	turtle.tracer(False)
	turtle.hideturtle()
	window_width=box_size*BOARD_COLUMN
	window_height=box_size*BOARD_ROW
	turtle.setup(window_width+100, window_height+100,startx=None, starty=None)
	draw_board()
	turtle.update()

	game=turtle.Turtle()
	game.up()
	game.hideturtle()
	game.shape("square")
	game.shapesize(0.3)
	#######################################
	start_game()
	turtle.listen()
	turtle.done()

