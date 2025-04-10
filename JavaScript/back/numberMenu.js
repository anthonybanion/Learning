const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let numero = null;

function mostrarMenu() {
  console.log("\n=== MENÚ ===");
  console.log("1. Ver si el número es PAR o IMPAR");
  console.log("2. Ver si el número es POSITIVO o NEGATIVO");
  console.log("S. Salir");
  rl.question("Elegí una opción: ", manejarOpcion);
}

function manejarOpcion(opcion) {
  switch (opcion.toUpperCase()) {
    case "1":
      if (numero % 2 === 0) {
        console.log(`👉 El número ${numero} es PAR`);
      } else {
        console.log(`👉 El número ${numero} es IMPAR`);
      }
      mostrarMenu();
      break;

    case "2":
      if (numero > 0) {
        console.log(`✅ El número ${numero} es POSITIVO`);
      } else if (numero < 0) {
        console.log(`⚠️ El número ${numero} es NEGATIVO`);
      } else {
        console.log(`🟡 El número es CERO`);
      }
      mostrarMenu();
      break;

    case "S":
      console.log("👋 ¡Hasta luego!");
      rl.close();
      break;

    default:
      console.log("❌ Opción no válida.");
      mostrarMenu();
      break;
  }
}

function iniciarPrograma() {
  rl.question("📥 Ingresá un número: ", (input) => {
    numero = parseFloat(input);

    if (isNaN(numero)) {
      console.log("❌ Eso no es un número válido.");
      iniciarPrograma(); // vuelve a pedirlo
    } else {
      mostrarMenu();
    }
  });
}

iniciarPrograma();
