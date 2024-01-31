from tkinter import Tk, Canvas, Button
import initialise

COLOR_BACKGROUND_CELLULE = 'white'
COLOR_BACKGROUND_CANVAS = 'blue'
LINE_CELLULE_SEPARATOR = 'black'
COLOR_SURVIVE_CELLULE = 'orange'
WIDTH_CELLULE_SEPARATOR = 5

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
	r = (x*CELLULE_SIZE+PAD, y*CELLULE_SIZE, CELLULE_SIZE*(x+1), CELLULE_SIZE*(y+1)-PAD)
	canvas.create_rectangle(r, width=1, fill='yellow')

def end_point(end):
	y,x = end
	r = (x*CELLULE_SIZE, y*CELLULE_SIZE+PAD, CELLULE_SIZE*(x+1)-PAD, CELLULE_SIZE*(y+1))
	canvas.create_rectangle(r, width=1, fill='green')

def carrots(matrix):
	for i in range(MAT_Y):
		for j in range(MAT_X):
			val = MAT[i][j]
			r = (i*CELLULE_SIZE, j*CELLULE_SIZE, CELLULE_SIZE*(i+1), CELLULE_SIZE*(j+1))
			r = (j*CELLULE_SIZE+PAD, i*CELLULE_SIZE+PAD, CELLULE_SIZE*(j+1)-PAD, CELLULE_SIZE*(i+1)-PAD)
			if val > 0:
				canvas.create_rectangle(r, width=1, fill=COLOR_SURVIVE_CELLULE)


trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
start_point(START)
end_point(END)
carrots(MAT)

canvas.pack(expand=False)
root.mainloop()
