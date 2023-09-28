from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
import random
import sys

class NumberGame(QWidget):
    def __init__(self):
        super(NumberGame, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CAKO Number')
        self.setFixedSize(800, 800)

        vbox = QVBoxLayout()
        
        # CAKO CHAN Image
        self.cako_chan = QGraphicsView(self)
        self.cako_scene = QGraphicsScene()
        self.cako_pixmap = QPixmap("cako.png")
        self.cako_scene.addPixmap(self.cako_pixmap)
        self.cako_chan.setScene(self.cako_scene)
        self.cako_chan.setFixedWidth(400)  # 幅を調整:width cako chan
        self.cako_chan.setFixedHeight(400)  # 高さを調整 height cako chan

        # Instruction label
        instruction_label = QLabel("HOW TO\n\nClick -1 small number which CAKO CHAN calls.")
        instruction_label.setAlignment(Qt.AlignCenter)
        instruction_label.setFont(QFont("Arial", 12))

        # Horizontal layout for CAKO CHAN image and instruction
        hbox_cako = QHBoxLayout()
        hbox_cako.addWidget(self.cako_chan)
        hbox_cako.addWidget(instruction_label)

        # Question label
        self.question_label = QLabel("READY")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setFont(QFont("Arial", 24))
        vbox.addLayout(hbox_cako)
        vbox.addWidget(self.question_label)

        # Number buttons
        self.num_buttons = []
        for i in range(1, 50):
            button = QPushButton(str(i))
            button.clicked.connect(self.checkAnswer)
            self.num_buttons.append(button)

        # Arrange buttons in 7x7 grid
        hbox = QHBoxLayout()
        counter = 0
        for i in range(7):
            vbox_inner = QVBoxLayout()
            for j in range(7):
                vbox_inner.addWidget(self.num_buttons[counter])
                counter += 1
            hbox.addLayout(vbox_inner)
            
        vbox.addLayout(hbox)

        # Text box for messages
        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)
        vbox.addWidget(self.text_box)

        # Restart and Exit buttons
        self.restart_button = QPushButton("Restart")
        self.restart_button.clicked.connect(self.restartGame)
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        hbox_bottom = QHBoxLayout()
        hbox_bottom.addWidget(self.restart_button)
        hbox_bottom.addWidget(self.exit_button)
        vbox.addLayout(hbox_bottom)

        self.setLayout(vbox)

        # Initialize game variables
        self.correct_answers = 0
        self.current_question = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(4000) #number display time

    def checkAnswer(self):
        sender = self.sender()
        clicked_number = int(sender.text())
        if clicked_number == self.current_question - 1:
            self.correct_answers += 1
            self.text_box.append("GOOD!")
            if self.correct_answers >= 20:
                self.question_label.setText("WIN!")
                self.timer.stop()
        else:
            self.text_box.append("OOPS!")
            self.question_label.setText("GAME OVER")
            self.timer.stop()

    def restartGame(self):
        self.correct_answers = 0
        self.current_question = 0
        self.question_label.setText("READY")
        self.text_box.clear()
        self.timer.start(4000) #number display time

    def updateGame(self):
        self.current_question = random.randint(1, 50)
        self.question_label.setText(str(self.current_question))

if __name__ == '__main__':
    app = QApplication([])
    game_window = NumberGame()
    game_window.show()
    sys.exit(app.exec_())
