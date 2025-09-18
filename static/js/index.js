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
                if (categoria.id == 1) {
                    descripcion = 'Apple Inc. es una empresa estadounidense que diseña y produce equipos electrónicos, software y servicios en línea.';
                } else if (categoria.id == 2) {
                    descripcion = 'Samsung es una empresa multinacional, conglomerado de empresas y chaebol con sede en Seúl, Corea del Sur.';
                } else if (categoria.id == 3) {
                    descripcion = 'Xiaomi Corporation es una empresa china de electrónica de consumo y fabricación inteligente con sede en Pekín.';
                } 
                const row = `
                    <a href="#" style="text-decoration: none; color: inherit;">
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