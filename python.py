import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(900,900)
    w.setWindowTitle("HallBass")
    w.show()
    sys.exit(app.exec_())