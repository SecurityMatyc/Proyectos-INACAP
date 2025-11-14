$(document).ready(function () {
  
  function limpiarErrores() {
    $(".error-message").text("");
  }

  
  function validarFecha(fecha) {
    const regex = /^\d{2}\/\d{2}\/\d{4}$/;
    if (!regex.test(fecha)) return false;
    const [dia, mes, anio] = fecha.split("/").map(Number);
    const date = new Date(anio, mes - 1, dia);
    return (
      date.getFullYear() === anio &&
      date.getMonth() === mes - 1 &&
      date.getDate() === dia
    );
  }

  
  $("#btnCancelar").click(function () {
    $("#formUsuario")[0].reset();
    limpiarErrores();
  });

  
  $("#formUsuario").submit(function (e) {
    e.preventDefault();
    limpiarErrores();
    let valido = true;

    const nombre = $("#nombre").val().trim();
    const usuario = $("#usuario").val().trim();
    const fechaIngreso = $("#fechaIngreso").val().trim();
    const email = $("#email").val().trim();

    if (!nombre) {
      $("#error-nombre").text("El nombre es obligatorio.");
      valido = false;
    }
    if (!usuario) {
      $("#error-usuario").text("El usuario es obligatorio.");
      valido = false;
    }
    if (!fechaIngreso) {
      $("#error-fechaIngreso").text("La fecha es obligatoria.");
      valido = false;
    } else if (!validarFecha(fechaIngreso)) {
      $("#error-fechaIngreso").text("Formato de fecha inválido (dd/MM/yyyy).");
      valido = false;
    }
    if (!email) {
      $("#error-email").text("El email es obligatorio.");
      valido = false;
    } else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      $("#error-email").text("Email inválido.");
      valido = false;
    }

    if (valido) {
      alert("Usuario registrado correctamente!");
      $("#formUsuario")[0].reset();
    }
  });
});
