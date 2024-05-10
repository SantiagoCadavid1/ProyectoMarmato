import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bienvenido")

        # Crear la etiqueta y ubicarla en el centro de la pantalla
        self.label = QLabel("¡Bienvenido a mi aplicación!", self)
        self.label.setAlignment(Qt.AlignCenter)  # Centrar el texto en la etiqueta
        self.adjust_label_position()  # Ajustar la posición de la etiqueta inicialmente

    def adjust_label_position(self):
        # Obtener la geometría de la pantalla
        desktop_geometry = QApplication.desktop().screenGeometry()

        # Calcular las coordenadas para el centro vertical y horizontal
        center_x = desktop_geometry.width() // 2
        center_y = desktop_geometry.height() // 2

        # Configurar la geometría de la etiqueta para que esté centrada en la pantalla
        self.label.setGeometry(center_x - 150, center_y - 50, 300, 100)

    def resizeEvent(self, event):
        # Llamar a la función para ajustar la posición de la etiqueta cada vez que la ventana se redimensiona
        self.adjust_label_position()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())

