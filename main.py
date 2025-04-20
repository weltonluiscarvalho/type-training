from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class TypeCheckLabel(QLabel):
    def __init__(self, target_text, parent=None):
        super().__init__(parent)
        self.target_text = target_text
        self.current_position = 0
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(50)
        self.setFont(font)
        self.setWordWrap(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.update_dysplay()

    def update_dysplay(self):
        html_text = self.target_text
        self.setText(html_text)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Type Training")

        text = "O que fazemos hoje ecoa pela eternidade"

        self.type_label = TypeCheckLabel(text)
        layout = QVBoxLayout()
        layout.addWidget(self.type_label)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
