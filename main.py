from PyQt5.QtWidgets import QApplication
import tictactoe_controller

if __name__ == '__main__':
    app = QApplication([])
    tictactoe_controller_object = tictactoe_controller.TicTacToeController()
    app.exec_()