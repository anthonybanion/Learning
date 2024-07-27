//Distintas operaciones con dos numeros 
//Dia: 26/07/2024
//Version: 1.0


Proceso calculadora_basica
	definir Num1, Num2, mul, div, res, sum Como Real; 
	definir op como entero;
	op <- 0;
	escribir "Ingrese los dos numeros operar:";
	leer Num1, Num2;
	sum <- Num1 + Num2;
	res <- Num1 - Num2;
	div <- Num1 / Num2;
	mul  <- Num1 * Num2;
	escribir "Elija una opcion:";
	escribir "********* MENU PRICIPAL *********";
	escribir "1: para la suma";
	escribir "2: para la resta";
	escribir "3: para la division";
	escribir "4: para la multiplicacion";
	
	leer op;
	segun op hacer
			1: escribir "la suma es:", sum; 
			2: escribir "la resta es:", res;
			3: escribir "la division es:", div;
			4: escribir "la multiplicacion es:", mul;
			de otro modo: 
				escribir "opcion invalida";
	FinSegun
	
FinProceso
