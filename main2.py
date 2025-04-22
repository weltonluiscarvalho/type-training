
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Type Training")

        text = "O que fazemos hoje ecoa pela eternidade"
        self.menuBar()

        widget = QWidget()

        layout = QVBoxLayout(widget)

        label = QLabel('Vou correr 16km hoje!')
        label.setStyleSheet('font-size: 50px')

        layout.addWidget(label)

        self.setCentralWidget(widget)

        # self.type_label = TypeCheckLabel(text)
        # self.hits = QLabel(f"Acertos: {self.type_label.acertos}")
        # self.errors = QLabel(f"Erros: {self.type_label.errors}")
        # self.hits.setStyleSheet("font-size: 30px; padding: 20px; border: 1px solid black;") 
        # self.errors.setStyleSheet("font-size: 30px; padding: 20px; border: 1px solid black;") 
        # layout = QVBoxLayout()
        # layout.addWidget(self.type_label)
        # layout.addWidget(self.hits)
        # layout.addWidget(self.errors)
        # self.setLayout(layout)

    # def update_label(self):
    #     self.hits.setText(f"Acertos: {self.type_label.acertos}")
    #     self.errors.setText(f"Erros: {self.type_label.errors}")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
