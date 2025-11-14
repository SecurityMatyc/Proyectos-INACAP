$(document).ready(function () {
  function limpiarErrores() {
    $(".error-message").text("");
    $("#formPost input, #formPost textarea").removeClass("input-error");
  }

  
  $("#btnCancelarPost").click(function () {
    $("#formPost")[0].reset();
    limpiarErrores();
  });

  
  $("#formPost").submit(function (e) {
    e.preventDefault();
    limpiarErrores();
    let valido = true;

    const userId = $("#userId").val().trim();
    const title = $("#title").val().trim();
    const body = $("#body").val().trim();

    if (!userId || isNaN(userId) || Number(userId) < 1) {
      $("#error-userId").text("El ID de usuario es obligatorio y debe ser mayor a 0.");
      $("#userId").addClass("input-error");
      valido = false;
    }
    if (!title) {
      $("#error-title").text("El título es obligatorio.");
      $("#title").addClass("input-error");
      valido = false;
    }
    if (!body) {
      $("#error-body").text("El contenido es obligatorio.");
      $("#body").addClass("input-error");
      valido = false;
    }

    if (valido) {
      alert("¡Publicación registrada correctamente!");
      $("#formPost")[0].reset();
    }
  });

  
  $("#formPost input, #formPost textarea").on("input", function () {
    if ($(this).val().trim() !== "") {
      $(this).removeClass("input-error");
      $(this).next(".error-message").text("");
    }
  });
});
