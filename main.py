from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QKeyEvent
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class TypeCheckLabel(QLabel):
    def __init__(self, target_text, parent=None):
        super().__init__(parent)
        self.errors = 0
        self.acertos = 0
        self.target_text = target_text
        self.current_position = 0
        self.correct_color = QColor("#2ecc71")
        self.wrong_color = QColor("#e74c3c")
        self.default_color = QColor("#000000")

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-size: 50px; padding: 20px; border: 1px solid black;") 
        self.setWordWrap(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.update_dysplay("#f1c40f")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def update_dysplay(self, background_color):
        html_text = ""

        for i, char in enumerate(self.target_text):
            if i < self.current_position:
                html_text += f'<span style="color:{self.correct_color.name()}">{char}</span>'
            elif i == self.current_position:
                html_text += f'<span style="color:{self.default_color.name()}; background-color:{background_color};">{char}</span>'
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
                self.update_dysplay("#f1c40f")
            return

        expected_char = self.target_text[self.current_position]
        if event.text() == expected_char:
            self.current_position += 1
            self.acertos += 1
            self.update_dysplay("#f1c40f")
            self.parentWidget().update_label()

            if self.current_position == len(self.target_text):
                self.setText(f'<span style="color:{self.correct_color.name()}">{self.target_text}</span>')
                self.setStyleSheet("font-size: 50px; padding: 20px; border: 3px solid #2ecc71;")
                print(f"O numero de erros foi {self.errors}")

        else:
            self.errors += 1
            self.update_dysplay("#e74c3c")
            self.parentWidget().update_label()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Type Training")

        text = "O que fazemos hoje ecoa pela eternidade"

        self.type_label = TypeCheckLabel(text)
        self.hits = QLabel(f"Acertos: {self.type_label.acertos}")
        self.errors = QLabel(f"Erros: {self.type_label.errors}")
        layout = QVBoxLayout()
        layout.addWidget(self.type_label)
        layout.addWidget(self.hits)
        layout.addWidget(self.errors)
        self.setLayout(layout)

    def update_label(self):
        self.hits.setText(f"Acertos: {self.type_label.acertos}")
        self.errors.setText(f"Erros: {self.type_label.errors}")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
