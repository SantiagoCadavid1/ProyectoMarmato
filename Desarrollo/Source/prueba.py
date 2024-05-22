import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Menu Example")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()

        # Crear y almacenar los dos menús como atributos de la clase
        self.menu1 = QWidget(self)
        self.init_menu1()

        # Mostrar el primer menú
        self.setCentralWidget(self.menu1)

    def init_menu1(self):
        label = QLabel('Primero', self.menu1)
        label.move(481, 154)
        button = QPushButton('Siguiente', self.menu1)
        button.setGeometry(188, 377, 200, 50)
        button.clicked.connect(self.show_menu2)

    def init_menu2(self):
        label = QLabel('Segundo', self.menu2)
        label.move(481, 154)
        button = QPushButton('Anterior', self.menu2)
        button.setGeometry(751, 377, 200, 50)
        button.clicked.connect(self.show_menu1)

    def show_menu1(self):
        self.menu1 = QWidget(self)
        self.init_menu1()
        self.setCentralWidget(self.menu1)

    def show_menu2(self):
        self.menu2 = QWidget(self)
        self.init_menu2()
        self.setCentralWidget(self.menu2)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
