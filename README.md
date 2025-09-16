# 🛒 Carrito de Compras – Proyecto 
---
## 📘 Descripción del Proyecto
El **Carrito de Compras** es una aplicación web que permite a los usuarios navegar productos, agregarlos a un carrito virtual y realizar una compra simulada.  
El sistema está desarrollado con **Flask (Python)** en el backend, conectado a **MySQL** como base de datos, y utiliza **HTML, CSS y JavaScript** para la interfaz de usuario.  
El proyecto busca mostrar la integración entre frontend, backend y base de datos, siendo una base para futuras implementaciones de e-commerce.


## ✅ Requerimientos Funcionales  
1. El sistema debe permitir a los usuarios **registrarse e iniciar sesión** con credenciales válidas.  
2. El usuario podrá **visualizar un catálogo de productos** con nombre, precio e imagen.  
3. El sistema debe permitir **agregar y eliminar productos** del carrito de compras.  
4. El usuario podrá **visualizar un resumen de su carrito** con el total calculado automáticamente.  
5. El sistema debe simular un **proceso de compra**, mostrando confirmación del pedido.  

---

## ⚙️ Requerimientos No Funcionales  
1. La aplicación debe ser **responsive**, adaptándose a dispositivos móviles y de escritorio.  
2. El sistema debe **responder en menos de 3 segundos** a las acciones del usuario en condiciones normales.  
3. La base de datos debe garantizar **integridad y consistencia** en la información de productos y pedidos.  
4. El código debe estar **documentado y estructurado** para facilitar su mantenimiento.  
5. El sistema debe contar con **medidas básicas de seguridad**, como cifrado de contraseñas en la base de datos.  

---

## 🛠️ Tecnologías Utilizadas
- Python / Flask 
- Html/ CSS/ JavaScript / 
- Git / GitHub
- Base de datos... MySql

## 🚀 Instalación y Ejecución
Pasos para instalar y correr el proyecto...

### 1. Instalar Dependencias
Instala los paquetes necesarios ejecutando los siguientes comandos en tu terminal:

```bash
pip install Flask
```
```bash
pip install Flask-Cors
```
```bash
pip install Flask-Login
```
```bash
pip install Flask-SQLAlchemy
```
```bash
pip install mysql-connector-python
```
### 2. Ejecutar la Aplicación
Ir a la carpeta donde se encuentra el archivo `app.py` y ejecuta el siguiente comando:
```bash
python app.py
```
Esto iniciará el servidor en `http://127.0.0.1:5000/`.
### 3. Acceder a la Aplicación
Abre tu navegador y navega a la siguiente URL para acceder a la aplicación:
```bash
http://127.0.0.1:5000/
```
---
 
## 👥 Roles y Créditos
| Nombre | Rol | Funciones |
|--------|-----|-----------|
| Enzo | Dev Backend | Implementó todo el backend |
| Brillight | Frontend | Realizado la estructura|
| Adrian | Manejo de errores | Se encargo de los concflictos |

## 🔄 Flujo de Trabajo en Git
- Estructura de ramas: `feature/`, `fix/`
- Ejemplo de commit atómico:
  ```bash
  git commit -m "feat: agregar funcionalidad para eliminar producto del carrito"
  ```
  
## 🖼️ Capturas de Pantalla

### 🖼️ Captura de comandos
---
- Iniciamos git clonando el repositorio
![repositorio](./screenshots/iniciar_git.png)
- Realizamos el primer commit y lo subimos al repositorio
![commit](./screenshots/2.png)
- Sincronizamos los datos del primer commit a otra computadora
![](./screenshots/3.png)
- Realizamos un git checkout -b feature/frontend

- Agregamos los nuevos cambios y realizamos un commit
![](./screenshots/4.png)
- Subimos los cambios al GitHub
![](./screenshots/5.png)
- Nos movemos de la rama Main a la rama Feature/Registros_login y realimos un commit y luego lo subimos al GitHub
![](./screenshots/6.png)
![](./screenshots/7.png)
- Creamos nuestro primer pull request
![](./screenshots/8.png)
- Examinamos el segundo pull request y hacemos y merge
![](./screenshots/9.png)
![](./screenshots/10.png)
![](./screenshots/11.png)
- Resolvemos nuestro primer conflicto
![](./screenshots/12.png)
![](./screenshots/13.png)
![](./screenshots/14.png)
![](./screenshots/15.png)
![](./screenshots/16.png)
- Ejemplo de git restore 
![](./screenshots/17.png)
![](./screenshots/18.png)
- Historial de puntos de control
![](./screenshots/19.png)
![](./screenshots/20.png)
- Historial de cabeceras
![](./screenshots/21.png)

### 🏠 Página Principal
--- 
- Prototipo de la página principal -    Inicio
![Página principal](./screenshots/index.png)
- Prototipo login 
![Login](./screenshots/iniciosesion.png)
- Prototipo registro
![Registrar](./screenshots/registro.png)

