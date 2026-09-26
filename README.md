# Restaurante App

**Estudiante:** Bryan Saul Iza Llano

Aplicacion de escritorio para administrar productos y consultar usuarios de un restaurante. Fue construida con Python y Tkinter, aplicando una separacion sencilla entre la interfaz, los modelos, los servicios y los archivos de datos.

## Objetivo del proyecto

El proyecto permite iniciar sesion y trabajar con la informacion basica del restaurante desde una ventana grafica. La aplicacion carga los datos al iniciar, muestra un resumen general y permite administrar productos sin usar una base de datos externa.

## Cualidades principales

- Interfaz grafica sencilla y facil de usar.
- Separacion del codigo por responsabilidades.
- Validacion de usuarios, nombres, codigos y precios.
- Precio escrito con punto o coma decimal, por ejemplo `2.50` o `2,50`.
- Datos guardados en archivos JSON locales.
- Mensajes para informar errores y operaciones realizadas.
- Menu lateral con accesos a Inicio, Usuarios y Productos.
- Ventana ajustable y ampliacion automatica al abrir la seccion de productos.
- Iconos en los botones del menu cuando el archivo de imagen esta disponible.

## Como se estructuro el proyecto

El proyecto se organizo en varias partes para que cada archivo tenga una tarea clara:

- `main.py`: inicia la aplicacion, crea la ventana y cambia entre las vistas.
- `modelos/`: contiene las clases que representan los datos del sistema.
- `servicios/`: contiene la lectura de archivos y las operaciones del restaurante.
- `ui/`: contiene las pantallas y los controles graficos.
- `datos/`: contiene la informacion guardada en formato JSON.
- `assets/`: contiene el logo y los iconos usados en la interfaz.

Esta separacion permite modificar la pantalla sin cambiar directamente la forma en que se guardan los datos. Tambien facilita agregar nuevas funciones en el futuro.

## Estructura de carpetas

```text
SEMANA 14/
|-- README.md
|-- restaurante_app/
	|-- main.py
	|-- datos/
	|   |-- productos.json
	|   |-- usuarios.json
	|-- modelos/
	|   |-- producto.py
	|   |-- usuario.py
	|   |-- __init__.py
	|-- servicios/
	|   |-- archivo_servicio.py
	|   |-- restaurante_servicio.py
	|   |-- __init__.py
	|-- ui/
	|   |-- login_view.py
	|   |-- main_view.py
	|   |-- __init__.py
	|-- assets/
		|-- icons/
		|-- logo/
```

## Componentes y contenedores utilizados

La interfaz se construyo con controles incluidos en Tkinter:

- `Tk`: ventana principal de la aplicacion.
- `Frame`: separa el menu lateral, el contenido y la barra de estado.
- `Label`: muestra titulos, nombres, mensajes y totales.
- `Entry`: permite escribir usuario, contrasena, codigo, nombre y precio.
- `LabelFrame`: agrupa el formulario y los listados con un titulo visible.
- `ttk.Button`: crea los botones de navegacion y acciones.
- `ttk.Treeview`: muestra los productos y usuarios en forma de tabla.
- `ttk.Scrollbar`: permite desplazarse por las tablas.
- `PhotoImage`: carga el logo y los iconos PNG.
- `messagebox`: muestra mensajes de exito o error.

Para acomodar los elementos se usan tres formas de distribucion:

- `pack`: organiza el menu, botones y elementos que ocupan un espacio continuo.
- `grid`: organiza el formulario junto a la tabla de productos.
- `place`: centra el formulario de inicio de sesion dentro de la ventana.

## Pantallas de la aplicacion

### Inicio de sesion

La vista `login_view.py` muestra el logo, los campos de usuario y contrasena, un mensaje de error y el boton para entrar. Las credenciales se revisan usando los usuarios cargados desde `usuarios.json`.

Usuario de prueba incluido:

```text
Usuario: saul
Contrasena: saul123
```

### Pantalla principal

La vista `main_view.py` contiene un menu lateral, un area central y una barra de estado. Desde el menu se puede regresar al inicio, consultar usuarios o administrar productos.

## Mejoras realizadas en la interfaz

- Se agrego un menu lateral para cambiar de seccion rapidamente.
- Se definieron colores, estilos y estados para los botones.
- Se mejoro el contraste del menu para que los iconos se distingan mejor.
- Se agregaron iconos para las opciones principales y el cierre de sesion.
- Se agrego una barra de estado con la cantidad de usuarios y productos.
- Se ajusto el tamano minimo de la ventana para evitar que el contenido quede oculto.
- Al entrar a Productos, la ventana se amplia para mostrar el formulario y las tres columnas de la tabla.
- Se agregaron tablas con barra de desplazamiento para facilitar la consulta.
- Se muestran mensajes cuando una operacion termina correctamente o cuando existe un error.

## Operaciones sobre productos

La seccion Productos permite realizar las operaciones principales:

1. **Registrar:** crea un producto con codigo, nombre y precio.
2. **Cargar por codigo:** busca un producto y coloca sus datos en el formulario.
3. **Actualizar:** cambia los datos de un producto existente.
4. **Eliminar:** quita un producto usando su codigo.
5. **Limpiar:** deja vacios los campos del formulario.

El codigo no puede repetirse, los campos de texto no pueden quedar vacios y el precio debe ser un numero igual o mayor que cero.

## Persistencia de datos

La aplicacion usa archivos JSON como almacenamiento local:

- `restaurante_app/datos/usuarios.json`: guarda identificador, nombre, usuario y contrasena.
- `restaurante_app/datos/productos.json`: guarda codigo, nombre y precio.

La clase `ArchivoServicio` se encarga de leer y escribir estos archivos. Si un archivo no existe, esta vacio o tiene un formato incorrecto, se crea o se reinicia con una lista vacia. Los productos se guardan automaticamente despues de registrar, actualizar o eliminar.

## Requisitos

- Python 3 instalado.
- Tkinter disponible. En Windows normalmente viene incluido con Python.
- Los archivos y carpetas del proyecto conservados en su estructura original.

No se necesitan paquetes externos para ejecutar la aplicacion.

## Pasos para ejecutar `main.py`

1. Abrir una terminal.
2. Entrar a la carpeta raiz del proyecto, la carpeta que contiene `README.md` y `restaurante_app`.
3. Ejecutar el programa con:

   ```powershell
   py restaurante_app\main.py
   ```

   En otros sistemas tambien puede funcionar:

   ```bash
   python restaurante_app/main.py
   ```

4. Ingresar con el usuario de prueba o con otro usuario registrado en `restaurante_app/datos/usuarios.json`.
5. Usar el menu lateral para consultar usuarios o administrar productos.

Tambien se puede comprobar que el codigo no tenga errores de sintaxis con:

```powershell
py -m compileall -q restaurante_app
```

## Notas

La aplicacion guarda los cambios directamente en los archivos JSON. Por eso conviene conservar una copia de `datos` si se desea proteger la informacion antes de hacer pruebas.
