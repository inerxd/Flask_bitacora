function mostrarOcultarContrasena() {
    var contrasenaInput = document.getElementById("password");
    var iconoMostrarOcultar = document.getElementById("iconoMostrarOcultar");

    if (contrasenaInput.type === "password") {
        contrasenaInput.type = "text";
        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye-slash"></i>';
    } else {
        contrasenaInput.type = "password";
        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye"></i>';
    }
}