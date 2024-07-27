//Implementa Login (ABM), con el concepto de baja logica y baja fisica, para una lista de alumnos

//Detalle: Para no usar las mismas variables en todas las funcion, le posponemos al nombre de la variables, la primera letra en mayucula
//del nombre la funcion, por ejemplo en Menu(palabra_M, clave_M)
//De esta manera llevamos el control de las variables, evitando la sobre escritura. 

//observación: En la baja fisica hay que implementar el barrado de la posicion, y hacer un corrimiento de los valores para poder volver
//a usar la posicion anterior.(en la funcion de Administración)

//Dia: 26/07/2024
//Version: 2.0


Funcion Administracion(palabra_ad, clave_ad, bandera_ad, j_ad)
	Definir t, opcion1 , opcion3, cont Como Entero;
	definir  opcion2 Como Caracter;
	
	Repetir  //Menu de consultas del Adminisstrador
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
		escribir "***************** Administrativo *****************";
		Escribir "Opcion 1: Lista de Alumnos regulares:";
		escribir "Opcion 2: Eliminar:";
		escribir "Opcion 3: Cerrar";
		escribir "ingrese la opcion que desea realizar:";
		leer opcion1;
		esperar 1 Segundos;
		Borrar Pantalla;
		
		segun opcion1 Hacer
			1: escribir"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				Escribir "Lista de Alumnos regulares dado de Alta:";
				Escribir " ";
				cont <- 0;
				
				para t<- 0 hasta j_ad-1 Con Paso 1 Hacer
					
					si bandera_ad[t] = "Alta" entonces
						escribir cont,") ", palabra_ad[t], " ", clave_ad[t], " ", bandera_ad[t];
						cont <- cont + 1;
					FinSi
		
				FinPara
			
				escribir " ";
				escribir "Presione cualquier tecla para volver al menu administrativo:";
				Esperar Tecla;
				Borrar Pantalla;
			
			2:  escribir"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				Escribir "Eliminar registro:";
				Escribir " ";
				cont <- 0;
				
				para t<- 0 hasta j_ad- 1 Con Paso 1 Hacer
					escribir cont, ") ",palabra_ad[t], " ", clave_ad[t], " ", bandera_ad[t];
					cont <- cont + 1;
				FinPara
				
				escribir " ";
				escribir "Deseas eliminar algun registro";
				escribir "Presione (s) o (S) para comfirmar:";
				escribir "Presione cualquier otra tecla para canselar:";
				leer opcion2;
				
				si (opcion2 = "s") o (opcion2 = "S") Entonces
					escribir "Ingrese el numero de registro a eliminar:";
					escribir "El numero tiene que ser entre 0 y ",j_ad -1;
					leer opcion3; 
					
					si opcion3 > (j_ad -1) entonces
						escribir "Registro no encontrado";
						esperar 1 segundo;
					SiNo
						palabra_ad[opcion3] <- " ";  //Baja Fisica
						clave_ad[opcion3] <- " ";
						bandera_ad[opcion3] <- " ";
						escribir "Se elimino Exitosamente el registro";
						esperar 1 segundo;
					FinSi
					
				FinSi
				
				esperar 1 segundos;
				Borrar Pantalla;
			3: 
				Borrar Pantalla;
				Escribir "Fin de Administración";
				esperar 1 segundo;
				
			De Otro Modo:
				Borrar Pantalla;
				escribir "Valor incorrecto";
				esperar 1 segundo;
		finSegun
	Hasta Que  opcion1 >= 3
FinFuncion


funcion retornar <- busqueda_lineal(vector_B, palabra_B, pos_B Por Referencia, dim_B)
	definir retornar Como Logico;
	definir i Como Entero;
	retornar <- falso;
	
	para i <- 0 hasta dim_B-1 Con Paso 1 Hacer  //Ciclo de busqueda
		
		si vector_B[i] = palabra_B Entonces
			retornar <- Verdadero;
			pos_B <- i;
		FinSi
		
	FinPara
FinFuncion


Funcion retornar <- Comparacion(vector_C, cero_C, dim_C)  //Funcion de comparación de un vector con el vector vacio
	Definir i Como Entero;
	definir retornar Como Logico;
	
	retornar <- Falso;
	i <- 0;
	
	Repetir  //verificaion de vector vacio
		
		si vector_C[i] = cero_C[i] Entonces
			retornar <- Verdadero;
		sino 
			retornar <- Falso;
		FinSi
		
		i <- i +1;
	Hasta Que (retornar = Falso) o (i = dim_C-1)	
