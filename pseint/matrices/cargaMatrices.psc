//Metodode carga de matrices 
//dia: 26/07/2024
//version 1.0


Proceso cargar_matrices
		definir matriz,i,j,k,m como entero;
		Dimension matriz[5,5];
		
		//cargado La Matriz por teclado
		para i <- 0 Hasta 4 Con Paso 1 hacer 
			para j <- 0 Hasta 4 Con Paso 1 hacer 
				escribir "ingrese un valor en la posicion ",i,",",j;
				leer matriz[i,j];
			FinPara
		FinPara
		
		//Mostrar la Matriz
		para k <- 0 Hasta 4 Con Paso 1 hacer 
			para m <- 0 Hasta 4 Con Paso 1 hacer 
				escribir sin bajar matriz[k,m], " ";  // Sin saltar es para las filas
			FinPara
			escribir ' ';  // Un salto para las columnas
		FinPara
FinProceso
