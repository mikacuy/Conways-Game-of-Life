import numpy as np
import codecs, json
import sys

#generate boards
board1= np.random.choice(2,(15, 15))
board2= np.random.choice(2,(30, 30))
board3= np.random.choice(2,(45, 32))
board4= np.random.choice(2,(40, 60))
board5= np.random.choice(2,(80, 80))

board1=board1.tolist()
board2=board2.tolist()
board3=board3.tolist()
board4=board4.tolist()
board5=board5.tolist()

boards_dict={}
boards_dict["Small Pattern (15x15)"]=board1
boards_dict["Medium Pattern (30x30)"]=board2
boards_dict["Lengthwise Pattern (45x32)"]=board3
boards_dict["Crosswise Pattern (40x60)"]=board4
boards_dict["Large Pattern (80x80)"]=board5

if __name__=="__main__":
	file_path = sys.argv[1] ## your path variable
	json.dump(boards_dict, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
	print("Done.")