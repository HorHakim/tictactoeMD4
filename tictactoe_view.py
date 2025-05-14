from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic

import os

class TicTacToeView(QMainWindow):
	def __init__(self):
		super(TicTacToeView, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "tictactoe.ui"), self)
		self.symbols = {f"player_{i}" : QIcon(QPixmap(f"./player_{i}.png")) for i in [1, 2]}
		self.show()



	def check_cell(self, row, col, current_turn):
		self.findChild(QPushButton, f"pb_{row}_{col}").setIcon(self.symbols[f"player_{current_turn}"])
		self.findChild(QPushButton, f"pb_{row}_{col}").setEnabled(False)

	def display_game_status(self, winner):
		# if winner:
		# 	self.game_state_label.setText(f"le gagnant est le player {1 if winner == 1 else 2}")
		# else:
		# 	self.game_state_label.setText("Match nul")


		self.game_state_label.setText('winner : 1' if winner == 1 else ('winner : 2' if winner == -1 else 'Match nul'))

		for row in range (0, 3):
			for col in range (0, 3):
				self.findChild(QPushButton, f"pb_{row}_{col}").setEnabled(False)


