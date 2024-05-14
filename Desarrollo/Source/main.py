import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap, QIcon
class MainWindow(QMainWindow):
    # Definición de variables generales
    tamañoFuentePrincipal = 40
    tamañoFuenteSecundario = 44
    tamañoFuenteTitulos = 120
    colorFuente = "#5E5E5E"
    tipografia = "Poppins"

    def __init__(self):
        super().__init__()

    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)

class MenuPrincipal(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")

        # Configurar el widget del reloj con las variables definidas
        self.clock_widget = QLabel("", self)
        self.clock_widget.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.clock_widget.setStyleSheet(f"font-size: {self.tamañoFuentePrincipal}px; color: {self.colorFuente}; font-family: {self.tipografia}")

        # Configurar el mensaje de bienvenida con las variables definidas y centrarlo
        self.label = QLabel("Bienvenido", self)
        self.label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente y verticalmente
        self.label.setStyleSheet(f"font-size: {self.tamañoFuenteTitulos}px; color: {self.colorFuente}; font-family: {self.tipografia}; font-weight: bold")
        
        # Configurar el widget de los botones
        self.boton_usuarios = QPushButton("", self)
        self.set_icon(self.boton_usuarios, "Desarrollo/Assets/menuPrincipal/usuarios.png")
        self.boton_usuarios.clicked.connect(self.on_usuarios_clicked)
        self.configure_button(self.boton_usuarios)

        self.boton_pedidos = QPushButton("", self)
        self.set_icon(self.boton_pedidos, "Desarrollo/Assets/menuPrincipal/pedidos.png")
        self.boton_pedidos.clicked.connect(self.on_pedidos_clicked)
        self.configure_button(self.boton_pedidos)

        self.boton_servicios = QPushButton("", self)
        self.set_icon(self.boton_servicios, "Desarrollo/Assets/menuPrincipal/servicios.png")
        self.boton_servicios.clicked.connect(self.on_servicios_clicked)
        self.configure_button(self.boton_servicios)

        self.boton_informes = QPushButton("", self)
        self.set_icon(self.boton_informes, "Desarrollo/Assets/menuPrincipal/informes.png")
        self.boton_informes.clicked.connect(self.on_informes_clicked)
        self.configure_button(self.boton_informes)

        
        self.main_widget = QWidget(self)
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.boton_usuarios, 0, 0)
        self.main_layout.addWidget(self.boton_pedidos, 0, 1)
        self.main_layout.addWidget(self.boton_servicios, 1, 0)
        self.main_layout.addWidget(self.boton_informes, 1, 1)
        self.main_widget.setLayout(self.main_layout)
        
        # Reducir el espacio alrededor de los botones
        self.main_layout.setContentsMargins(266, 10, 266, 10)

        # Crear un layout de cuadrícula y agregar widgets
        layout = QGridLayout()
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.clock_widget, 0, 0)
        layout.addWidget(self.main_widget, 2, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 8)

        # Crear un widget central para contener el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Iniciar el temporizador para actualizar el reloj
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
    def set_icon(self, button, icon_path):
        pixmap = QPixmap(icon_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
        button.setStyleSheet("border: none; padding: 0px;")
        
    def configure_button(self, button):
        button.setStyleSheet("border: none; background-color: transparent; padding: 0px;")

        
    def on_usuarios_clicked(self):
        QMessageBox.information(self, "Pedidos", "Se presionó el botón de Usuarios")

    def on_pedidos_clicked(self):
        QMessageBox.information(self, "Pedidos", "Se presionó el botón de Pedidos")

    def on_servicios_clicked(self):
        QMessageBox.information(self, "Servicios", "Se presionó el botón de Servicios")

    def on_informes_clicked(self):
        QMessageBox.information(self, "Informes", "Se presionó el botón de Informes")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuPrincipal()
    window.showMaximized()
    sys.exit(app.exec_())
