import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QMessageBox, QGridLayout, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap, QIcon, QColor


class WindowNavigator:
    def __init__(self, stacked_widget, menu_principal, menu_usuarios, menu_formulario_usuarioN, menu_confirmar_usuarioN,
                 menu_lista_usuarios, menu_editar_usuario, menu_eliminar_usuarios, menu_pedidos, menu_crear_pedido,
                 menu_confirmar_pedido, menu_lista_pedidos, menu_editar_pedido, menu_eliminar_pedido, menu_servicios,
                 menu_visualizar_servicio, menu_editar_servicio, menu_informes, menu_visualizar_informe):
        self.stacked_widget = stacked_widget
        self.menu_principal = menu_principal
        self.menu_usuarios = menu_usuarios
        self.menu_formulario_usuarioN = menu_formulario_usuarioN
        self.menu_confirmar_usuarioN = menu_confirmar_usuarioN
        self.menu_lista_usuarios = menu_lista_usuarios
        self.menu_editar_usuario = menu_editar_usuario
        self.menu_eliminar_usuarios = menu_eliminar_usuarios
        self.menu_pedidos = menu_pedidos
        self.menu_crear_pedido = menu_crear_pedido
        self.menu_confirmar_pedido = menu_confirmar_pedido
        self.menu_lista_pedidos = menu_lista_pedidos
        self.menu_editar_pedido = menu_editar_pedido
        self.menu_eliminar_pedido = menu_eliminar_pedido
        self.menu_servicios = menu_servicios
        self.menu_visualizar_servicio = menu_visualizar_servicio
        self.menu_editar_servicio = menu_editar_servicio
        self.menu_informes = menu_informes
        self.menu_visualizar_informe = menu_visualizar_informe

    def navigate_to_principal(self):
        self.stacked_widget.setCurrentWidget(self.menu_principal)

    def navigate_to_usuarios(self):
        self.stacked_widget.setCurrentWidget(self.menu_usuarios)
        
    def navigate_to_formulario_usuarioN(self):
        self.stacked_widget.setCurrentWidget(self.menu_formulario_usuarioN)

    def navigate_to_confirmar_usuarioN(self):
        self.stacked_widget.setCurrentWidget(self.menu_confirmar_usuarioN)

    def navigate_to_lista_usuarios(self):
        self.stacked_widget.setCurrentWidget(self.menu_lista_usuarios)

    def navigate_to_editar_usuario(self):
        self.stacked_widget.setCurrentWidget(self.menu_editar_usuario)

    def navigate_to_eliminar_usuarios(self):
        self.stacked_widget.setCurrentWidget(self.menu_eliminar_usuarios)

    def navigate_to_pedidos(self):
        self.stacked_widget.setCurrentWidget(self.menu_pedidos)

    def navigate_to_crear_pedido(self):
        self.stacked_widget.setCurrentWidget(self.menu_crear_pedido)

    def navigate_to_confirmar_pedido(self):
        self.stacked_widget.setCurrentWidget(self.menu_confirmar_pedido)

    def navigate_to_lista_pedidos(self):
        self.stacked_widget.setCurrentWidget(self.menu_lista_pedidos)

    def navigate_to_editar_pedido(self):
        self.stacked_widget.setCurrentWidget(self.menu_editar_pedido)

    def navigate_to_eliminar_pedido(self):
        self.stacked_widget.setCurrentWidget(self.menu_eliminar_pedido)

    def navigate_to_servicios(self):
        self.stacked_widget.setCurrentWidget(self.menu_servicios)

    def navigate_to_visualizar_servicio(self):
        self.stacked_widget.setCurrentWidget(self.menu_visualizar_servicio)

    def navigate_to_editar_servicio(self):
        self.stacked_widget.setCurrentWidget(self.menu_editar_servicio)

    def navigate_to_informes(self):
        self.stacked_widget.setCurrentWidget(self.menu_informes)

    def navigate_to_visualizar_informe(self):
        self.stacked_widget.setCurrentWidget(self.menu_visualizar_informe)
          
