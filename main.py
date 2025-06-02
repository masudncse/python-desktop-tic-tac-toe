import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QGridLayout, QWidget, QLabel, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(400, 500)
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Status label
        self.status_label = QLabel("Player X's turn")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont('Arial', 16))
        main_layout.addWidget(self.status_label)
        
        # Game board
        self.board_widget = QWidget()
        self.board_layout = QGridLayout(self.board_widget)
        self.board_layout.setSpacing(5)
        self.buttons = []
        
        # Create buttons
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.setFont(QFont('Arial', 40))
                button.clicked.connect(lambda checked, row=i, col=j: self.make_move(row, col))
                self.board_layout.addWidget(button, i, j)
                self.buttons.append(button)
        
        main_layout.addWidget(self.board_widget)
        
        # Reset button
        reset_button = QPushButton("New Game")
        reset_button.setFont(QFont('Arial', 14))
        reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(reset_button)
        
        # Style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: white;
                border: 2px solid #cccccc;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
            QLabel {
                color: #333333;
            }
        """)

    def make_move(self, row, col):
        if self.game_over:
            return
            
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].setText(self.current_player)
            
            if self.check_winner():
                self.status_label.setText(f"Player {self.current_player} wins!")
                self.game_over = True
            elif "" not in self.board:
                self.status_label.setText("It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.setText(f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows, columns and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.status_label.setText("Player X's turn")
        for button in self.buttons:
            button.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec()) 