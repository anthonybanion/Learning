//Implementar login con el concepto de ABM, para una lista de 20 alumnos usando vector

//Detalle: Para no usar las mismas variables en todas las funcion, le posponemos al nombre de la variables, la primera letra en mayucula
//del nombre la funcion, por ejemplo en Menu(palabra_M, clave_M)
//De esta manera llevamos el control de las variables, evitando la sobre escritura. 

//Dia: 26/07/2024
//Version: 1.1


funcion retornar <- busqueda_lineal(vector_B, palabra_B, pos_B Por Referencia)  
	definir retornar Como Logico;
	definir i Como Entero;
	
	retornar <- falso;
	para i <- 0 hasta 19 Con Paso 1 Hacer
		si vector_B[i] = palabra_B Entonces
			retornar <- Verdadero;
			pos_B <- i;
		FinSi
	FinPara
FinFuncion


Funcion retornar <- Comparacion(vector_C, cero_C)  //Funcion de comparación  de un vector con vector nulo
	Definir i Como Entero;
	definir retornar Como Logico;

	retornar <- Falso; 	//Inicialización de variables
	i <- 0;
	
	Repetir  //verificaion de vector vacio
		si vector_C[i] = cero_C[i] Entonces
			retornar <- Verdadero;
		sino 
			retornar <- Falso;
		FinSi
		i <- i +1;
	Hasta Que (retornar = Falso) o (i= 19)	
FinFuncion


Funcion Inicializacion(vector_palabra_I, vector_clave_I, cero_I)  //Inicialización de vectores
	Definir i Como Entero;
	para i <- 0 hasta 19 Con Paso 1 Hacer
		vector_palabra_I[i] <- "0";
		vector_clave_I[i] <- "0";
		cero_I[i] <- "0";
	FinPara	
FinFuncion


Funcion Modificar(vector_palabra_Mo, vector_clave_Mo, pos1_Mo, pos2_Mo)
	definir opcion Como Caracter;
	pos1_Mo <- 0;
	pos2_Mo <- 0;
	
	escribir "******************** Modificar ********************";
	escribir "Desea modificar la contraseña";
	escribir "Presione (s) o (S) para comfirmar:";
	escribir "Presione cualquier otra tecla para canselar la modificación:";
	leer opcion;
	Si (opcion = "s") o (opcion = "S") Entonces
		Borrar Pantalla;
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
		Login(vector_palabra_Mo, vector_clave_Mo, pos1_Mo, pos2_Mo);
		escribir "Escribe la nueva contraseña:";
		leer vector_clave_Mo[pos2_Mo]; 
		Borrar Pantalla;
		
		mientras Longitud(vector_clave_Mo[pos2_Mo]) < 4 Hacer  //Ciclo de verificación de contraseña con mas de 4 digitos
			escribir "Usa 4 caracteres como mínimo para la contraseña";
			esperar 1 Segundos;
			escribir "ingrese una contraseña ";
			leer vector_clave_Mo[pos2_Mo];
			Borrar Pantalla;
		FinMientras
		
		escribir "La modificación fue exitosa";
		esperar 2 segundo;
		Borrar Pantalla;
	SiNo
		escribir "Se canselo la modificación:";
		esperar 2 segundo;
		Borrar Pantalla;
	FinSi
FinFuncion


Funcion Baja(vector_palabra_B, vector_clave_B, pos1_B, pos2_B)  //Baja fisica
	definir opcion Como Caracter;
	pos1_B <- 0;
	pos2_B <- 0;
	escribir "******************** Baja ********************";
	escribir "Desea realizar la Baja del sistema";
	escribir "Presione (s) o (S) para comfirmar:";
	escribir "Presione cualquier otra tecla para canselar la baja:";
	leer opcion;

	Si (opcion = "s") o (opcion = "S") Entonces  	//Confirmacion de baja del sistema
		Borrar Pantalla;
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
		Login(vector_palabra_B, vector_clave_B, pos1_B, pos2_B);
		vector_palabra_B[pos1_B] <- " ";  	
		vector_clave_B[pos2_B] <- " ";
		Borrar Pantalla;
		escribir "La baja del sistema fue exitosa";
		esperar 2 segundo;
		Borrar Pantalla;
	SiNo
		escribir "Se canselo la baja del sistema";
		esperar 2 segundo;
		Borrar Pantalla;
	FinSi
