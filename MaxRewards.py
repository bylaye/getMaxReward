"""

"""

class MaxRewards:

	def __init__(self, matrix, start, end):
		self.matrix = matrix
		self.start = start
		self.end = end
		check = self._check_params()
		if check[0]:
			self.max_rewards, self.itineraries = self._process()
			self.movements = self._movements(self.itineraries)
		else:
			print(check[1])
			print(f'Exit program')
			exit (0)
	
	def _check_entry(self, entry, values_checking):
		v1, v2 = values_checking
		return True if entry[0] >= 0 and entry[0] < v1 and entry[1] >= 0 and entry[1] < v2 else False
			
	def _check_params(self):
		self.N_ROWS = len(self.matrix)
		self.N_COLS = len(self.matrix[0])
		checking = True
		comment = ''
		len_matrix = (self.N_ROWS, self.N_COLS)
		if self._check_entry(self.start, len_matrix):
			comment += 'Entry OK Start\n'
		else:
			comment += 'Entry NOK Start\n'
			checking = False
		if self._check_entry(self.end, len_matrix):
			comment += 'Entry OK End\n'
		else:
			comment += 'Entry NON End\n'
			checking = False
		e1, e2 = self.end
		if self._check_entry(self.start, (e1+1, e2+1)):
			comment += 'Entry OK Start - End\n'
		else:
			comment += 'Entry NOK Start > End\n'
			checking = False
		return checking, comment
		
	def _process(self):
		sx, sy = self.start
		ex, ey = self.end
		ex, ey = ex+1, ey+1
		reward_tab = [[0]*ey for _ in range(ex)]
		path = [[None]*ey for _ in range(ex)]
		reward_tab[sx][sy] = self.matrix[sx][sy]
		for i in range(sx, ex):
			for j in range(sy, ey):
				left = [reward_tab[i][j-1],(i,j-1)] if i >= sx and j > sy else [0, self.start]
				top = [reward_tab[i-1][j], (i-1, j)] if i>sx else [0, self.start]
				m = max(left, top)
				reward_tab[i][j] = m[0] + self.matrix[i][j]
				path[i][j] = m[1]
		itineraire = self._itineraries(path)
		return reward_tab[-1][-1], itineraire
		
	def _itineraries(self, path):
		out = [self.end]
		ex, ey = self.end
		pred = (ex, ey)
		while pred != self.start:
			c = path[pred[0]][pred[1]]
			out.append(c)
			pred = (c[0],c[1])
		out.reverse()
		return out
		
	def _movements(self, itineraire):
		out = 's'
		pred = itineraire[0]
		for i in range(1, len(itineraire)):
		    next = itineraire[i]
		    if pred[0] == next[0]:
		        out += '-d'
		    else:
		        out += '-b'
		    pred = next
		return out
	
	def get_max_rewards(self):
		return self.max_rewards
		
	def get_itineraries(self):
		return self.itineraries
		
	def get_movements(self):
		return self.movements
