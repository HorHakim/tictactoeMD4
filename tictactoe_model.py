import numpy
import random

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


	def get_empty_cells(self):
		empty_cells = []
		for row in range(0,3):
			for col in range(0,3):
				if self.grid[row, col] == 0:
					empty_cells.append((row, col))

		return empty_cells




	def get_optimal_move(self):
		if numpy.all(self.grid==0):
			return random.randint(0, 2), random.randint(0, 2)

		best_score = -float("inf")
		best_row, best_col = None, None
		
		for row, col in self.get_empty_cells():

			self.grid[row, col] = 1
			score = self.minimax_pruning(robot_turn=False)
			if score > best_score:
				best_score = score 
				best_row, best_col = row, col
			self.grid[row, col] = 0

		return best_row, best_col


	def minimax(self, robot_turn=False):
		winner = self.check_winner()
		if winner:
			return winner

		elif not self.check_game_progress():
			return 0

		# la partie back tracking qui parcours l'arbre des possibles
		best_score = -float("inf") if robot_turn else float("inf")
		for row, col in self.get_empty_cells():
			self.grid[row, col] = 1 if robot_turn else -1
			
			score = self.minimax(not robot_turn)
			best_score = max(score, best_score) if robot_turn else min(score, best_score)
			
			self.grid[row, col] = 0

		return best_score



	def minimax_pruning(self, robot_turn=False, alpha=-float("inf"), beta=float("inf")):
		winner = self.check_winner()
		if winner:
			return winner

		elif not self.check_game_progress():
			return 0

		# la partie back tracking qui parcours l'arbre des possibles
		best_score = -float("inf") if robot_turn else float("inf")
		for row, col in self.get_empty_cells():
			self.grid[row, col] = 1 if robot_turn else -1
			
			score = self.minimax_pruning(not robot_turn, alpha, beta)

			self.grid[row, col] = 0

			if robot_turn:
				best_score = max(score, best_score)
				alpha = max(alpha, score)
			else:
				best_score = min(score, best_score)
				beta = min(beta, score)

			if beta <= alpha:
				return best_score
		
		return best_score



	def check_winner(self):
		for verification_kernel in self.verfication_kernels:
			if (self.grid * verification_kernel).sum() == 3:
				return 1
			elif (self.grid * verification_kernel).sum() == -3:
				return -1


	def check_game_progress(self):
		return numpy.any(self.grid==0)





		