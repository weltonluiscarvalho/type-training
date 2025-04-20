from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

class TypeCheckLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

app = QApplication()

texto = "O que fazemos hoje ecoa pela eternidade"

label = TypeCheckLabel(texto)
label.setAlignment(Qt.AlignCenter)

font = QFont()
font.setPointSize(50)
label.setFont(font)
label.setWordWrap(True)
label.setTextInteractionFlags(Qt.TextSelectableByMouse)

label.show()

app.exec()
