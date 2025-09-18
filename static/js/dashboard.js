document.addEventListener('DOMContentLoaded', function () {
    fetchUsers();
    fetchCategorias();

    const modalAdd = document.getElementById('add-category-modal');
    const btnAdd = document.getElementById('add-category-btn');
    const spanAdd = document.getElementsByClassName('close')[0];

    const modalModify = document.getElementById('modal-modified-category');
    const spanModify = document.getElementsByClassName('close-modify')[0];


    // Botón para añadir categoría
    btnAdd.onclick = function () {
        modalAdd.style.display = 'block';
    }

    spanAdd.onclick = function () {
        modalAdd.style.display = 'none';
    }

    spanModify.onclick = function () {
        modalModify.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == modalAdd) {
            modalAdd.style.display = 'none';
        }
        if (event.target == modalModify) {
            modalModify.style.display = 'none';
        }
    }

    // Formulario para añadir categoría
    document.getElementById('add-category-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const categoryName = document.getElementById('category-name').value;
        const categoryImage = document.getElementById('category-image').value;

        fetch('/api/categoria/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nombre: categoryName,
                imagen: categoryImage
            }),
        })
            .then(response => {
                return response.json().then(data => ({ ok: response.ok, data: data }));
            })
            .then(({ ok, data }) => {
                if (ok) {
                    alert(data.message || 'Categoría añadida con éxito.');
                    modalAdd.style.display = 'none';
                    document.getElementById('add-category-form').reset();
                    fetchCategorias(); // Recargar categorías
                } else {
                    alert(data.error || 'Error al añadir la categoría.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al conectar con el servidor.');
            });
    });

    // Formulario para modificar categoría
    document.getElementById('modify-category-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const categoryId = document.getElementById('modify-category-id').value;
        const categoryName = document.getElementById('modify-category-name').value;
        const categoryImage = document.getElementById('modify-category-image').value;

        fetch(`/api/categoria/modify/${categoryId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nombre: categoryName,
                imagen: categoryImage
            }),
        })
            .then(response => {
                return response.json().then(data => ({ ok: response.ok, data: data }));
            })
            .then(({ ok, data }) => {
                if (ok) {
                    alert(data.message || 'Categoría modificada con éxito.');
                    modalModify.style.display = 'none';
                    fetchCategorias(); // Recargar categorías
                } else {
                    alert(data.error || 'Error al modificar la categoría.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al conectar con el servidor.');
            });
    });
});

function fetchUsers() {
    fetch('/api/users')
        .then(response => response.json())
        .then(users => {
            const tableBody = document.getElementById('user-table-body');
            tableBody.innerHTML = '';
            users.forEach(user => {
                const row = `
                    <tr>
                        <td>${user.id}</td>
                        <td>${user.nombre}</td>
                        <td>${user.apellido}</td>
                        <td>${user.correo}</td>
                        <td>
                            <select class="role-select" onchange="updateRole(${user.id}, this.value)">
                                <option value="1" ${user.rol_id === 1 ? 'selected' : ''}>Usuario</option>
                                <option value="2" ${user.rol_id === 2 ? 'selected' : ''}>Administrador</option>
                            </select>
                        </td>
                        <td class="actions">
                            <button class="btnAdd-delete" onclick="deleteUser(${user.id})">Eliminar</button>
                        </td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error al cargar usuarios:', error));
}
function fetchCategorias() {
    fetch('/api/categoria/get')
        .then(response => response.json())
        .then(categorias => {
            const tableBody = document.getElementById('categoria-table-body');
            tableBody.innerHTML = ''; // Limpiar tabla
            categorias.forEach(categoria => {
                const row = `
                    <div class="categorias-container">
                        <div class="card">
                            <div class="card-img-container">
                                <img src="${categoria.imagen}" alt="Imagen de ${categoria.nombre}">
                            </div>
                            <div class="card-body">
                                <h3>${categoria.nombre}</h3>
                            </div>
                            <div class="card-buttons">
                                <button onclick="openModifyModal(${categoria.id}, '${categoria.nombre}', '${categoria.imagen}')">Modificar</button>
                                <button onclick="removeProductoFromCategoria(${categoria.id}, '${categoria.nombre}')">Eliminar</button>
                            </div>
                        </div>
                    </div>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error al cargar categorias:', error));
}

function openModifyModal(id, nombre, imagen) {
    const modalModify = document.getElementById('modal-modified-category');
    document.getElementById('modify-category-id').value = id;
    document.getElementById('modify-category-name').value = nombre;
    document.getElementById('modify-category-image').value = imagen;
    modalModify.style.display = 'block';
}

// -- Funciones para los usuarios ---------------------------------------------------------------------------------
function updateRole(userId, newRoleId) {
    if (!confirm(`¿Estás seguro de que quieres cambiar el rol del usuario ${userId}?`)) return;
    fetch(`/api/users/${userId}/role`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rol_id: newRoleId }),
    })
        .then(response => {
            if (response.ok) {
                alert('Rol actualizado con éxito.');
                fetchUsers();
            } else {
                alert('Error al actualizar el rol.');
            }
        })
        .catch(error => console.error('Error:', error));
}

function deleteUser(userId) {
    if (!confirm(`¿Estás seguro de que quieres eliminar al usuario ${userId}?`)) return;
    fetch(`/api/users/${userId}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) {
                alert('Usuario eliminado con éxito.');
                fetchUsers();
            } else {
                alert('Error al eliminar el usuario.');
            }
        })
        .catch(error => console.error('Error:', error));
}

// -- Funciones para las categorias ---------------------------------------------------------------------------------

function removeProductoFromCategoria(categoriaId, categoriaName) {
    if (!confirm(`¿Estás seguro de que quieres eliminar la categoría ${categoriaName}?`)) return;
    fetch(`/api/categoria/remove/${categoriaId}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert(`Categoría ${categoriaName} eliminada con éxito.`);
                fetchCategorias();
            } else {
                alert('Error al eliminar la categoría.');
            }
        })
        .catch(error => console.error('Error:', error));
}