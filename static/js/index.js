document.addEventListener('DOMContentLoaded', function () {
    fetchCategorias();
});

function fetchCategorias() {
    fetch('/api/categoria/get')
        .then(response => response.json())
        .then(categorias => {
            const tableBody = document.getElementById('categorias');
            tableBody.innerHTML = ''; // Limpiar tabla
            categorias.forEach(categoria => {
                let descripcion = '';
                let ancla = '#';

                switch (categoria.id) {
                    case 1:
                        descripcion = 'Apple Inc. es una empresa estadounidense que diseña y produce equipos electrónicos, software y servicios en línea.';
                        ancla = 'iphone';
                        break;
                    case 2:
                        descripcion = 'Samsung es una empresa multinacional, conglomerado de empresas y chaebol con sede en Seúl, Corea del Sur.'
                        ancla = 'samsung';
                        break;
                    case 3:
                        descripcion = 'Xiaomi Corpotation en una empresa china de electrónica  de condumo y fabricación inteligente con sede en Pekín.';
                        ancla = 'xiaomi';
                        break;
                    default:
                        descripcion = 'Descripcion no disponible';
                        ancla = '#';
                        break;
                }

                let url = `/catalogo#${ancla}`;

                const row = `
                    <a href="${url}" style="text-decoration: none; color: inherit;">
                        <div class="categoria">
                            <div class="categoria_marca">
                                <img src="${categoria.imagen}" alt="Imagen de ${categoria.nombre}" />
                                <h3>${categoria.nombre}</h3>
                                <p>${descripcion}</p>
                            </div>
                        </div>
                    </a>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error al cargar categorias:', error));
}