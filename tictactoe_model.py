import numpy


class TicTacToeModel:
	def __init__(self):
		self.grid = numpy.zeros(shape=(3,3))
		self.turn = 1
		self.game_in_progress = True
		self.winner = None
		self.generate_verification_kernels()


	def generate_verification_kernels(self):
		self.verfication_kernels = [] # step 0 : générer un liste contenant les noyaux de vérification : 8 éléments
		self.verfication_kernels.append(numpy.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))
		self.verfication_kernels.append(numpy.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))
		self.verfication_kernels.append(numpy.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]]))

		self.verfication_kernels.append(numpy.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]]))
		self.verfication_kernels.append(numpy.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))
		self.verfication_kernels.append(numpy.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]]))

		self.verfication_kernels.append(numpy.identity(3))
		self.verfication_kernels.append(numpy.fliplr(numpy.identity(3)))

		# self.verfication_kernels = [] # step 0 : générer un liste contenant les noyaux de vérification : 8 éléments
		# up_row = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
		# right_col = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
		# self.verfication_kernels.append(numpy.array(up_row))
		# self.verfication_kernels.append(numpy.flip(up_row))
		# self.verfication_kernels.append(numpy.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))

		# self.verfication_kernels.append(numpy.array(right_col))
		# self.verfication_kernels.append(numpy.flip(right_col))
		# self.verfication_kernels.append(numpy.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))

		# self.verfication_kernels.append(numpy.identity(3))
		# self.verfication_kernels.append(numpy.fliplr(numpy.identity(3)))


	def human_move(self, row, col):
		self.grid[row, col] = 1 if self.turn == 1 else -1
		self.turn = 2 if self.turn == 1 else 1


		self.game_in_progress = self.check_game_progress()
		self.winner = self.check_winner()

		if self.winner:
			self.game_in_progress = False



	def robot_move(self):
		row, col = self.get_optimal_move()
		self.grid[row, col] = 1 if self.turn == 1 else -1
		self.turn = 2 if self.turn == 1 else 1


		self.game_in_progress = self.check_game_progress()
		self.winner = self.check_winner()

		if self.winner:
			self.game_in_progress = False

		return row, col

	def get_optimal_move(self):
		for row in range(0,3):
			for col in range(0,3):
				if self.grid[row, col] == 0:
					return row, col



	def check_winner(self):
		for verification_kernel in self.verfication_kernels:
			if (self.grid * verification_kernel).sum() == 3:
				return 1
			elif (self.grid * verification_kernel).sum() == -3:
				return -1


	def check_game_progress(self):
		return numpy.any(self.grid==0)





		