FinFuncion


Funcion Inicializacion(vector, dim_I)  //Funcion de Inicialización
	Definir i Como Entero;
	
	para i <- 0 hasta dim_I-1 Con Paso 1 Hacer
		vector[i] <- "0";
	FinPara
FinFuncion

Funcion Modificar(vector_palabra_Mo, vector_clave_Mo, pos1_Mo, pos2_Mo, dim_Mo, bandera_Mo)
	definir opcion Como Caracter;
	
	pos1_Mo <- 0;
	pos2_Mo <- 0;
	escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
	escribir "******************** Modificar ********************";
	escribir "Desea modificar la contraseña";
	escribir "Presione (s o (S) para comfirmar:";
	escribir "Presione cualquier otra tecla para canselar la modificación:";
	leer opcion;
	
	Si (opcion = "s") o (opcion = "S") Entonces
		Borrar Pantalla;
		Login(vector_palabra_Mo, vector_clave_Mo, pos1_Mo, pos2_Mo, dim_Mo, bandera_Mo);
		
		si bandera_Mo[pos1_Mo] = "Alta" Entonces
			escribir "Escribe la nueva contraseña:";
			leer vector_clave_Mo[pos2_Mo]; 
			Borrar Pantalla;
		
			mientras Longitud(vector_clave_Mo[pos2_Mo]) < 4 Hacer  //Verificación de contraseña con mas de 4 digitos
				escribir "Usa 4 caracteres como mínimo para la contraseña";
				esperar 1 Segundos;
				escribir "ingrese una contraseña ";
				leer vector_clave_Mo[pos2_Mo];
				Borrar Pantalla;
			FinMientras
		
			escribir "La modificación fue exitosa";
			esperar 1 segundo;
			Borrar Pantalla;
		FinSi
		
	SiNo
		escribir "Se canselo la modificación:";
		esperar 1 segundo;
		Borrar Pantalla;
	FinSi
FinFuncion


Funcion Baja(vector_palabra_B, vector_clave_B, pos1_B, pos2_B, dim_B, bandera_B)
	definir opcion Como Caracter;
	
	pos1_B <- 0;
	pos2_B <- 0;
	escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
	escribir "******************** Baja ********************";
	escribir "Desea realizar la Baja del sistema";
	escribir "Presione (s) o (S) para comfirmar:";
	escribir "Presione cualquier otra tecla para canselar la baja:";
	leer opcion;
	
	Si (opcion = "s") o (opcion = "S") Entonces  //Confirmación de baja del sistema
		Borrar Pantalla;
		Login(vector_palabra_B, vector_clave_B, pos1_B, pos2_B, dim_B, bandera_B);
		
		si bandera_B[pos1_B] = "Alta" Entonces
			bandera_B[pos1_B] <- "Baja";  //Baja logica consiste en poner una bandera de aviso y no eliminarlo fisicamente del sistema
			Borrar Pantalla;
			escribir "La baja del sistema fue exitosa";
			esperar 1 segundo;
			Borrar Pantalla;
		FinSi
		
	SiNo
		escribir "Se canselo la baja del sistema";
		esperar 1 segundo;
		Borrar Pantalla;
	FinSi
FinFuncion

Funcion Registro(vector_palabra_R , vector_clave_R,j Por Referencia, bandera_R)
	escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
	escribir "******************** Registro ********************";
	escribir "ingrese el usuario para registrarse:";
	leer vector_palabra_R[j];
	Borrar Pantalla;
	escribir "ingrese la contraseña:";
	leer vector_clave_R[j];
	Borrar Pantalla;
	
	mientras Longitud(vector_clave_R[j]) < 4 Hacer  //Verificación de contraseña con mas de 4 digitos
		escribir "Usa 4 caracteres como mínimo para la contraseña";
		esperar 1 Segundos;
		escribir "ingrese una contraseña ";
		leer vector_clave_R[j];
		Borrar Pantalla;
	FinMientras
	
	Borrar Pantalla;
	bandera_R[j] <- "Alta";
	escribir "¡ Felicidades su registro fue Exitoso !";
	esperar 2 segundos;
	Borrar Pantalla;
FinFuncion


