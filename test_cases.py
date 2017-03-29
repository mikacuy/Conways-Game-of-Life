import conway
import numpy as np
'''
Test cases for updating the board according
to the rule of Conway's Game of Life

1= alive
0= dead
'''

'''
Method to generate a random list of length 8 representing the neighbors of a cell
@param alive_neighbors= number of alive neighbors
'''
def generate_random_neighbors(alive_neighbors):
	neighbors=np.zeros(8)
	neighbors[:alive_neighbors]=1
	np.random.shuffle(neighbors)
	return neighbors

'''
Method to generate a cell with its random neighbors
@param state= initial cell state
returns 3x3 numpy array with the cell of interest at the center
'''
def generate_cell_life(state, alive_neighbors):
	neighbors= generate_random_neighbors(alive_neighbors)
	#add central cell
	board= np.append(neighbors,state)
	temp= board[-1]
	board[-1]=board[4]
	board[4]=temp
	board=board.reshape((3,3))
	return board

'''
Method to test whether current cell state == expected state
Returns SUCCESS or FAIL 
'''
def check_case(grid, expected_state):
	if (grid[1,1]==expected_state):
		return "SUCCESS"
	else:
		return "FAILED"

#Test 1: Underpopulation: a live with fewer than 2 live neighbors dies
#(1) 0 alive neighbors
grid= generate_cell_life(1,0)
conway.update_board(grid)
print("Test 1.1: Underpopulation: ", check_case(grid,0))
#(2) 1 alive neighbor
grid= generate_cell_life(1,1)
conway.update_board(grid)
print("Test 1.2: Underpopulation: ", check_case(grid,0))
print()

#Test 2: Next Generation: any live cell with 2 or 3 live neighbors lives on
#(1) 2 alive neighbors
grid= generate_cell_life(1,2)
conway.update_board(grid)
print("Test 2.1: Next Generation: ", check_case(grid,1))
#(2) 3 alive neighbor
grid= generate_cell_life(1,3)
conway.update_board(grid)
print("Test 2.2: Next Generation: ", check_case(grid,1))
print()

#Test 3: Overpopulation: any live cell with more than 3 live neighbors dies
#(1) 4 alive neighbors
grid= generate_cell_life(1,4)
conway.update_board(grid)
print("Test 3.1: Overpopulation: ", check_case(grid,0))
#(2) 5 alive neighbor
grid= generate_cell_life(1,5)
conway.update_board(grid)
print("Test 3.2: Overpopulation: ", check_case(grid,0))
#(3) 6 alive neighbors
grid= generate_cell_life(1,6)
conway.update_board(grid)
print("Test 3.3: Overpopulation: ", check_case(grid,0))
#(4) 7 alive neighbor
grid= generate_cell_life(1,7)
conway.update_board(grid)
print("Test 3.4: Overpopulation: ", check_case(grid,0))
#(5) 8 alive neighbor
grid= generate_cell_life(1,8)
conway.update_board(grid)
print("Test 3.5: Overpopulation: ", check_case(grid,0))
print()

#Test 4: Reproduction: Any dead cell with exactly 3 live neighbors becomes alive
#(1) 3 alive neighbor
grid= generate_cell_life(0,3)
conway.update_board(grid)
print("Test 4.1: Reproduction: ", check_case(grid,1))
#(2) 0 alive neighbor
grid= generate_cell_life(0,0)
conway.update_board(grid)
print("Test 4.2: Reproduction: ", check_case(grid,0))
#(3) 1 alive neighbor
grid= generate_cell_life(0,1)
conway.update_board(grid)
print("Test 4.3: Reproduction: ", check_case(grid,0))
#(4) 2 alive neighbor
grid= generate_cell_life(0,2)
conway.update_board(grid)
print("Test 4.4: Reproduction: ", check_case(grid,0))
#(5) 4 alive neighbor
grid= generate_cell_life(0,4)
conway.update_board(grid)
print("Test 4.5: Reproduction: ", check_case(grid,0))
#(6) 5 alive neighbor
grid= generate_cell_life(0,5)
conway.update_board(grid)
print("Test 4.6: Reproduction: ", check_case(grid,0))
#(7) 6 alive neighbor
grid= generate_cell_life(0,6)
conway.update_board(grid)
print("Test 4.7: Reproduction: ", check_case(grid,0))
#(8) 7 alive neighbor
grid= generate_cell_life(0,7)
conway.update_board(grid)
print("Test 4.8: Reproduction: ", check_case(grid,0))
#(9) 8 alive neighbor
grid= generate_cell_life(0,8)
conway.update_board(grid)
print("Test 4.9: Reproduction: ", check_case(grid,0))


