import sqlite3
from base_datos.conexion import ConexionBD
from tkinter import messagebox

def crear_tabla():
    
    conexion = ConexionBD()

    nueva_tabla = '''

        CREATE TABLE socios(
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero VARCHAR(10),
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        tipo VARCHAR(100),
        email VARCHAR(100),
        telefono VARCHAR(100),
        especialidad VARCHAR(100)
        )'''
    
    try:
        conexion.cursor.execute(nueva_tabla)
        conexion.cerrar()
        título = 'Creación de tabla en la base de datos'
        mensaje = 'Se creó correctamente la tabla en la base de datos'
        messagebox.showinfo(título, mensaje)
    except:
        título = 'Creación de tabla en la base de datos'
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(título, mensaje)

def borrar_tabla():
    conexion = ConexionBD()

    eliminar_tabla = 'DROP TABLE socios'

    try:
        conexion.cursor.execute(eliminar_tabla)
        conexion.cerrar()
        título = 'Borrar tabla en la base de datos'
        mensaje = 'Se eliminó exitosamente la tabla'
        messagebox.showinfo(título, mensaje)
    except:
        título = 'Borrar tabla en la base de datos'
        mensaje = 'No existe la tabla que se quiere eliminar'
        messagebox.showwarning(título, mensaje)

def guardar(socio):
    conexion = ConexionBD()
 
    guardar_socio = f'''INSERT INTO socios(numero, nombre, apellido, tipo, email, telefono, especialidad) VALUES('{socio.numero}', '{socio.nombre}', '{socio.apellido}', '{socio.tipo}',
     '{socio.email}', '{socio.telefono}', '{socio.especialidad}')'''
    
    try:
        conexion.cursor.execute(guardar_socio)
        conexion.cerrar()
    except:
        título = 'Conexión al registro'
        mensaje = 'La tabla de socios no está creada en la BBDD'
        messagebox.showerror(título, mensaje)
        
def listar():
    
    conexion = ConexionBD()
    lista_socios = []
    listar_tabla = 'SELECT * FROM socios'

    try:
        conexion.cursor.execute(listar_tabla)
        lista_socios = conexion.cursor.fetchall()
        conexion.cerrar()
        return lista_socios
    except:
        titulo = 'Conexión al Registro'
        mensaje = 'La tabla socios no está creada en la BD'
        messagebox.showerror(titulo, mensaje)

def editar(socio, id_socio):
    conexion = ConexionBD()

    editar_tabla = f"""UPDATE socios
SET numero = '{socio.numero}', nombre = '{socio.nombre}', apellido = '{socio.apellido}', tipo = '{socio.tipo}',
email = '{socio.email}', telefono = '{socio.telefono}', especialidad = '{socio.especialidad}'
WHERE id = {id_socio}
"""
    #try: 
    conexion.cursor.execute(editar_tabla)
    conexion.cerrar()
    '''except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar el registro'
        messagebox.showerror(titulo, mensaje)'''

def eliminar(id_socio):
    conexion = ConexionBD()

    eliminar_dato = f'DELETE FROM socios WHERE id = {id_socio}'

    try:
        conexion.cursor.execute(eliminar_dato)
        conexion.cerrar()
    except:
        titulo = 'Eliminación de datos'
        mensaje = 'No se ha podido eliminar el registro'
        messagebox.showerror(titulo, mensaje)

def buscar(nombre, apellido):
    conexion = ConexionBD()
    lista_busqueda = []
    elegir_elemento = f"""SELECT * FROM socios WHERE nombre = '{nombre}' or apellido = '{apellido}'""" 

    try:
        conexion.cursor.execute(elegir_elemento)
        lista_busqueda = conexion.cursor.fetchall()

        conexion.cerrar()
        return lista_busqueda
    except:
        titulo = 'Búsqueda de socio'
        mensaje = 'No se ha encontrado al socio'
        messagebox.showerror(titulo, mensaje)

def ordenar():
    conexion = ConexionBD()
    lista_ordenada = []
    ordenar_socios = f"""SELECT * FROM socios ORDER BY apellido DESC"""
    conexion.cursor.execute(ordenar_socios)
    lista_ordenada = conexion.cursor.fetchall()

    conexion.cerrar()
    return lista_ordenada

class Socio:
    def __init__(self, numero, nombre, apellido, tipo, email, telefono, especialidad):
        self.id_socio = None
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        self.email = email
        self.telefono = telefono
        self.especialidad = especialidad

    def __str__(self):
        return f'Socio[{self.numero}, {self.nombre}, {self.apellido}, {self.tipo}, {self.email}, {self.telefono}, {self.especialidad}]'
    
