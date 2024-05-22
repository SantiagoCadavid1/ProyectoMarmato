import sqlite3
import random
import string

# Generar nombres aleatorios
def generar_nombre():
    nombres = ['Juan', 'Pedro', 'María', 'Ana', 'Carlos', 'Luis', 'Laura', 'Sofía', 'Diego', 'Andrea']
    apellidos = ['Perez', 'Gomez', 'Rodriguez', 'Gonzalez', 'Martinez', 'Lopez', 'Diaz', 'Hernandez', 'Sanchez', 'Torres']
    nombre_completo = random.choice(nombres) + ' ' + random.choice(apellidos)
    return nombre_completo

# Generar cédula aleatoria
def generar_cedula():
    return ''.join(random.choices(string.digits, k=10))

# Generar roles aleatorios
def generar_rol():
    roles = ['Administrador', 'Usuario']
    return random.choice(roles)

# Generar id_tarjeta aleatorio
def generar_id_tarjeta():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Conectar a la base de datos SQLite
conn = sqlite3.connect('Desarrollo/Database/marmato_db.db')
cursor = conn.cursor()

# Insertar 200 usuarios adicionales
for _ in range(200):
    nombre = generar_nombre()
    cedula = generar_cedula()
    id_tarjeta = generar_id_tarjeta()
    rol = generar_rol()
    cursor.execute("INSERT INTO usuarios (nombre, cedula, id_tarjeta, rol) VALUES (?, ?, ?, ?)", (nombre, cedula, id_tarjeta, rol))

# Confirmar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()
