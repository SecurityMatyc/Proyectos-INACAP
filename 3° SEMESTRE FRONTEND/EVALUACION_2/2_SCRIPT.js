// Mostrar mensaje de error
function mostrarError(idCampo, mensaje) {
  const campo = document.getElementById(idCampo);
  const error = document.getElementById("error-" + idCampo);
  campo.classList.add("error");
  error.textContent = mensaje;
}

// Limpiar mensaje de error
function limpiarError(idCampo) {
  const campo = document.getElementById(idCampo);
  const error = document.getElementById("error-" + idCampo);
  campo.classList.remove("error");
  error.textContent = "";
}

// Validación de RUT chileno
function validarRut(rut) {
  rut = rut.replace(/\./g, "").replace(/-/g, "");
  const cuerpo = rut.slice(0, -1);
  let dv = rut.slice(-1).toUpperCase();

  let suma = 0;
  let multiplo = 2;

  for (let i = cuerpo.length - 1; i >= 0; i--) {
    suma += parseInt(cuerpo[i]) * multiplo;
    multiplo = multiplo < 7 ? multiplo + 1 : 2;
  }

  let dvEsperado = 11 - (suma % 11);
  dvEsperado = dvEsperado === 11 ? "0" : dvEsperado === 10 ? "K" : dvEsperado.toString();

  return dv === dvEsperado;
}

// Validación de formato de fecha dd/MM/yyyy
function validarFecha(fecha) {
  const regex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/;
  return regex.test(fecha);
}

// Validación de email
function validarEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

// Validación de contraseña
function validarPassword(pass) {
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$/;
  return regex.test(pass);
}

// Validación de archivo PDF o DOCX
function validarArchivo(file) {
  if (!file) return true;
  const tiposPermitidos = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
  ];
  return tiposPermitidos.includes(file.type);
}

// Validación principal
document.getElementById("registroForm").addEventListener("submit", function (e) {
  e.preventDefault();
  let valido = true;

  // Validar nombre
  const nombre = document.getElementById("nombreCompleto").value.trim();
  if (nombre === "") {
    mostrarError("nombreCompleto", "Debe ingresar su nombre completo.");
    valido = false;
  } else {
    limpiarError("nombreCompleto");
  }

  // Validar RUT
  const rut = document.getElementById("rut").value.trim();
  if (rut === "") {
    mostrarError("rut", "El RUT es obligatorio.");
    valido = false;
  } else if (!validarRut(rut)) {
    mostrarError("rut", "El RUT ingresado no es válido.");
    valido = false;
  } else {
    limpiarError("rut");
  }

  // Validar fecha si existe
  const fecha = document.getElementById("fechaNacimiento").value.trim();
  if (fecha && !validarFecha(fecha)) {
    mostrarError("fechaNacimiento", "Formato inválido. Use dd/MM/yyyy.");
    valido = false;
  } else {
    limpiarError("fechaNacimiento");
  }

  // Validar archivo
  const archivo = document.getElementById("cv").files[0];
  if (archivo && !validarArchivo(archivo)) {
    mostrarError("cv", "Archivo inválido. Solo se permite PDF o DOCX.");
    valido = false;
  } else {
    limpiarError("cv");
  }

  // Validar email
  const email = document.getElementById("email").value.trim();
  if (email === "") {
    mostrarError("email", "Debe ingresar su email.");
    valido = false;
  } else if (!validarEmail(email)) {
    mostrarError("email", "El email ingresado no es válido.");
    valido = false;
  } else {
    limpiarError("email");
  }

  // Validar contraseña
  const pass = document.getElementById("password").value;
  if (pass === "") {
    mostrarError("password", "Debe ingresar una contraseña.");
    valido = false;
  } else if (!validarPassword(pass)) {
    mostrarError("password", "Debe tener mayúscula, minúscula, número y 6-12 caracteres.");
    valido = false;
  } else {
    limpiarError("password");
  }

  // Validar repetir contraseña
  const repetir = document.getElementById("repetirPassword").value;
  if (repetir === "") {
    mostrarError("repetirPassword", "Debe repetir la contraseña.");
    valido = false;
  } else if (repetir !== pass) {
    mostrarError("repetirPassword", "Las contraseñas no coinciden.");
    valido = false;
  } else {
    limpiarError("repetirPassword");
  }

  // Mostrar mensaje final
  if (valido) {
    alert("✅ Formulario enviado correctamente.");
    document.getElementById("registroForm").reset();
    document.querySelectorAll(".error-message").forEach(e => e.textContent = "");
    document.querySelectorAll("input, select").forEach(e => e.classList.remove("error"));
  } else {
    alert("❌ El formulario contiene errores. Por favor, revíselos.");
  }
});

// Botón Cancelar
document.getElementById("btnCancelar").addEventListener("click", function () {
  document.getElementById("registroForm").reset();
  document.querySelectorAll(".error-message").forEach(e => e.textContent = "");
  document.querySelectorAll("input, select").forEach(e => e.classList.remove("error"));
});
