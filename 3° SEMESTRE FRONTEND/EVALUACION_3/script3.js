$(document).ready(function () {
  let tabla;

  $('#btnCargar').click(function () {
    const tipo = $('#tipoDatos').val();
    const url = `https://jsonplaceholder.typicode.com/${tipo}`;

    fetch(url)
      .then(res => res.json())
      .then(data => {
        if (tabla) {
          tabla.destroy();
          $('#tablaDatos tbody').empty();
          $('#encabezadoTabla').empty();
        }

        
        const keys = Object.keys(data[0]);
        keys.forEach(k => {
          $('#encabezadoTabla').append(`<th>${k.toUpperCase()}</th>`);
        });

        
        data.forEach(obj => {
          const fila = keys.map(k => `<td>${obj[k]}</td>`).join('');
          $('#tablaDatos tbody').append(`<tr>${fila}</tr>`);
        });

        
        tabla = $('#tablaDatos').DataTable();
      })
      .catch(err => {
        alert('Error al cargar los datos');
        console.error(err);
      });
  });
});
