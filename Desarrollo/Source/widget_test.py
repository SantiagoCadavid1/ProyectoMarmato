import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QTime


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        self.setGeometry(0, 0, 1920, 1080)

        # Fondo de la ventana
        self.set_background_image("Desarrollo/Assets/Pruebas/fondo.png")

        # Label de la hora actual
        self.clock_widget = QLabel("", self)
        self.clock_widget.setGeometry(1652, 60, 179, 60)
        self.clock_widget.setStyleSheet("color: #FFFFFF; font-size: 40px; font-family: Poppins;")

        # Timer para actualizar la hora cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()  # Actualizar la hora inicial

        # Botón con imagen transparente
        self.create_image_button("Desarrollo/Assets/Pruebas/cerrar.png", 39, 39, 1406, 258, self.close, True)

        # Entradas de texto con bordes redondeados
        self.entry1 = self.create_entry(957, 447, 434, 52)
        self.entry2 = self.create_entry(957, 529, 434, 52)
        
        options = ["Seleccionar", "Administrador", "Operario", "Usuario", "Visitante", "Cliente"]
        self.entry3 = self.create_dropdown_menu(957, 611, 434, 52, options)

        # Botón sin imagen sin bordes
        self.create_text_button("Cancelar", 762, 727, 168, 40, 36, "#727272", "Poppins", self.cancel_action, False)

        # Botón con imagen transparente
        self.create_image_button("Desarrollo/Assets/Pruebas/siguiente.png", 201, 60, 957, 717, self.next_action, True)

    def set_background_image(self, image_path):
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), Qt.transparent)
        self.setPalette(palette)
        pixmap = QPixmap(image_path)
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1920, 1080)
        self.background_label.setPixmap(pixmap.scaled(1920, 1080))

    def create_label(self, text, x, y, width, height, font_size, font_color, font_family):
        label = QLabel(text, self)
        label.setGeometry(x, y, width, height)
        label.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")

    def create_image_button(self, image_path, width, height, x, y, action, transparent):
        button = QPushButton(self)
        button.setGeometry(x, y, width, height)
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.size())
        button.clicked.connect(action)
        if transparent:
            button.setStyleSheet("background-color: transparent; border: none;")

    def create_text_button(self, text, x, y, width, height, font_size, font_color, font_family, action, no_border):
        button = QPushButton(text, self)
        button.setGeometry(x, y, width, height)
        button.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")
        button.clicked.connect(action)
        if no_border:
            button.setStyleSheet("background-color: transparent; border: none;")  # Removiendo el borde

            
    def create_dropdown_menu(self, x, y, width, height, options):
        dropdown_menu = QComboBox(self)
        dropdown_menu.setGeometry(x, y, width, height)
        dropdown_menu.addItems(options)
        return dropdown_menu

    def create_entry(self, x, y, width, height):
        entry = QLineEdit(self)
        entry.setGeometry(x, y, width, height)
        entry.setStyleSheet("font-size: 36px; font-family: Poppins; color: #727272; border-radius: 10px;")
        return entry

    def cancel_action(self):
        print("Cancelar acción")

    def next_action(self):
        print("Siguiente acción")

    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