Funcion  Login(vector_palabra_L, vector_clave_L, pos1_L Por Referencia, pos2_L Por Referencia, dim_L, bandera_L)
	definir palabra_ingresada, clave_ingresada Como Caracter;
	escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
	escribir "******************** LOGIN ********************";
	
	repetir  //Coincidencias de usuario y contraseña 
		escribir "Ingrese Ususario";
		leer palabra_ingresada;
		escribir "Ingrese contraseña";
		leer clave_ingresada;
		Borrar pantalla;
		
		si (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L, dim_L) = Falso) o (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L, dim_L) = Falso) Entonces
			escribir "el usuario o la comtraseña es incorrecto:";
		FinSi	
		
		si (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L, dim_L) = Verdadero) y (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L, dim_L) = Verdadero) y (pos1_L <> pos2_L) Entonces
			escribir "el usuario o la comtraseña es incorrecto:";
		FinSi
		
		esperar 1 segundos;
		Borrar pantalla;
		
	hasta que  (busqueda_lineal(vector_palabra_L, palabra_ingresada, pos1_L, dim_L) = Verdadero) y (busqueda_lineal(vector_clave_L, clave_ingresada, pos2_L, dim_L) = Verdadero) y (pos1_L = pos2_L)
	
	Si bandera_L[pos1_L] = "Baja" Entonces  //Verificacion de borrado logico
		escribir "Usted esta dado de baja en el sistema:";
		esperar 2 Segundos;
		Borrar pantalla;
	SiNo
		escribir "Ingreso al sistema";
		esperar 1 Segundos;
		Borrar pantalla;
		
	FinSi
FinFuncion


Funcion Menu(vector_palabra_M, vector_clave_M, cero_M, dim_M)
	definir opcion, j, pos1_M, pos2_M como entero;
	definir bandera_M Como Caracter;  // Definición de la bandera, es para el borrado logico
	Dimension bandera_M[dim_M];

	Inicializacion(bandera_M, dim_M);  	//inicializando
	pos1_M <- 0;
	pos2_M <- 0;
	j <- 0;

	Repetir
		Borrar Pantalla;
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";	
		escribir "******************** MENU ********************";
		escribir "Opcion 1: Registro";
		escribir "Opcion 2: Login";
		escribir "Opcion 3: Modificar";
		escribir "Opcion 4: Baja";
		escribir "Opcion 5: Administrativo:";
		escribir "Opcion 6: cerrar:";
		escribir "ingrese la opcion que desea realizar:";
		leer opcion;
		esperar 1 Segundos;
		Borrar Pantalla;		

		segun opcion hacer 
			1: 
				Registro(vector_palabra_M, vector_clave_M, j, bandera_M);
				j <- j + 1;
				
			2: //Verificacion de registro
				si (comparacion(vector_palabra_M, cero_M, dim_M) = Verdadero) o (comparacion(vector_clave_M, cero_M, dim_M) = Verdadero) Entonces
					escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Login(vector_palabra_M, vector_clave_M, pos1_M, pos2_M, dim_M, bandera_M);
				FinSi
				
			3: //Verificacion de registro
				si (comparacion(vector_palabra_M, cero_M, dim_M) = Verdadero) o (comparacion(vector_clave_M, cero_M, dim_M) = Verdadero) Entonces
					escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Modificar(vector_palabra_M, vector_clave_M, pos1_M, pos2_M, dim_M, bandera_M);
				FinSi
				
			4: //Verificacion de registro
				si (comparacion(vector_palabra_M, cero_M, dim_M) = Verdadero) o (comparacion(vector_clave_M, cero_M, dim_M) = Verdadero) Entonces
					escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Baja(vector_palabra_M, vector_clave_M, pos1_M, pos2_M, dim_M, bandera_M);
				FinSi
				
			5: //Verificacion de registro
				si (comparacion(vector_palabra_M, cero_M, dim_M) = Verdadero) o (comparacion(vector_clave_M, cero_M, dim_M) = Verdadero) Entonces
					escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Administracion(vector_palabra_M, vector_clave_M, bandera_M, j);
				FinSi
			6:
				Borrar Pantalla;
				Escribir "Fin del proceso";
			De Otro Modo:
				Borrar Pantalla;
				escribir "Valor incorrecto";
		FinSegun
		
	Hasta Que  opcion >= 6
FinFuncion


Proceso baja_logica_fisica //Programa principla
	definir vector_palabra, vector_clave, cero Como Caracter;
	definir dim  Como Entero;
	dim <- 20;  	//constante que nos cambia la longuitud del vector usuario y contraseña
	Dimension vector_palabra[dim], vector_clave[dim], Cero[dim];
	
	Inicializacion(vector_palabra, dim);  	//Inicialización 
	Inicializacion(vector_clave, dim);
	Inicializacion(cero, dim);
	
	Menu(vector_palabra, vector_clave, cero, dim);
FinProceso
