function submit_entry(){

    console.log("submit_entry() function executed.");
    var id = document.getElementById('id');
    var idReg = id.value;
    var usuario = document.getElementById('usuario');
    var password = document.getElementById('password');
    var tipo_usuario = document.getElementById('tipo_usuario')
    var adminUrl = document.getElementById('data-url').getAttribute('data-admin-url');


    
     
  var entry = {
    
    usuario: usuario.value,
    password: password.value,
    tipo_usuario:tipo_usuario.value
           };
    console.log(entry);
    fetch(`${window.origin}/actualizar/${idReg}`,{
      method: "PUT",
      credentials: "include",
      body:JSON.stringify(entry),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
    .then(function(response) {
  if(response.ok) {
      window.location.replace(adminUrl);
      return;
  }
  throw new Error("Error en la respuesta de red");
}).catch(function(error) {
  console.log(error);
});
   
}