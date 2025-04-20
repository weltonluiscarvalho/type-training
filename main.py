from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel


app = QApplication()

texto = "O que fazemos hoje ecoa pela eternidade"

label = QLabel(texto)
label.setAlignment(Qt.AlignCenter)

font = QFont()
font.setPointSize(50)
label.setFont(font)
label.setWordWrap(True)
label.setTextInteractionFlags(Qt.TextSelectableByMouse)

label.show()

app.exec()
