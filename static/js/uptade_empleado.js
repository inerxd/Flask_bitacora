
function send_put(){
    fetch('http://localhost:5000/actualizar_empleado/{{datos.id_empleado}}',{
        method: 'PUT',
        body:JSON.stringify({
             nombre : document.getElementById('id').value,
             rfc : document.getElementById('rfc').value,
             direccion : document.getElementById('direccion').value,
             grado_estudio : document.getElementById('grado_estudio').value,
             edad : document.getElementById('edad').value,
             puesto : document.getElementById('puesto').value
           
        })

    })
    .then(response =>response.json())
    .then(data =>console.log(data))
}
    const nombre = document.getElementById('id').value;
    const rfc = document.getElementById('rfc').value;
    const direccion = document.getElementById('direccion').value;
    const grado_estudio = document.getElementById('grado_estudio').value;
    const edad = document.getElementById('edad').value;
    const puesto = document.getElementById('puesto').value;

    


