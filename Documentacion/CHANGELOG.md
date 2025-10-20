# 📄 CHANGELOG

Todos los cambios importantes de este proyecto se documentarán en este archivo.  
El formato sigue las convenciones de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)  
y la numeración de versiones se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [1.0.0] - 2025-10-20
### 🚀 Lanzamiento inicial: *Carrito de Compras – Proyecto*

### 🆕 Added
- Implementación del **backend con Flask**:
  - Configuración del servidor, rutas y controladores.
  - Conexión a base de datos **MySQL** con SQLAlchemy.
  - Gestión de usuarios (registro e inicio de sesión con contraseñas cifradas).
  - Endpoints para productos, carrito y pedidos.

- Desarrollo del **frontend**:
  - Estructura HTML de las páginas: catálogo, carrito, login y registro.
  - Estilos CSS para diseño responsive (adaptado a móviles y escritorio).
  - Funcionalidad JavaScript para agregar/eliminar productos y actualizar precios en tiempo real.

- Configuración del **repositorio Git/GitHub**:
  - Estructura de ramas basada en `feature/` y `fix/`.
  - Primeros commits atómicos y descriptivos.
  - Creación de ramas: `feature/frontend`, `feature/backend`, `feature/login`.
  - Realización de *pull requests* y resolución de conflictos.

- **Base de datos MySQL**:
  - Creación de tablas para productos, usuarios y pedidos.
  - Garantía de integridad referencial e información consistente.

- **Documentación**:
  - Archivo `README.md` con descripción, instalación y roles del equipo.
  - Capturas de evidencias de commits, ramas y PRs.
  - Flujo de trabajo documentado con ejemplos de `git checkout`, `restore`, `merge`.

### 🔧 Fixed
- Resolución de conflictos al fusionar ramas `feature/frontend` y `feature/login`.
- Corrección de rutas estáticas en Flask para servir los archivos HTML y CSS.
- Ajuste en la lógica del carrito que no actualizaba correctamente el total.

### 🔄 Changed
- Se reorganizó la estructura del proyecto para separar frontend y backend.
- Se actualizaron los nombres de las ramas para seguir la convención `feature/` y `fix/`.
- Se mejoró el diseño visual del catálogo y botones de acción.

### 👥 Credits
- **Enzo** – Backend Developer (implementación del servidor Flask).
- **Brillight** – Frontend Developer (estructura HTML, CSS y JS).
- **Adrihan** – Manejo de errores y resolución de conflictos Git.

---

## [Por publicar]
### 🧩 Planned
- Integración con API de pago simulada.
- Implementación de autenticación con JWT.
- Mejora del dashboard de usuario.
- Pruebas unitarias para backend y frontend.
