# 🤝 Guía de Contribución – Carrito de Compras

Gracias por tu interés en contribuir al proyecto **Carrito de Compras** 🛒  
Este documento explica las reglas, convenciones y flujo de trabajo que todo colaborador debe seguir para mantener un desarrollo ordenado, colaborativo y coherente.

---

## 📋 Requisitos Previos

Antes de contribuir, asegúrate de tener:
- Git instalado y configurado (`git --version`).
- Acceso al repositorio principal en GitHub.
- Python 3 y Flask instalados.
- Base de datos MySQL configurada.

---

## 🌳 Estrategia de Ramificación (Git Flow Adaptado)

El proyecto sigue una versión simplificada de **Git Flow**, con las siguientes ramas principales:

| Rama | Descripción |
|------|--------------|
| `main` | Rama estable que contiene versiones listas para producción. |
| `develop` | Rama base para integrar nuevas funcionalidades antes de lanzar una versión. |

### 🔱 Ramas secundarias

| Tipo de rama | Convención de nombre | Uso |
|---------------|----------------------|-----|
| Feature | `feature/<nombre-funcionalidad>` | Nueva funcionalidad. |
| Fix | `fix/<nombre-error>` | Corrección de bug detectado. |
| Hotfix | `hotfix/<nombre-urgente>` | Corrección rápida en producción. |
| Release | `release/<versión>` | Preparación de una nueva versión estable. |

**Ejemplo:**
```bash
git checkout -b feature/agregar-eliminar-producto
git checkout -b fix/error-login
```

---

## 🧱 Convención de Commits

Se siguen los prefijos del estándar Conventional Commits:

| Tipo | Propósito | Ejemplo |
|------|-----------|---------|
| `feat:` | Nueva funcionalidad | `feat: agregar botón de eliminar producto` |
| `fix:` | Corrección de error | `fix: corregir error en total del carrito` |
| `docs:` | Cambios en documentación | `docs: actualizar instrucciones en README` |
| `style:` | Cambios de formato o estilo | `style: ajustar márgenes en catálogo` |
| `refactor:` | Reestructuración del código sin alterar funcionalidad | `refactor: optimizar consulta SQL` |
| `test:` | Agregar o modificar pruebas | `test: agregar prueba de registro de usuario` |

Los commits deben ser atómicos (una acción por commit) y claros.

---

## 🔄 Flujo de Contribución

1. Fork del repositorio principal (si no tienes acceso directo).

2. Clona tu fork:
```bash
git clone https://github.com/<tu_usuario>/carrito-compras.git
```

3. Agrega el upstream:
```bash
git remote add upstream https://github.com/<repositorio-principal>/carrito-compras.git
```

4. Crea una rama nueva desde develop:
```bash
git checkout develop
git pull upstream develop
git checkout -b feature/nueva-funcionalidad
```

5. Realiza los cambios y commits siguiendo las convenciones.

6. Sincroniza con el upstream antes de enviar tu PR:
```bash
git fetch upstream
git merge upstream/develop
```

7. Sube tus cambios y abre un Pull Request (PR):
   - Título claro (ejemplo: `feat: agregar función de búsqueda`).
   - Descripción breve de lo que se hizo y por qué.
   - Espera la revisión cruzada de otro integrante antes del merge.

8. Una vez aprobado, se hace merge a `develop`.

---

## 🧩 Revisión Cruzada (Code Review)

Todo PR debe ser revisado por al menos un compañero.

La revisión incluye:
- Legibilidad del código.
- Nombres de variables y funciones.
- Correcto uso de convenciones.
- Validación funcional (que no rompa el flujo principal).

---

## 🔐 Branch Rules y Tag Rules

### 🌿 Branch Rules

- `main` y `develop` están protegidas (no se hace push directo).
- Solo se puede hacer merge mediante Pull Request aprobado.
- Se deben pasar las revisiones y no tener conflictos activos.

### 🏷️ Tag Rules

Se utiliza versionado semántico (SemVer) siguiendo la estructura:
```
vMAJOR.MINOR.PATCH
```

Ejemplos:
- `v1.0.0` → Versión inicial estable.
- `v1.1.0` → Nuevas funcionalidades sin romper compatibilidad.
- `v1.1.1` → Corrección menor o bugfix.

Comandos:
```bash
git tag -a v1.0.0 -m "Versión inicial estable"
git push origin v1.0.0
```

---

## 🗂️ Gestión de Issues y Milestones

- Cada issue debe describir claramente el problema o mejora.
- Usa etiquetas (labels) como:
  - `bug`
  - `enhancement`
  - `documentation`
  - `frontend`
  - `backend`
- Asigna responsables y relaciona el issue con un milestone.
- Cierra el issue solo cuando el Pull Request correspondiente se haya fusionado.

**Ejemplo de issue:**

- **Título:** Error al calcular total del carrito
- **Descripción:** El total no se actualiza cuando se elimina un producto.
- **Etiqueta:** `bug`
- **Rama relacionada:** `fix/error-total-carrito`

---

## 🧭 Tablero de Proyecto (Project Board)

El equipo puede usar el tablero de GitHub para organizar tareas y hacer seguimiento al progreso:

- **To Do** → tareas por hacer
- **In Progress** → tareas en desarrollo
- **Review** → en revisión por otros miembros
- **Done** → tareas finalizadas

---

## 💬 Comunicación del Equipo

- Usa comentarios en los Pull Requests para sugerencias y revisiones.
- Reporta avances, dudas o bloqueos mediante issues.
- Mantén siempre tu repositorio sincronizado con el upstream para evitar conflictos.

---

## 🏁 Buenas Prácticas

- Realiza commits pequeños y frecuentes.
- Asegúrate de que todo cambio pase por revisión antes del merge.
- Documenta cada cambio relevante en el archivo `CHANGELOG.md`.
- Respeta las convenciones de ramas y commits definidas en esta guía.
- No subas archivos temporales ni credenciales sensibles.

---

✅ **Recuerda:** Un buen flujo colaborativo garantiza calidad, orden y facilita la integración continua del proyecto.