//Se ingresa 5 palabras por teclado. Determinar con una funcion 
//cuantas letras A tiene cada una de ellas. En cada caso, informar 
//la cantidad mediante el prograa principal
//dia 26/07/2024
//version: 1.0


Funcion contador <- buscador(palabra)
	Definir contador, j como entero;
	
	contador <- 0;
	Para  j <- 0 hasta Longitud(palabra) -1 Hacer  //ciclo que recorrer la palabra caracter por caracter
		Si (Subcadena(palabra, j, j) == "a") o (Subcadena(palabra, j, j) == "A") Entonces  //Compara cada caracter con la letra "a" o "A"
			contador <- contador + 1;  //si coincide le agrega 1 al contador
		FinSi
	FinPara
FinFuncion

//Programa principal
Proceso buscando_a

	Definir palabra Como Caracter;
	Definir i Como Entero;
	
	Para i <- 0 Hasta  5 Con Paso 1 Hacer
		Escribir('Ingrese palabra:');
		Leer palabra;
		Escribir  buscador(palabra);
	FinPara
FinProceso
