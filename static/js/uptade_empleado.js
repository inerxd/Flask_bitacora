
  function submit_entry() {
    var id = document.getElementById("id");
    var idReg = id.value;
    var name = document.getElementById("name");
    var rfc = document.getElementById("rfc");
    var adress = document.getElementById("adress");
    var study_grade = document.getElementById("study_grade");
    var age = document.getElementById("age");
    var position = document.getElementById("position");
    var adminUrl = document.getElementById('data-url').getAttribute('data-admin-url');
    

    var entry = {
      
      name: name.value,
      rfc: rfc.value,
      adress: adress.value,
      study_grade: study_grade.value,
      age: age.value,
      position: position.value,

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
