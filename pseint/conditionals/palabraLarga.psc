//Ingresa dos palabras y se compara cual es la palabra mas larga
//Dia: 26/07/2024
//Version: 1.0


Proceso palabra_mas_larga
	definir palabra1, palabra2 como caracter;
	definir long1, long2 como entero;
	escribir "ingrese la primera palabra:";
	leer palabra1;
	escribir "ingrese la segunda palabra:";
	leer palabra2;
	long1 <- longitud(palabra1);
	long2 <- longitud(palabra2);
	
	si long1 <> long2 entonces 
		si long1 > long2 entonces 
			escribir "La primera palabra es mas larga";
		sino 
			escribir "La segunda palabra es mas larga";
		FinSi
	sino 
		escribir "Son iguales";
	FinSi
	
	//********* el Si separados **************
	//si long1 > long2 entonces 
		//escribir "la primera palabra es mas larga";
		
	//FinSi
	
	//si long1 < long2 entonces 
		//escribir "la segunda palabra es mas larga";
	//Finsi
	
	//si long1 = long2 entonces 
		//escribir "Son iguales";
	//FinSi
FinProceso
