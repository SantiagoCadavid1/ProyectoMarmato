import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QMessageBox, QGridLayout, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap, QIcon, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tamañoFuentePrincipal = 40
        self.tamañoFuenteSecundario = 50
        self.tamañoFuenteTitulos = 120
        self.colorFuente = "#5E5E5E"
        self.tipografia = "Poppins"
        self.anchoVentana = 1440       # Ancho por defecto de la ventana
        self.altoVentana = 1024
        
        self.setWindowTitle("Menu Principal")
        self.setGeometry(0, 0, self.anchoVentana, self.altoVentana)
        self.showMaximized()
        
        self.menu_principal=QWidget(self)
        self.menu_usuarios=QWidget(self)
        self.menu_formulario_usuarioN=QWidget(self)
        self.menu_confirmar_usuarioN=QWidget(self)
        self.menu_lista_usuarios=QWidget(self)
        self.menu_editar_usuario=QWidget(self)
        self.menu_eliminar_usuarios=QWidget(self)
        self.menu_pedidos=QWidget(self)
        self.menu_crear_pedido=QWidget(self)
        self.menu_confirmar_pedido=QWidget(self)
        self.menu_lista_pedidos=QWidget(self)
        self.menu_editar_pedido=QWidget(self)
        self.menu_eliminar_pedido=QWidget(self)
        self.menu_servicios=QWidget(self)
        self.menu_visualizar_servicio=QWidget(self)
        self.menu_editar_servicio=QWidget(self)
        self.menu_informes=QWidget(self)
        self.menu_visualizar_informe=QWidget(self)
        
        self.clock_widget = self.create_clock_widget()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.init_menu_principal()
        
        self.setCentralWidget(self.menu_principal)
        
    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)
            
    def create_clock_widget(self):
        clock_widget = QLabel("", self)
        clock_widget.setGeometry(1188, 51, 179, 60)
        clock_widget.setStyleSheet(f"font-size: {self.tamañoFuentePrincipal}px; color: {self.colorFuente}; font-family: {self.tipografia}")
        return clock_widget
    
    def set_background_image(self, image_path):
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), Qt.transparent)
        self.setPalette(palette)
        pixmap = QPixmap(image_path)
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.anchoVentana, self.altoVentana)
        self.background_label.setPixmap(pixmap.scaled(self.anchoVentana, self.altoVentana))
        
    def create_label(self, menu, text, x, y, width, height, font_size, font_color, font_family, flag):
        label = QLabel(text, menu)
        label.setGeometry(x, y, width, height)
        if flag:
            label.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family}; font-weight: bold")  
        else:
            label.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")
        return label
    
    def create_image_button(self, menu, image_path, width, height, x, y, action, transparent):
        button = QPushButton(menu)
        button.setGeometry(x, y, width, height)
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.size())
        button.clicked.connect(action)
        if transparent:
            button.setStyleSheet("background-color: transparent; border: none;")
        return button
    
    def create_hover_image_button(self, menu, normal_image_path, hover_image_path, width, height, x, y, action, transparent):
        button = QPushButton(menu)
        button.setGeometry(x, y, width, height)
        normal_pixmap = QPixmap(normal_image_path)
        hover_pixmap = QPixmap(hover_image_path)
        normal_icon = QIcon(normal_pixmap)
        hover_icon = QIcon(hover_pixmap)
        
        button.setIcon(normal_icon)
        button.setIconSize(normal_pixmap.size())
        button.clicked.connect(action)
        
        if transparent:
            button.setStyleSheet("background-color: transparent; border: none;")
        
        # Define the enterEvent and leaveEvent within the method
        def enterEvent(event):
            button.setIcon(hover_icon)
            super(QPushButton, button).enterEvent(event)

        def leaveEvent(event):
            button.setIcon(normal_icon)
            super(QPushButton, button).leaveEvent(event)

        # Attach the events to the button
        button.enterEvent = enterEvent
        button.leaveEvent = leaveEvent
        
        return button
    
    def create_text_button(self, menu, text, x, y, width, height, font_size, font_color, font_family, action, no_border):
        button = QPushButton(text, menu)
        button.setGeometry(x, y, width, height)
        button.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")
        button.clicked.connect(action)
        if no_border:
            button.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family}; background-color: transparent; border: none;")  # Removiendo el borde
        else:
            button.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")
        return button
    
    def create_dropdown_menu(self, menu, x, y, width, height, options):
        dropdown_menu = QComboBox(menu)
        dropdown_menu.setGeometry(x, y, width, height)
        dropdown_menu.addItems(options)
        return dropdown_menu

    def create_entry(self, menu, x, y, width, height):
        entry = QLineEdit(menu)
        entry.setGeometry(x, y, width, height)
        entry.setStyleSheet("font-size: 36px; font-family: Poppins; color: #727272; border-radius: 10px;")
        return entry

    def init_menu_principal(self):
        self.setWindowTitle("Menu Principal")
        self.clock_widget.setParent(self.menu_principal)  # Asegurarse de que el reloj esté en el menú principal
        self.clock_widget.show()
        
        titulo=self.create_label(self.menu_principal, "Bienvenido", 373, 147, 750, 180, self.tamañoFuenteTitulos, self.colorFuente ,self.tipografia, True)
        
        boton_usuarios = self.create_hover_image_button(self.menu_principal, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 266, 355, self.on_menu_principal_usuarios_clicked, True)
        boton_pedidos = self.create_hover_image_button(self.menu_principal, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 743, 355, self.on_menu_principal_usuarios_clicked, True)
        boton_servicios = self.create_hover_image_button(self.menu_principal, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 266, 633, self.on_menu_principal_usuarios_clicked, True)
        boton_informes = self.create_hover_image_button(self.menu_principal, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 743, 633, self.on_menu_principal_usuarios_clicked, True)
        
    def init_menu_usuarios(self):
        self.setWindowTitle("Menu Usuarios")
        self.clock_widget.setParent(self.menu_usuarios)  # Asegurarse de que el reloj esté en el menú principal
        self.clock_widget.show()
        
        titulo=self.create_label(self.menu_usuarios, "Usuarios", 373, 147, 750, 180, self.tamañoFuenteTitulos, self.colorFuente ,self.tipografia, True)
        
        boton_agregar = self.create_hover_image_button(self.menu_usuarios, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 266, 355, self.on_menu_usuarios_agregar_clicked, True)
        boton_editar = self.create_hover_image_button(self.menu_usuarios, "Desarrollo/Assets/Pruebas/pedro1.png", "Desarrollo/Assets/Pruebas/pedro2.png", 432, 240, 743, 355, self.on_menu_usuarios_editar_clicked, True)
        
        boton_atras = self.create_image_button(self.menu_usuarios, "Desarrollo/Assets/Pruebas/cerebro.png", 143, 63, 1203, 862, self.on_menu_usuarios_atras_clicked, True)
        
    def init_menu_formulario_usuarioN(self):
        self.setWindowTitle("Formulario Usuario Nuevo")
        self.clock_widget.setParent(self.menu_formulario_usuarioN)  # Asegurarse de que el reloj esté en el menú principal
        self.clock_widget.show()
        
        titulo=self.create_label(self.menu_formulario_usuarioN, "Registro", 602, 224, 235, 83, self.tamañoFuenteSecundario, self.colorFuente ,self.tipografia, True)
        
        self.menu_formulario_usuarioN_entry_cedula = self.create_entry(self.menu_formulario_usuarioN, 717, 424, 434, 52)
        self.menu_formulario_usuarioN_entry_nombre = self.create_entry(self.menu_formulario_usuarioN, 717, 506, 434, 52)
        
        options = ["Seleccionar", "Administrador", "Operario", "Usuario", "Visitante", "Cliente"]
        self.menu_formulario_usuarioN_rol_drop = self.create_dropdown_menu(self.menu_formulario_usuarioN, 717, 588, 434, 52, options)
        
        boton_cancelar = self.create_text_button(self.menu_formulario_usuarioN, "Cerrar", 522, 704, 168, 40, self.tamañoFuentePrincipal, self.colorFuente, self.tipografia, self.on_menu_formulario_usuarioN_cancelar_clicked, True)
        boton_aceptar = self.create_image_button(self.menu_formulario_usuarioN, "Desarrollo/Assets/Pruebas/cerebro.png", 201, 60, 694, 717, self.on_menu_formulario_usuarioN_aceptar_clicked, True)
        boton_cerrar = self.create_image_button(self.menu_formulario_usuarioN, "Desarrollo/Assets/Pruebas/cerrar.png", 39, 39, 1166, 210, self.on_menu_formulario_usuarioN_cerrar_clicked, True)

        
    def init_menu_confirmar_usuarioN(self, cedula, nombre, rol):
        self.setWindowTitle("Confirmar Usuario Nuevo")
        self.clock_widget.setParent(self.menu_confirmar_usuarioN)  # Asegurarse de que el reloj esté en el menú principal
        self.clock_widget.show()
        
        boton_cerrar = self.create_image_button(self.menu_confirmar_usuarioN, "Desarrollo/Assets/Pruebas/cerrar.png", 39, 39, 1166, 210, self.on_menu_confirmar_usuarioN_cerrar_clicked, True)
        
        label_cedula=self.create_label(self.menu_confirmar_usuarioN, cedula, 752, 325, 400, 40, self.tamañoFuenteSecundario, self.colorFuente ,self.tipografia, False)
        label_nombre=self.create_label(self.menu_confirmar_usuarioN, nombre, 752, 407, 300, 60, self.tamañoFuenteSecundario, self.colorFuente ,self.tipografia, False)
        label_rol=self.create_label(self.menu_confirmar_usuarioN, rol, 752, 489, 350, 40, self.tamañoFuenteSecundario, self.colorFuente ,self.tipografia, False)
        
        self.menu_confirmar_usuarioN_boton_editar = self.create_text_button(self.menu_confirmar_usuarioN, "Editar", 551, 704, 120, 40, self.tamañoFuentePrincipal, self.colorFuente, self.tipografia, self.on_menu_confirmar_usuarioN_editar_clicked, True)
        self.menu_confirmar_usuarioN_boton_aceptar = self.create_image_button(self.menu_confirmar_usuarioN, "Desarrollo/Assets/Pruebas/cerebro.png", 201, 60, 688, 694, self.on_menu_confirmar_usuarioN_aceptar_clicked, True)
        

        
    def on_menu_principal_usuarios_clicked(self):
        self.menu_usuarios = QWidget(self)
        self.init_menu_usuarios()
        self.setCentralWidget(self.menu_usuarios)
    
    def on_menu_principal_pedidos_clicked(self):
        QMessageBox.information(self, "Pedidos", "Se presionó el botón de Pedidos")
    
    def on_menu_principal_servicios_clicked(self):
        QMessageBox.information(self, "Servicios", "Se presionó el botón de Servicios")
    
    def on_menu_principal_informes_clicked(self):
        QMessageBox.information(self, "Informes", "Se presionó el botón de Informes")
        
    def on_menu_usuarios_agregar_clicked(self):
        self.menu_formulario_usuarioN = QWidget(self)
        self.init_menu_formulario_usuarioN()
        self.setCentralWidget(self.menu_formulario_usuarioN)
        
    def on_menu_usuarios_editar_clicked(self):
        QMessageBox.information(self, "Editar", "Se presionó el botón de Editar")
        
    def on_menu_usuarios_atras_clicked(self):
        QMessageBox.information(self, "Atras", "Se presionó el botón de Atras")
        
    def on_menu_formulario_usuarioN_aceptar_clicked(self):
        cedula = self.menu_formulario_usuarioN_entry_cedula.text()
        nombre = self.menu_formulario_usuarioN_entry_nombre.text()
        rol = self.menu_formulario_usuarioN_rol_drop.currentText()
        self.menu_confirmar_usuarioN = QWidget(self)
        self.init_menu_confirmar_usuarioN(cedula, nombre, rol)
        self.setCentralWidget(self.menu_confirmar_usuarioN)
        
    def on_menu_formulario_usuarioN_cancelar_clicked(self):
        QMessageBox.information(self, "Cancelar", "Se presionó el botón de Cancelar")
        
    def on_menu_formulario_usuarioN_cerrar_clicked(self):
        QMessageBox.information(self, "Cerrar", "Se presionó el botón de Cerrar")
        
    def on_menu_confirmar_usuarioN_aceptar_clicked(self):
        self.menu_confirmar_usuarioN_boton_editar.setParent(None)
        self.menu_confirmar_usuarioN_boton_aceptar.setParent(None)
        
    def on_menu_confirmar_usuarioN_editar_clicked(self):
        QMessageBox.information(self, "Editar", "Se presionó el botón de Editar")
        
    def on_menu_confirmar_usuarioN_cerrar_clicked(self):
        QMessageBox.information(self, "Cerrar", "Se presionó el botón de Cerrar")
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
