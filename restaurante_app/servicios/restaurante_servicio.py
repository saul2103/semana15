from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    # Reune las acciones principales del restaurante.
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        # Trae los datos guardados y crea sus objetos.
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")

        self.usuarios = [
            Usuario(
                datos.get("identificador", ""),
                datos.get("nombre", ""),
                datos.get("usuario", ""),
                datos.get("contrasena", datos.get("contraseña", "")),
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("codigo", ""),
                datos.get("nombre", ""),
                datos.get("precio", 0),
            )
            for datos in productos_json
        ]

    def validar_acceso(self, usuario, contrasena):
        # Busca si los datos de acceso son correctos.
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado

        return None

    def cantidad_usuarios(self):
        # Cuenta las personas registradas.
        return len(self.usuarios)

    def cantidad_productos(self):
        # Cuenta los productos registrados.
        return len(self.productos)

    def listar_usuarios(self):
        # Devuelve los usuarios para mostrarlos en pantalla.
        return self.usuarios

    def listar_productos(self):
        # Devuelve los productos para mostrarlos en pantalla.
        return self.productos

    def guardar_productos(self):
        # Guarda la lista actual de productos.
        datos= [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
            }
            for producto in self.productos
        ]
        self.archivo_servicio.escribir_json("productos.json", datos)

    def buscar_producto_por_codigo(self, codigo):
        # Busca un producto usando su codigo.
        codigo=codigo.strip()  # Elimina espacios en blanco al inicio y al final

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo, nombre, precio):
        # Crea un producto nuevo y lo guarda.
        nuevo_producto = Producto(codigo, nombre, precio)
        if self.buscar_producto_por_codigo(nuevo_producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con ese codigo.")

        self.productos.append(nuevo_producto)
        self.guardar_productos()
        return nuevo_producto

    def actualizar_producto(self, codigo, nombre, precio):
        # Cambia los datos de un producto existente.
        producto_actual = self.buscar_producto_por_codigo(codigo)

        if producto_actual is None:
            raise ValueError(f"No existe un producto con ese codigo.")

        datos_validados = Producto(codigo, nombre, precio)
        producto_actual.codigo = datos_validados.codigo
        producto_actual.nombre = datos_validados.nombre
        producto_actual.precio = datos_validados.precio
        self.guardar_productos()
        return producto_actual

    def eliminar_producto(self, codigo):
        # Quita un producto y guarda el cambio.
        producto_actual= self.buscar_producto_por_codigo(codigo)

        if producto_actual is None:
            raise ValueError(f"No existe un producto con ese codigo.")

        self.productos.remove(producto_actual)
        self.guardar_productos()
        return producto_actual
    