function submit_entry(){

    console.log("submit_entry() function executed.");
    var id = document.getElementById('id');
    var idReg = id.value;
    var email = document.getElementById('email');
    var password = document.getElementById('password');
    var User_Type_id_User_Type = document.getElementById('User_Type_id_User_Type')
    var adminUrl = document.getElementById('data-url').getAttribute('data-admin-url');


    
     
  var entry = {
    
    email: email.value,
    password: password.value,
    User_Type_id_User_Type:User_Type_id_User_Type.value
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