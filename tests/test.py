import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Install PyQt using the following command: "pip install PyQt5" after installing python on PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(900,900)
    w.setWindowTitle("HallBass")
    w.show()
    sys.exit(app.exec_())