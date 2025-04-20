from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

class TypeCheckLabel(QLabel):
    def __init__(self, target_text, parent=None):
        super().__init__(parent)
        self.target_text = target_text
        self.current_position = 0

        self.update_dysplay()

    def update_dysplay(self):
        html_text = self.target_text
        self.setText(html_text)

app = QApplication()

texto = "O que fazemos hoje ecoa pela eternidade"

label = TypeCheckLabel(target_text=texto)
label.setAlignment(Qt.AlignCenter)

font = QFont()
font.setPointSize(50)
label.setFont(font)
label.setWordWrap(True)
label.setTextInteractionFlags(Qt.TextSelectableByMouse)

label.show()

app.exec()
