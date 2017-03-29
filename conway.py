import numpy as np

'''
This method takes any board (numpy array) 
and updates it based on the rules of Conway's Game of Life

1= alive
0= dead
'''
def update_board(board):
	temp= np.lib.pad(board,1,"constant")

	for i in range(board.shape[0]):
		for j in range(board.shape[1]):

			#get number of alive neighbors
			num_alive_neighbors=0
			for x in range(3):
				for y in range(3):
					#dont include self
					if(x==1 and y==1):
						continue
					#neighbors
					if(temp[i+x,j+y]==1):
						num_alive_neighbors+=1

			#get state for successive board
			#(1)alive cell
			if(temp[i+1,j+1]==1):
				if(num_alive_neighbors<2 or num_alive_neighbors>3):
					board[i,j]=0
				else:
					board[i,j]=1
			#(2)dead cell
			else:
				if(num_alive_neighbors==3):
					board[i,j]=1
				else:
					board[i,j]=0
	return