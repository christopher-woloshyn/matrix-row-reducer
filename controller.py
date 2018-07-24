import matrix

class Controller:
	def __init__(self, filename):
		self.filename = "inputs.txt"
		self.readFile()

		mat = matrix.Matrix(self.rows, self.cols, self.matrix)
		mat.reduce()

	def readFile(self):
		inputs = open(self.filename, 'r')
		row_cols = list(map(int, inputs.readline().split()))
		self.rows = row_cols[0]
		self.cols = row_cols[1]
		self.matrix = [list(map(int, inputs.readline().split())) for j in range(self.rows)]
		inputs.close()