class MainWindow(QMainWindow):
    tamañoFuentePrincipal = 40
    tamañoFuenteSecundario = 50
    tamañoFuenteTitulos = 120
    colorFuente = "#5E5E5E"
    tipografia = "Poppins"
    anchoVentana = 1440       # Ancho por defecto de la ventana
    altoVentana = 1024     # Alto por defecto de la ventana

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_principal = MenuPrincipal(self)
        self.stacked_widget.addWidget(self.menu_principal)

        self.menu_usuarios = MenuUsuarios(self)
        self.stacked_widget.addWidget(self.menu_usuarios)
        
        self.menu_formulario_usuarioN = MenuFormularioUsuarioN(self)
        self.stacked_widget.addWidget(self.menu_formulario_usuarioN)

        # Crear instancias para los otros menús...
        self.menu_confirmar_usuarioN = MenuConfirmarUsuarioN(self)
        self.stacked_widget.addWidget(self.menu_confirmar_usuarioN)

        self.menu_lista_usuarios = MenuListaUsuarios(self)
        self.stacked_widget.addWidget(self.menu_lista_usuarios)

        self.menu_editar_usuario = MenuEditarUsuario(self)
        self.stacked_widget.addWidget(self.menu_editar_usuario)

        self.menu_eliminar_usuarios = MenuEliminarUsuarios(self)
        self.stacked_widget.addWidget(self.menu_eliminar_usuarios)

        self.menu_pedidos = MenuPedidos(self)
        self.stacked_widget.addWidget(self.menu_pedidos)

        self.menu_crear_pedido = MenuCrearPedido(self)
        self.stacked_widget.addWidget(self.menu_crear_pedido)

        self.menu_confirmar_pedido = MenuConfirmarPedido(self)
        self.stacked_widget.addWidget(self.menu_confirmar_pedido)

        self.menu_lista_pedidos = MenuListaPedidos(self)
        self.stacked_widget.addWidget(self.menu_lista_pedidos)

        self.menu_editar_pedido = MenuEditarPedido(self)
        self.stacked_widget.addWidget(self.menu_editar_pedido)

        self.menu_eliminar_pedido = MenuEliminarPedido(self)
        self.stacked_widget.addWidget(self.menu_eliminar_pedido)

        self.menu_servicios = MenuServicios(self)
        self.stacked_widget.addWidget(self.menu_servicios)

        self.menu_visualizar_servicio = MenuVisualizarServicio(self)
        self.stacked_widget.addWidget(self.menu_visualizar_servicio)

        self.menu_editar_servicio = MenuEditarServicio(self)
        self.stacked_widget.addWidget(self.menu_editar_servicio)

        self.menu_informes = MenuInformes(self)
        self.stacked_widget.addWidget(self.menu_informes)

        self.menu_visualizar_informe = MenuVisualizarInforme(self)
        self.stacked_widget.addWidget(self.menu_visualizar_informe)

        self.window_navigator = WindowNavigator(self.stacked_widget, self.menu_principal, self.menu_usuarios, 
                                                self.menu_formulario_usuarioN, self.menu_confirmar_usuarioN, 
                                                self.menu_lista_usuarios, self.menu_editar_usuario, 
                                                self.menu_eliminar_usuarios, self.menu_pedidos, 
                                                self.menu_crear_pedido, self.menu_confirmar_pedido, 
                                                self.menu_lista_pedidos, self.menu_editar_pedido, 
                                                self.menu_eliminar_pedido, self.menu_servicios, 
                                                self.menu_visualizar_servicio, self.menu_editar_servicio, 
                                                self.menu_informes, self.menu_visualizar_informe)

        self.stacked_widget.setCurrentWidget(self.menu_principal)
        
        # Configurar el tamaño de la ventana al valor predeterminado
        self.resize(self.anchoVentana, self.altoVentana)
        
        # Iniciar el temporizador para actualizar la hora
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
    def create_clock_widget(self, parent):
        clock_widget = QLabel("", parent)
        clock_widget.setGeometry(1188, 51, 179, 60)
        clock_widget.setStyleSheet(f"font-size: {self.tamañoFuentePrincipal}px; color: {self.colorFuente}; font-family: {self.tipografia}")
        return clock_widget
    
    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        current_widget = self.stacked_widget.currentWidget()
        if hasattr(current_widget, 'clock_widget'):
            current_widget.clock_widget.setText(time_string)
            
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
        return label

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
        return button

    def create_text_button(self, text, x, y, width, height, font_size, font_color, font_family, action, no_border):
        button = QPushButton(text, self)
        button.setGeometry(x, y, width, height)
        button.setStyleSheet(f"color: {font_color}; font-size: {font_size}px; font-family: {font_family};")
        button.clicked.connect(action)
        if no_border:
            button.setStyleSheet("background-color: transparent; border: none;")  # Removiendo el borde
        return button

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

