from PyQt5.QtWidgets import QPushButton

from tictactoe_view import TicTacToeView
from tictactoe_model import TicTacToeModel

from functools import partial

class TicTacToeController:
	def __init__(self):
		self.tictactoe_view_object = TicTacToeView()
		self.tictactoe_model_object = TicTacToeModel()
		self.connect_widgets()

		self.robot_update_grid()


	def connect_widgets(self):
		for row in range(0, 3):
			for col in range(0, 3):
				self.tictactoe_view_object.findChild(QPushButton, f"pb_{row}_{col}").clicked.connect(partial(self.update_game, row, col))


	def update_game(self, row, col):
		current_turn = self.tictactoe_model_object.turn
		self.tictactoe_model_object.human_move(row, col)
		self.tictactoe_view_object.check_cell(row, col, current_turn)

		if not self.tictactoe_model_object.game_in_progress:
			self.tictactoe_view_object.display_game_status(self.tictactoe_model_object.winner)
			return None

		self.robot_update_grid()


	def robot_update_grid(self):
		current_turn = self.tictactoe_model_object.turn
		row, col = self.tictactoe_model_object.robot_move()
		self.tictactoe_view_object.check_cell(row, col, current_turn)

		if not self.tictactoe_model_object.game_in_progress:
			self.tictactoe_view_object.display_game_status(self.tictactoe_model_object.winner)
			return None