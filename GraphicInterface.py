from tkinter import Tk, Canvas, Button, LEFT, BOTTOM
import initialise
from MaxRewards import MaxRewards

COLOR_BACKGROUND_CELLULE = 'white'
COLOR_BACKGROUND_CANVAS = 'blue'
LINE_CELLULE_SEPARATOR = 'black'
COLOR_REWARD_CELLULE = 'orange'
WIDTH_CELLULE_SEPARATOR = 5
COLOR_OUTLINE_START_CELLULE = 'yellow'
COLOR_OUTLINE_END_CELLULE = 'green'
COLOR_OUTLINE_SIMULATION = 'red'

MAT = initialise.MATRIX
START = initialise.START
END = initialise.END
MAT_X = len(MAT[0])
MAT_Y = len(MAT)
CELLULE_SIZE = 80
PAD = int(CELLULE_SIZE*(1-0.8))
MIN_X = 0 #A ne pas changer
MIN_Y = 0 #A ne pas changer
MAX_X = MAT_X * CELLULE_SIZE
MAX_Y = MAT_Y * CELLULE_SIZE 

root = Tk()
root.title('Max Carrot Rewarded')
canvas = Canvas(root,  width=MAX_X, height=MAX_Y+150, background=COLOR_BACKGROUND_CANVAS)
#canvas.pack(fill='both', expand=True)

def trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y):
	canvas.create_rectangle(MIN_X, MIN_X, MAX_X, MAX_Y, width=1, fill=COLOR_BACKGROUND_CELLULE)
	for i in range(MIN_X+CELLULE_SIZE, MAX_X, CELLULE_SIZE):
		canvas.create_line((i, MIN_X, i, MAX_Y), width=WIDTH_CELLULE_SEPARATOR, fill=LINE_CELLULE_SEPARATOR)
	for j in range(MIN_Y+CELLULE_SIZE, MAX_Y, CELLULE_SIZE):
		canvas.create_line((MIN_Y, j, MAX_X, j), width=WIDTH_CELLULE_SEPARATOR, fill=LINE_CELLULE_SEPARATOR)

def start_point(start):
	y,x = start
	r = (x*CELLULE_SIZE+PAD, y*CELLULE_SIZE+PAD, CELLULE_SIZE*(x+1)-PAD, CELLULE_SIZE*(y+1)-PAD)
	canvas.create_rectangle(r, width=WIDTH_CELLULE_SEPARATOR, outline=COLOR_OUTLINE_START_CELLULE)

def end_point(end):
	y,x = end
	r = (x*CELLULE_SIZE+PAD, y*CELLULE_SIZE+PAD, CELLULE_SIZE*(x+1)-PAD, CELLULE_SIZE*(y+1)-PAD)
	canvas.create_rectangle(r, outline=COLOR_OUTLINE_END_CELLULE, width=WIDTH_CELLULE_SEPARATOR*2.5)

def carrots(matrix):
	for i in range(MAT_Y):
		for j in range(MAT_X):
			val = MAT[i][j]
			r = (i*CELLULE_SIZE, j*CELLULE_SIZE, CELLULE_SIZE*(i+1), CELLULE_SIZE*(j+1))
			r = (j*CELLULE_SIZE+PAD, i*CELLULE_SIZE+PAD, CELLULE_SIZE*(j+1)-PAD, CELLULE_SIZE*(i+1)-PAD)
			if val > 0:
				canvas.create_rectangle(r, width=1, outline=COLOR_REWARD_CELLULE,  fill=COLOR_REWARD_CELLULE)

effet_simulation = START
iteration = 0

def itineraries():
	global effet_simulation
	y,x = effet_simulation
	r = (x*CELLULE_SIZE, y*CELLULE_SIZE, CELLULE_SIZE*(x+1), CELLULE_SIZE*(y+1))
	canvas.create_rectangle(r, outline=COLOR_OUTLINE_SIMULATION,width=WIDTH_CELLULE_SEPARATOR*2)
	root.after(1000, simulation_step)

def simulation_step():
	global effet_simulation, iteration
	if iteration < len(itineraire):
		effet_simulation = itineraire[iteration]
		itineraries()
		iteration += 1

def simulation(MAT, START, END):
	canvas.delete('all')
	global itineraire
	trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
	start_point(START)
	end_point(END)
	carrots(MAT)
	M = MaxRewards(MAT, START, END)
	rewards = M.get_max_rewards()
	movements = M.get_movements()
	itineraire = M.get_itineraries()
	simulation_step()
	print(START, END, itineraire)

def play():
	simulation(MAT, START, END)
	
def generate_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y, MAT, START, END):
	trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
	start_point(START)
	end_point(END)
	carrots(MAT)

def run():
	#generate_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y, MAT, START, END)
	trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
	start_point(START)
	end_point(END)
	carrots(MAT)
	start_simulation = Button(root, text='START SIMULATION', width=20, command=play)
	start_simulation.pack(side=BOTTOM, padx=10, pady=20)
	canvas.pack(expand=False)
	root.mainloop()
	
run()
