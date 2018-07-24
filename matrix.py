from fractions import Fraction as frac

class Matrix:
	def __init__(self, rows, cols, matrix):
		self.rows = rows
		self.cols = cols
		self.matrix = matrix

		self.DEBUG = True

	def printMatrix(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(self.matrix[i][j], sep='', end=' ', flush=True)
			print("")
		print("")

	def reduce(self):
		
		if self.DEBUG:
			print("Starting Matrix:")
			print("")
			self.printMatrix()

		for i in range(min(self.rows, self.cols)):

			# Repositions the row vector if the value on the diagonal is 0
			# by switching with the row vector below it. 
			if self.matrix[i][i] == 0:

				try:
					self.matrix[i], self.matrix[i+1] = self.matrix[i+1], self.matrix[i]
				except:
					break

				if self.DEBUG:
					print("Switched row " + str(i+1) + " with row " + str(i+2) + ":")
					print("")
					self.printMatrix()

			# Changes the value on the diagonal to 1 by multiplying the row vector
			# by the inverse of that value.
			if self.matrix[i][i] != 1:

				scalar = frac(1, self.matrix[i][i])
				self.matrix[i] = [j*scalar for j in self.matrix[i]]

				if self.DEBUG:
					print("Multiplied row " + str(i+1) + " by " + str(scalar) + ":")
					print("")
					self.printMatrix()

			# Multiplies one row vector by a scalar, and adds that vector to another row vector in order
			# to isolate the value 1 on the diagonal.
			for j in range(self.rows):
				if j != i:
					if self.matrix[j][i] != 0:
						scalar = -self.matrix[j][i]
						for k in range(self.cols):
							self.matrix[j][k] += self.matrix[i][k]*(scalar)

						if self.DEBUG:
							print("Multiplied row " + str(i+1) + " by " + str(scalar) + " and added the result to row " + str(j+1) + ":")
							print("")
							self.printMatrix()