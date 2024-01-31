"""

"""

class MaxRewards:
	def __init__(self, matrix, start, end):
		self.matrix = matrix
		self.start = start
		self.end = end
		check = self.check_params()
		if check[0]:
			print(check[1])
			pass
		else:
			print(check[1])
			exit (0)
	
	def check_entry(self, entry, values_checking):
		v1, v2 = values_checking
		return True if entry[0] >= 0 and entry[0] < v1 and entry[1] >= 0 and entry[1] < v2 else False
			
	def check_params(self):
		self.N_ROWS = len(self.matrix)
		self.N_COLS = len(self.matrix[0])
		checking = True
		comment = ''
		len_matrix = (self.N_ROWS, self.N_COLS)
		if self.check_entry(self.start, len_matrix):
			comment += 'Entry OK Start\n'
		else:
			comment += 'Entry NOK Start\n'
			checking = False
		if self.check_entry(self.end, len_matrix):
			comment += 'Entry OK End\n'
		else:
			comment += 'Entry NON End\n'
			checking = False
		e1, e2 = self.end
		if self.check_entry(self.start, (e1+1, e2+1)):
			comment += 'Entry OK Start - End\n'
		else:
			comment += 'Entry NOK Start > End\n'
			checking = False
		return checking, comment
		
			
