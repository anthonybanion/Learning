//Programa que carga y muestra un vector
//dia: 296/07/2024
//version: 1.0


Proceso Cargar_Vector
	definir vector,i,j como entero;
	Dimension vector[5];
	
	//cargado de vector en foma manual
	//vector[0] <- 2;
	//vector[1] <- 25;
	//vector[2] <- 8;
	//vector[3] <- 6;
	//vector[4] <- 20;
	
	//cargado de vector por teclado
	para j <- 0 Hasta 4 Con Paso 1 hacer 
		escribir "ingrese un valor en la posicion ",j;
	leer vector[j];
	FinPara
	
	//Mostrar el vector
	para i <- 0 Hasta 4 Con Paso 1 hacer 
		escribir sin bajar vector[i], " ";
	FinPara
FinProceso