class MenuPrincipal(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Menu Principal")

        self.clock_widget = self.parent.create_clock_widget(self)

        self.label = self.parent.create_label("Bienvenido", 373, 147, 693, 180, MainWindow.tamañoFuenteTitulos, MainWindow.colorFuente, MainWindow.tipografia)

        self.boton_usuarios = self.parent.create_image_button("Desarrollo/Assets/menuPrincipal/usuarios.png", 432, 240, 266, 355, self.on_usuarios_clicked, True)
        self.boton_pedidos = self.parent.create_image_button("Desarrollo/Assets/menuPrincipal/pedidos.png", 432, 240, 743, 355, self.on_pedidos_clicked, True)
        self.boton_servicios = self.parent.create_image_button("Desarrollo/Assets/menuPrincipal/servicios.png", 432, 240, 266, 633, self.on_servicios_clicked, True)
        self.boton_informes = self.parent.create_image_button("Desarrollo/Assets/menuPrincipal/informes.png", 432, 240, 743, 633, self.on_informes_clicked, True)

    def on_usuarios_clicked(self):
        self.parent.window_navigator.navigate_to_usuarios()

    def on_pedidos_clicked(self):
        self.parent.window_navigator.navigate_to_pedidos()

    def on_servicios_clicked(self):
        QMessageBox.information(self, "Servicios", "Se presionó el botón de Servicios")

    def on_informes_clicked(self):
        QMessageBox.information(self, "Informes", "Se presionó el botón de Informes")

class MenuUsuarios(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Menu Usuarios")

        self.clock_widget = self.parent.create_clock_widget(self)
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

    def on_agregar_clicked(self):
        self.parent.window_navigator.navigate_to_formulario_usuarioN()

    def on_editar_clicked(self):
        self.parent.window_navigator.navigate_to_lista_usuarios()

    def on_atras_clicked(self):
        self.parent.window_navigator.navigate_to_principal()

class MenuFormularioUsuarioN(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Formulario registro usuario")

        self.clock_widget = self.parent.create_clock_widget(self)
        self.create_main_widget()

        layout = QGridLayout()
        layout.addWidget(self.clock_widget, 0, 0, alignment=Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(self.main_widget, 1, 0)
        self.setLayout(layout)
        
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 9)

    def create_main_widget(self):
        self.main_layout = QGridLayout()
        self.main_widget = QWidget(self)

        self.create_close_button()
        self.create_labels_and_entries()
        self.create_role_dropdown()
        self.create_buttons()

        self.main_layout.addWidget(self.close_button, 0, 1, alignment=Qt.AlignRight | Qt.AlignTop)
        self.main_layout.addWidget(self.label_registro, 1, 0, 1, 2, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.label_identificacion, 2, 0)
        self.main_layout.addWidget(self.entry_identificacion, 2, 1)
        self.main_layout.addWidget(self.label_nombre, 3, 0)
        self.main_layout.addWidget(self.entry_nombre, 3, 1)
        self.main_layout.addWidget(self.label_rol, 4, 0)
        self.main_layout.addWidget(self.combo_rol, 4, 1)
        self.main_layout.addWidget(self.button_cancelar, 5, 0)
        self.main_layout.addWidget(self.button_aceptar, 5, 1)

        self.main_widget.setLayout(self.main_layout)

    def create_close_button(self):
        self.close_button = QPushButton(self)
        self.set_icon(self.close_button, "Desarrollo/Assets/menuFormularioUsuarioN/cerrar.png")
        self.close_button.setStyleSheet("border: none;")
        self.close_button.clicked.connect(self.close)

    def create_labels_and_entries(self):
        self.label_registro = QLabel("Registro", self)
        self.label_registro.setStyleSheet(f"font-size: {MainWindow.tamañoFuenteSecundario}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}; font-weight: bold")
        self.label_identificacion = QLabel("Número de identificación:", self)
        self.entry_identificacion = QLineEdit(self)
        self.entry_identificacion.setFixedWidth(200)
        self.label_nombre = QLabel("Nombre completo:", self)
        self.entry_nombre = QLineEdit(self)
        self.entry_nombre.setFixedWidth(200)

        # Otros labels usarán el tamaño de fuente principal
        self.label_identificacion.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")
        self.label_nombre.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")

    def create_role_dropdown(self):
        self.label_rol = QLabel("Rol:", self)
        self.combo_rol = QComboBox(self)
        roles = ["Seleccionar", "Administrador", "Operario", "Invitado", "Usuario", "Comprador"]
        self.combo_rol.addItems(roles)
        self.label_rol.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")

    def create_buttons(self):
        self.button_cancelar = QPushButton("cancelar", self)
        self.button_cancelar.setStyleSheet(f"font-size: {MainWindow.tamañoFuentePrincipal}px; border: none; background-color: transparent; color: {MainWindow.colorFuente}; font-family: {MainWindow.tipografia}")
        self.button_aceptar = QPushButton(self)
        self.set_icon(self.button_aceptar, "Desarrollo/Assets/menuFormularioUsuarioN/aceptar.png")
        self.button_aceptar.setStyleSheet("border: none;")
        self.button_aceptar.clicked.connect(self.on_aceptar_clicked)

    def set_icon(self, widget, icon_path):
        pixmap = QPixmap(icon_path)
        icon = QIcon(pixmap)
        widget.setIcon(icon)
        widget.setIconSize(pixmap.rect().size())

    def on_aceptar_clicked(self):
        QMessageBox.information(self, "Aceptar", "Se presionó el botón Aceptar")
        
class MenuConfirmarUsuarioN(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Confirmar registro usuario")
        
class MenuListaUsuarios(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Lista de usuarios")
        
        self.create_clock_widget()
        self.create_label()
        self.create_table()
        
        layout = QGridLayout()
        layout.addWidget(self.clock_widget, 0, 1, alignment=Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(self.label, 1, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.table, 2, 0, 1, 2)  # Se ocupa dos columnas para la tabla
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 0)
        layout.setRowStretch(2, 1)  # La tabla ocupará el espacio restante en vertical
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.setLayout(layout)
        
        self.lista_usuarios()  # Llamar al método para cargar los usuarios
        
    def create_clock_widget(self):
        self.clock_widget = QLabel("", self)
        self.clock_widget.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.clock_widget.setStyleSheet("font-size: 20px; color: black; font-family: Arial;")
        
    def create_label(self):
        self.label = QLabel("Usuarios", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; color: black; font-family: Arial; font-weight: bold")
        
    # Dentro del método create_table() en la clase MenuListaUsuarios
    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Se añade una columna adicional para los checkboxes
        self.table.setHorizontalHeaderLabels(["Nombre", "Cédula", "Rol", "Seleccionar"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Para que las columnas se ajusten automáticamente
        self.table.verticalHeader().setVisible(False)  # Ocultar los números de fila
        
        # Centrar el checkbutton en la columna "Seleccionar"
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
    def lista_usuarios(self):
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('Desarrollo/Database/marmato_db.db')
        cursor = conn.cursor()

        # Ejecutar la consulta para seleccionar los campos nombre, cedula y rol de la tabla usuarios
        cursor.execute("SELECT nombre, cedula, rol FROM usuarios")

        # Obtener todos los resultados de la consulta
        usuarios = cursor.fetchall()

        # Iterar sobre los usuarios y agregarlos a la tabla
        for index, usuario in enumerate(usuarios):
            nombre_item = QTableWidgetItem(usuario[0])
            cedula_item = QTableWidgetItem(str(usuario[1]))
            rol_item = QTableWidgetItem(usuario[2])
            check_box = QCheckBox()
            
            # Conectar la señal stateChanged del checkbox a la función de cambio de color
            check_box.stateChanged.connect(lambda state, row=index: self.change_row_color(row, state))

            self.table.insertRow(index)
            self.table.setItem(index, 0, nombre_item)
            self.table.setItem(index, 1, cedula_item)
            self.table.setItem(index, 2, rol_item)
            self.table.setCellWidget(index, 3, check_box)

        # Ajustar el tamaño de la tabla según la ventana
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        # Cerrar la conexión a la base de datos
        conn.close()
        
    def change_row_color(self, row, state):
        # Definir el color deseado en hexadecimal
        color_hex = "#1D8DD0"
        color = QColor(color_hex)

        # Cambiar el color de fondo de la fila cuando el checkbox cambia de estado
        if state == Qt.Checked:
            self.table.item(row, 0).setBackground(color)  # Cambiar color de fondo de la primera columna
            self.table.item(row, 1).setBackground(color)  # Cambiar color de fondo de la segunda columna
            self.table.item(row, 2).setBackground(color)  # Cambiar color de fondo de la tercera columna
        
        else:
            # Si el estado no está marcado, restaurar al color blanco
            self.table.item(row, 0).setBackground(Qt.white)  # Restaurar color de fondo de la primera columna
            self.table.item(row, 1).setBackground(Qt.white)  # Restaurar color de fondo de la segunda columna
            self.table.item(row, 2).setBackground(Qt.white)  # Restaurar color de fondo de la tercera columna
        
    def update_time(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString("h:mm ap")
        self.clock_widget.setText(time_string)
        
class MenuEditarUsuario(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Editar usuario")
        
class MenuEliminarUsuarios(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Eliminar usuarios")
        
class MenuPedidos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Menu pedidos")
        
        self.clock_widget = self.parent.create_clock_widget(self)
        
class MenuCrearPedido(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Formulario crear pedido")
        
class MenuConfirmarPedido(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Confirmar pedido")
        
class MenuListaPedidos(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Lista pedidos")
        
class MenuEditarPedido(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Formulario editar pedido")
        
class MenuEliminarPedido(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Eliminar pedido")
        
class MenuServicios(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Menu servicios")
        
class MenuVisualizarServicio(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Visualizar servicio")
        
class MenuEditarServicio(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Formulario editar servicio")
        
class MenuInformes(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Menu informes")


class MenuVisualizarInforme(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Visualizar informe")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
