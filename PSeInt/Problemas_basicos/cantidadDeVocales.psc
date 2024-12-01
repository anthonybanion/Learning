//Ingrese una variable por teclado y se debe indicar cuantas vocales tiene
//dia: 26/07/2024
//version: 1.0

Proceso cantidad_de_vocales
	definir palabra, vocales Como Caracter; 
	definir i, j , conteo Como Entero;
	
	conteo <- 0; 
	escribir ("Ingrese palabra");
	leer palabra;
	vocales <- "aeiou";  // Le asigno a la variable vocales todas las vocales
	
		para i <- 0 Hasta Longitud(palabra) - 1 Con Paso 1 Hacer  	// Primer ciclo es para recorrer los caracteres de la variable palabra 
			para j <- 0 hasta longitud(vocales) con paso 1 Hacer  // segundo ciclo es para recorre los caracteres de la variable vocales
				// comparo si un caracter de la variable palabra 
				// coinside con algunos de los caracter de la variable vocales 
				si Subcadena(palabra,i,i) == Subcadena(vocales,j,j) Entonces
					conteo <- conteo + 1;  // Si coinside contamos 1
				FinSi
			FinPara
		FinPara
		Escribir("La cantdad de vocales es:"); 
		escribir(conteo); 
	
FinProceso
