from PySide6.QtWidgets import QApplication
from model.temperature import Temperature


if __name__ == "__main__":
    app = QApplication()  
    w = Temperature()
    w.show()

    app.exec()  