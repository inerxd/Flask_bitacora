function submit_entry() {


    var id = document.getElementById('id');
    var idReg = id.value;
    var log_data = document.getElementById('log_data');
    var comments = document.getElementById('comments');
    var adminUrl = document.getElementById('data-url').getAttribute('data-admin-url');



    var entry = {

        log_data: log_data.value,
        comments: comments.value,

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