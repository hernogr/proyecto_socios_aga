import tkinter as tk
from tkinter import ttk, messagebox
from base_datos.base_socios import crear_tabla, borrar_tabla, Socio, guardar, listar, editar, eliminar, buscar, ordenar

class MiFrame(tk.Frame):
     def __init__(self, raiz):
         super().__init__()
         self.raiz = raiz
         self.pack()
         self.etiquetas()
         self.entries()
         self.botones()
         self.tabla_socios()

         self.id_socio = None    
     def etiquetas(self):
         self.etiqueta_numero = tk.Label(self, text = 'Número de DNI')
         self.etiqueta_numero.config(font = ('Arial', 12))
         self.etiqueta_numero.grid(row = 0, column = 1)

         self.etiqueta_nombre = tk.Label(self, text = 'Nombre')
         self.etiqueta_nombre.config(font = ('Arial', 12))
         self.etiqueta_nombre.grid(row = 1, column = 1)

         self.etiqueta_apellido = tk.Label(self, text = 'Apellido')
         self.etiqueta_apellido.config(font = ('Arial', 12))
         self.etiqueta_apellido.grid(row = 2, column = 1)

         self.etiqueta_tipo = tk.Label(self, text = 'Tipo')
         self.etiqueta_tipo.config(font = ('Arial', 12))
         self.etiqueta_tipo.grid(row = 3, column = 1)

         self.etiqueta_email = tk.Label(self, text = 'E-mail')
         self.etiqueta_email.config(font = ('Arial', 12))
         self.etiqueta_email.grid(row = 4, column = 1)

         self.etiqueta_telefono = tk.Label(self, text = 'Teléfono')
         self.etiqueta_telefono.config(font = ('Arial', 12))
         self.etiqueta_telefono.grid(row = 5, column = 1)

         self.etiqueta_especialidad = tk.Label(self, text = 'Especialidad')
         self.etiqueta_especialidad.config(font = ('Arial', 12))
         self.etiqueta_especialidad.grid(row = 6, column = 1)

         self.etiqueta_buscar = tk.Label(self, text = 'Buscar')
         self.etiqueta_buscar.config(font = ('Arial', 12))
         self.etiqueta_buscar.grid(row = 50, column = 1)

     def entries(self):
        self.mi_numero = tk.StringVar()
        self.entry_numero = tk.Entry(self, textvariable = self.mi_numero)
        self.entry_numero.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_numero.grid(row = 0, column = 1, columnspan = 7)

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_nombre.grid(row = 1, column = 1, columnspan = 7)

        self.mi_apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable = self.mi_apellido)
        self.entry_apellido.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_apellido.grid(row = 2, column = 1, columnspan = 7)

        self.mi_tipo = tk.StringVar()
        self.entry_tipo = tk.Entry(self, textvariable = self.mi_tipo)
        self.entry_tipo.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_tipo.grid(row = 3, column = 1, columnspan = 7)

        self.mi_email = tk.StringVar()
        self.entry_email = tk.Entry(self, textvariable = self.mi_email)
        self.entry_email.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_email.grid(row = 4, column = 1, columnspan = 7)

        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable = self.mi_telefono)
        self.entry_telefono.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_telefono.grid(row = 5, column = 1, columnspan = 7)

        self.mi_especialidad = tk.StringVar()
        self.entry_especialidad = tk.Entry(self, textvariable = self.mi_especialidad)
        self.entry_especialidad.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_especialidad.grid(row = 6, column = 1, columnspan = 7)
        
        self.busqueda = tk.StringVar()
        self.entry_buscar = tk.Entry(self, textvariable = self.busqueda)
        self.entry_buscar.config(width = 50, state = 'normal', font = ('Arial', 12))
        self.entry_buscar.grid(row = 50, column = 1, columnspan = 7, padx = 10, pady = 10)

     def botones(self):
        self.boton_guardar = tk.Button(self, text = 'Guardar', command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12), bg = 'white', fg = 'black')
        self.boton_guardar.grid(row = 7, column = 1, padx = 10, pady = 10)

        self.boton_editar = tk.Button(self, text = 'Editar', command = self.editar_datos)
        self.boton_editar.config(width = 20, font = ('Arial', 12), bg = 'white', fg = 'black')
        self.boton_editar.grid(row = 7, column = 2, padx = 10, pady = 10)

        self.boton_borrar = tk.Button(self, text = 'Borrar', command = self.eliminar_datos)
        self.boton_borrar.config(width = 20, font = ('Arial', 12), bg = 'white', fg = 'black')
        self.boton_borrar.grid(row = 7, column = 3, padx = 10, pady = 10)

        self.boton_buscar = tk.Button(self, text = 'Buscar', command = self.buscar_datos)
        self.boton_buscar.config(width = 20, font = ('Arial', 12), bg = 'white', fg = 'black')
        self.boton_buscar.grid(row = 7, column = 4, padx = 10, pady = 10)

        self.boton_ordenar = tk.Button(self, text = 'Ordenar', command = self.ordenar_datos)
        self.boton_ordenar.config(width = 20, font = ('Arial', 12), bg = 'white', fg = 'black')
        self.boton_ordenar.grid(row = 7, column = 5, padx = 10, pady = 10)

     def guardar_datos(self):
        
        socio = Socio(
            self.mi_numero.get(),
            self.mi_nombre.get(),
            self.mi_apellido.get(),
            self.mi_tipo.get(),
            self.mi_email.get(),
            self.mi_telefono.get(),
            self.mi_especialidad.get()
        )
        
        if self.id_socio == None:
            guardar(socio)
        else:
            editar(socio, self.id_socio)

        self.tabla_socios()
        self.limpiar_campos()

        self.id_socio = None

     def limpiar_campos(self):
        self.mi_numero.set('')
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_tipo.set('')
        self.mi_email.set('')
        self.mi_telefono.set('')
        self.mi_especialidad.set('')

     def tabla_socios(self):
        self.lista_socios = listar()
        self.lista_socios.reverse()

        self.tabla = ttk.Treeview(self, column = ('Número', 'Nombre', 'Apellido', 'Tipo', 'E-mail', 'Teléfono', 'Especialidad'))
        self.tabla.grid(row = 8, column = 0, columnspan = 7, sticky = 'nsew', pady = 10)
      

       
        self.scrollv = ttk.Scrollbar(self, orient = 'vertical', command = self.tabla.yview)
        self.scrollv.grid(row = 8, column = 7, sticky = 'ns')
        self.tabla.configure(yscrollcommand = self.scrollv.set)
        '''
        self.scrollh = ttk.Scrollbar(self, orient = 'horizontal', command = self.tabla.xview)
        self.scrollh.grid(row = 18, column = 0, columnspan = 7, padx = 10, sticky = 'ew')
        self.tabla.configure(xscrollcommand = self.scrollh.set)'''

        self.tabla.column('#0',  width = 0, stretch=tk.NO)
        self.tabla.column('#1',  width = 200)
        self.tabla.column('#2',  width = 200)
        self.tabla.column('#3',  width = 200)
        self.tabla.column('#4',  width = 200)
        self.tabla.column('#5', width = 200)
        self.tabla.column('#6',  width = 200)
        self.tabla.column('#7',  width = 200)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Número de DNI')
        self.tabla.heading('#2', text = 'Nombre')
        self.tabla.heading('#3', text = 'Apellido')
        self.tabla.heading('#4', text = 'Tipo de Membresía')
        self.tabla.heading('#5', text = 'E-mail')
        self.tabla.heading('#6', text = 'Teléfono')
        self.tabla.heading('#7', text = 'Especialidad')

        for p in self.lista_socios:
             self.tabla.insert('', 0, text = p[0],
                               values = (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
     
     def editar_datos(self):
         try:
            self.id_socio = self.tabla.item(self.tabla.selection())['text']
            self.numero_socio = self.tabla.item(self.tabla.selection())['values'][0]
            self.nombre_socio = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellido_socio = self.tabla.item(self.tabla.selection())['values'][2]
            self.tipo_socio = self.tabla.item(self.tabla.selection())['values'][3]
            self.email_socio = self.tabla.item(self.tabla.selection())['values'][4]
            self.telefono_socio = self.tabla.item(self.tabla.selection())['values'][5]
            self.especialidad_socio = self.tabla.item(self.tabla.selection())['values'][6]

            self.entry_numero.insert(0, self.numero_socio)
            self.entry_nombre.insert(0, self.nombre_socio)
            self.entry_apellido.insert(0, self.apellido_socio)
            self.entry_tipo.insert(0, self.tipo_socio)
            self.entry_email.insert(0, self.email_socio)
            self.entry_telefono.insert(0, self.telefono_socio)
            self.entry_especialidad.insert(0, self.especialidad_socio)


         except:
             titulo = 'Edición de datos'
             mensaje = 'No se ha seleccionado ningún registro'
             messagebox.showerror(titulo, mensaje)

         
     def eliminar_datos(self):
            try:
               self.id_socio = self.tabla.item(self.tabla.selection())['text']
               eliminar(self.id_socio)
               self.tabla_socios()
               self.id_socio = None
            except:
                titulo = 'Eliminar un registro'
                mensaje = 'No se ha seleccionado ningún registro'
                messagebox.showerror(titulo, mensaje)


     def buscar_datos(self):
         nombre_socio = self.busqueda.get()
         apellido_socio = self.busqueda.get()
         self.lista_busqueda = buscar(nombre_socio, apellido_socio)
       
         if self.lista_busqueda is None or len(self.lista_busqueda) == 0:
               self.tabla_socios()
         else:
            self.tabla.delete(*self.tabla.get_children())
            for resultado in self.lista_busqueda:
               self.tabla.insert("", "end", text = resultado[0], values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7]))
         self.id_socio = None

     def ordenar_datos(self):
         self.ordenar_datos = ordenar()
         self.tabla.delete(*self.tabla.get_children())
         for p in self.ordenar_datos:
             self.tabla.insert('', 0, text = p[0],
                               values = (p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
        
        
def barra_menu(raiz):
        barra_menu = tk.Menu(raiz)
        raiz.config(menu = barra_menu, width = 800, height = 500)

        menu_opciones = tk.Menu(barra_menu, tearoff = 0)
        barra_menu.add_cascade(label = 'Opciones', menu = menu_opciones)

        menu_opciones.add_command(label = 'Crear base de datos', command = crear_tabla)
        menu_opciones.add_command(label = 'Eliminar base de datos', command = borrar_tabla)
        menu_opciones.add_command(label = 'Salir', command = raiz.destroy)
