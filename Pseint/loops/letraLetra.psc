//Ingrese una palabra y muestralo letra por letra 
//dia: 26/07/2024
//version: 1.0 

Proceso letra_x_letra
	definir palabra, letra como caracter;
	definir long, i como entero;
	escribir "Igrese una palabra";
	leer palabra;
	long <- longitud(palabra);
	para i <- 0 hasta long con paso 1 Hacer
		borrar pantalla;
		letra <- subcadena(palabra,i,i);
		escribir "",letra;
		esperar 1 segundos;
	FinPara
FinProceso
