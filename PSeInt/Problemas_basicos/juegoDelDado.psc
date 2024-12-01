//Juago del dado, dos juagadores tiran un dado en turnos distintos 
//mostrar el ganador
//Dia: 26/07/2024
//Version: 1.0


Proceso numero_alto
	definir dado1, dado2 Como Entero;
	escribir "***************** NUMERO ALTO *************";
	escribir "Presione cualquier tecla para tirar el primer dado:";
	esperar tecla;
	dado1 <- aleatorio(1,6);
	escribir "el primer dado salio: ", dado1;
	esperar 2 segundos;
	escribir "Presione cualquier tecla para tirar el segundo dado:";
	esperar tecla;
	dado2 <- aleatorio(1,6);
	escribir "el segundo dado salio: ", dado2;
	esperar 2 segundos;
		//Si anidado
		si dado1 <> dado2 entonces 
			si dado1 > dado2 entonces 
				escribir "el ganador es el primer jugador ";
			sino 
				escribir "el ganador es el segundo jugador ";
			FinSi
		sino 
			escribir "EMPATE";
		FinSi
		//********* el Si separados **************
		//si dado1 > dado2 entonces 
		//	escribir "el ganador es el primer jugador ";
		//FinSi
		
		//si dado1 < dado2 entonces 
		//	escribir "el ganador es el segundo jugador ";
		//FinSi
		
		//si dado1 = dado2 entonces 
		//	escribir "EMPATE ";
		//Finsi
		//****************************************
FinProceso
