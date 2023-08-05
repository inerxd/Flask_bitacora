function submit_entry() {


    var id = document.getElementById('id');
    var idReg = id.value;
    var dato_bitacora = document.getElementById('dato_bitacora');
    var comentarios = document.getElementById('comentarios');



    var entry = {

        dato_bitacora: dato_bitacora.value,
        comentarios: comentarios.value,

    };
    console.log(entry);
    fetch(`${window.origin}/actualizar_bitacora/${idReg}`, {
        method: "PUT",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then(function (response) {
            if (response.ok) {
                window.location.replace(document.referrer);
                return;
            }
            throw new Error("Error en la respuesta de red");
        }).catch(function (error) {
            console.log(error);
        });

}