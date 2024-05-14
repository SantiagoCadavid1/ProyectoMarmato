import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QMessageBox, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap, QIcon

class WindowNavigator:
    def __init__(self, stacked_widget, menu_principal, menu_usuarios):
        self.stacked_widget = stacked_widget
        self.menu_principal = menu_principal
        self.menu_usuarios = menu_usuarios

    def navigate_to_principal(self):
        self.stacked_widget.setCurrentWidget(self.menu_principal)

    def navigate_to_usuarios(self):
        self.stacked_widget.setCurrentWidget(self.menu_usuarios)

class MainWindow(QMainWindow):
    tamañoFuentePrincipal = 40
    tamañoFuenteTitulos = 120
    colorFuente = "#5E5E5E"
    tipografia = "Poppins"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_principal = MenuPrincipal(self)
        self.stacked_widget.addWidget(self.menu_principal)

        self.menu_usuarios = MenuUsuarios(self)
        self.stacked_widget.addWidget(self.menu_usuarios)

        self.window_navigator = WindowNavigator(self.stacked_widget, self.menu_principal, self.menu_usuarios)

        self.stacked_widget.setCurrentWidget(self.menu_principal)

class MenuPrincipal(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Menu Principal")

        self.create_clock_widget()
        self.create_label()
        self.create_buttons()

        layout = QGridLayout()
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.clock_widget, 0, 0)
        layout.addWidget(self.main_widget, 2, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 8)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def create_clock_widget(self):
        self.clock_widget = QLabel("", self)
        self.clock_widget.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.clock_widget.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")

    def create_label(self):
        self.label = QLabel("Bienvenido", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(f"font-size: {MainWindow.tamañoFuenteTitulos}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}; font-weight: bold")

    def create_buttons(self):
        self.main_widget = QWidget(self)
        self.boton_usuarios = self.create_button("Desarrollo/Assets/menuPrincipal/usuarios.png", self.on_usuarios_clicked)
        self.boton_pedidos = self.create_button("Desarrollo/Assets/menuPrincipal/pedidos.png", self.on_pedidos_clicked)
        self.boton_servicios = self.create_button("Desarrollo/Assets/menuPrincipal/servicios.png", self.on_servicios_clicked)
        self.boton_informes = self.create_button("Desarrollo/Assets/menuPrincipal/informes.png", self.on_informes_clicked)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.boton_usuarios, 0, 0)
        self.main_layout.addWidget(self.boton_pedidos, 0, 1)
        self.main_layout.addWidget(self.boton_servicios, 1, 0)
        self.main_layout.addWidget(self.boton_informes, 1, 1)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(400, 10, 400, 10)

    def create_button(self, icon_path, on_clicked):
        button = QPushButton("", self)
        self.set_icon(button, icon_path)
        button.clicked.connect(on_clicked)
        self.configure_button(button)
        return button

    def set_icon(self, button, icon_path):
        pixmap = QPixmap(icon_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
        button.setStyleSheet("border: none; padding: 0px;")

    def configure_button(self, button):
        button.setStyleSheet("border: none; background-color: transparent; padding: 0px;")

    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)

    def on_usuarios_clicked(self):
        self.parent.window_navigator.navigate_to_usuarios()

    def on_pedidos_clicked(self):
        QMessageBox.information(self, "Pedidos", "Se presionó el botón de Pedidos")

    def on_servicios_clicked(self):
        QMessageBox.information(self, "Servicios", "Se presionó el botón de Servicios")

    def on_informes_clicked(self):
        QMessageBox.information(self, "Informes", "Se presionó el botón de Informes")

class MenuUsuarios(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Menu Usuarios")

        self.create_clock_widget()
        self.create_label()
        self.create_buttons()

        layout = QGridLayout()
        layout.addWidget(self.clock_widget, 0, 0)
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.main_widget, 2, 0)
        layout.addWidget(self.button_widget, 3, 0, alignment=Qt.AlignRight)  # Alinea el botón a la derecha
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 7)
        layout.setRowStretch(3, 1)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def create_clock_widget(self):
        self.clock_widget = QLabel("", self)
        self.clock_widget.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.clock_widget.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")

    def create_label(self):
        self.label = QLabel("Usuarios", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(f"font-size: {MainWindow.tamañoFuenteTitulos}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}; font-weight: bold")

    def create_buttons(self):
        self.main_widget = QWidget(self)
        self.boton_agregar = self.create_button("Desarrollo/Assets/menuUsuarios/agregar_usuario.png", self.on_agregar_clicked)
        self.boton_editar = self.create_button("Desarrollo/Assets/menuUsuarios/editar_usuario.png", self.on_editar_clicked)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.boton_agregar, 0, 0)
        self.main_layout.addWidget(self.boton_editar, 0, 1)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(266, 10, 266, 10)
        
        self.button_widget = QWidget(self)
        self.boton_atras = self.create_button("Desarrollo/Assets/menuUsuarios/atras.png", self.on_atras_clicked)
        self.button_layout = QGridLayout()
        self.button_layout.addWidget(self.boton_atras, 0, 0)
        self.button_widget.setLayout(self.button_layout)
        self.button_layout.setContentsMargins(40, 40, 40, 40)

    def create_button(self, icon_path, on_clicked):
        button = QPushButton("", self)
        self.set_icon(button, icon_path)
        button.clicked.connect(on_clicked)
        self.configure_button(button)
        return button

    def set_icon(self, button, icon_path):
        pixmap = QPixmap(icon_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
        button.setStyleSheet("border: none; padding: 0px;")

    def configure_button(self, button):
        button.setStyleSheet("border: none; background-color: transparent; padding: 0px;")

    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)

    def on_agregar_clicked(self):
        QMessageBox.information(self, "Agregar", "Se presionó el botón de Agregar")

    def on_editar_clicked(self):
        QMessageBox.information(self, "Editar", "Se presionó el botón de Editar")

    def on_atras_clicked(self):
        self.parent.window_navigator.navigate_to_principal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
