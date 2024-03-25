
  function submit_entry() {
    var id = document.getElementById("id");
    var idReg = id.value;
    var nombre = document.getElementById("nombre");
    var rfc = document.getElementById("rfc");
    var direccion = document.getElementById("direccion");
    var grado_estudio = document.getElementById("grado_estudio");
    var edad = document.getElementById("edad");
    var puesto = document.getElementById("puesto");
    var adminUrl = document.getElementById('data-url').getAttribute('data-admin-url');
    

    var entry = {
      
      nombre: nombre.value,
      rfc: rfc.value,
      direccion: direccion.value,
      grado_estudio: grado_estudio.value,
      edad: edad.value,
      puesto: puesto.value,

    };

    fetch(`${window.origin}/actualizar_empleado/${idReg}`, {
      method: "PUT",
      credentials: "include",
      body: JSON.stringify(entry),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json",
      }),
    })
      .then(function (response) {
        if (response.ok) {
          window.location.replace(adminUrl);
          return;
        }
        throw new Error("Error en la respuesta de red");
      })
      .catch(function (error) {
        console.log(error);
      });
  }
