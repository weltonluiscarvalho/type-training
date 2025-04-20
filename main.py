from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QKeyEvent
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class TypeCheckLabel(QLabel):
    def __init__(self, target_text, parent=None):
        super().__init__(parent)
        self.target_text = target_text
        self.current_position = 0
        self.correct_color = QColor("#2ecc71")
        self.wrong_color = QColor("#e74c3c")
        self.default_color = QColor("#000000")

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-size: 50px; padding: 20px; border: 1px solid black;") 
        self.setWordWrap(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.update_dysplay()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def update_dysplay(self):
        html_text = ""

        for i, char in enumerate(self.target_text):
            if i < self.current_position:
                html_text += f'<span style="color:{self.correct_color.name()}">{char}</span>'
            elif i == self.current_position:
                html_text += f'<span style="color:{self.default_color.name()}; background-color:#f1c40f;">{char}</span>'
            else:
                html_text += f'<span style="color:{self.default_color.name()}">{char}</span>'

        self.setText(html_text)

    def keyPressEvent(self, event: QKeyEvent):
        if self.current_position >= len(self.target_text):
            return

        if event.key() in (Qt.Key.Key_Shift, Qt.Key.Key_Control, Qt.Key.Key_Alt, Qt.Key.Key_CapsLock):
            return

        if event.key() == Qt.Key.Key_Backspace:
            if self.current_position > 0:
                self.current_position -= 1
                self.update_dysplay()
            return

        expected_char = self.target_text[self.current_position]
        if event.text() == expected_char:
            self.current_position += 1
            self.update_dysplay()

            if self.current_position == len(self.target_text):
                self.setText(f'<span style="color:{self.correct_color.name()}">{self.target_text}</span>')
                self.setStyleSheet("font-size: 50px; padding: 20px; border: 3px solid #2ecc71;")

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