FinFuncion


Funcion Registro(vector_palabra_R , vector_clave_R,j Por Referencia)

		escribir "******************** Registro ********************";
		escribir "ingrese el usuario para registrarse:";
		leer vector_palabra_R[j];
		Borrar Pantalla;
		escribir "ingrese la contraseña:";
		leer vector_clave_R[j];
		Borrar Pantalla;
	
	mientras Longitud(vector_clave_R[j]) < 4 Hacer  	//Verificación de contraseña con mas de 4 digitos
		escribir "Usa 4 caracteres como mínimo para la contraseña";
		esperar 1 Segundos;
		escribir "ingrese una contraseña ";
		leer vector_clave_R[j];
		Borrar Pantalla;
	FinMientras
	
	Borrar Pantalla;
	escribir "¡ Felicidades su registro fue Exitoso !";
	esperar 2 segundos;
	Borrar Pantalla;
FinFuncion


Funcion  Login(vector_palabra_L, vector_clave_L, pos1_L Por Referencia, pos2_L Por Referencia)
	definir palabra_ingresada, clave_ingresada Como Caracter;
	
	escribir "******************** LOGIN ********************";
	
	repetir   	//Coincidencias de usuario y contraseña 
		escribir "Ingrese Ususario";
		leer palabra_ingresada;
		escribir "Ingrese contraseña";
		leer clave_ingresada;
		Borrar pantalla;
		
		si (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L) = Falso) o (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L) = Falso) Entonces
			escribir "el usuario o la comtraseña es incorrecto:";
		FinSi	
		
		si (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L) = Verdadero) y (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L) = Verdadero) y (pos1_L <> pos2_L) Entonces
			escribir "el usuario o la comtraseña es incorrecto:";
		FinSi
		
		esperar 1 segundos;
		Borrar pantalla;
	hasta que  (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L) = Verdadero) y (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L) = Verdadero) y (pos1_L = pos2_L)
	
	escribir "Ingreso al sistema";
	esperar 1 Segundos;
	Borrar pantalla;
FinFuncion


Funcion Menu(vector_palabra_M, vector_clave_M, cero_M)
	definir opcion, j, pos1_M, pos2_M como entero;

	pos1_M <- 0;
	pos2_M <- 0;
	j <- 0;
	
	Repetir
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";	
		escribir "******************** MENU ********************";
		escribir "Opcion 1: Registro";
		escribir "Opcion 2: Login";
		escribir "Opcion 3: Modificar";
		escribir "Opcion 4: Baja";
		escribir "Opcion 5: cerrar";
		escribir "ingrese la opcion que desea realizar:";
		leer opcion;
		esperar 1 Segundos;
		Borrar Pantalla;		
		
		segun opcion hacer 
			1: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				Registro(vector_palabra_M, vector_clave_M, j);
				j <- j + 1;  //Nos informa la posicion de registro
				
			2: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si (comparacion(vector_palabra_M, cero_M) = Verdadero) o (comparacion(vector_clave_M, cero_M) = Verdadero) Entonces  //Condicion de verificacion de Registro previo
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Login(vector_palabra_M, vector_clave_M, pos1_M, pos2_M);
				FinSi
			
			3: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si (comparacion(vector_palabra_M, cero_M) = Verdadero) o (comparacion(vector_clave_M, cero_M) = Verdadero) Entonces  	//Condicion de verificacion de Registro previo
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Modificar(vector_palabra_M, vector_clave_M, pos1_M, pos2_M);
				FinSi
				
			4: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si (comparacion(vector_palabra_M, cero_M) = Verdadero) o (comparacion(vector_clave_M, cero_M) = Verdadero) Entonces  //Condicion de verificacion de Registro previo
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Baja(vector_palabra_M, vector_clave_M, pos1_M, pos2_M);
				FinSi
				
			De Otro Modo:
				escribir "Fin del proceso";
		FinSegun
		
	Hasta Que  opcion >= 5
FinFuncion


Proceso ABM_login_multi_usuario  //Programa principla
	Definir vector_palabra, vector_clave, cero Como Caracter;  //Definicion de variables globales
	Dimension vector_palabra[20], vector_clave[20], Cero[20];
	
	Inicializacion(vector_palabra, vector_clave, cero);  	
	Menu(vector_palabra, vector_clave, cero);	
FinProceso
