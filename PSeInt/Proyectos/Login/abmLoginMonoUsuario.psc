//Implementar un Login con el concepto ABM (alta baja y modificar) , para un solo usuario

//Detalle: Para no usar las mismas variables en todas las funcion, le posponemos al nombre de la variables, la primera letra en mayucula
//del nombre la funcion, por ejemplo en Menu(palabra_M, clave_M)
//De esta manera llevamos el control de las variables, evitando la sobre escritura. 

//Dia: 26/07/2024
//Version: 1.0


Funcion Modificar(palabra_Mo Por Referencia, clave_Mo Por Referencia)
	definir opcion Como Caracter;
	escribir "******************** Modificar ********************";
	escribir "Desea modificar la contraseña";
	escribir "Presione (s) o (S) para comfirmar:";
	esperar 1 segundo;
	escribir "Presione cualquier otra tecla para canselar la modificación:";
	leer opcion;
	
	Si (opcion = "s") o (opcion = "S") Entonces
		Borrar Pantalla;
		escribir "Escribe la nueva contraseña:";
		leer clave_Mo; 
		Borrar Pantalla;
		
		mientras Longitud(clave_Mo) < 4 Hacer  //Ciclo de verificación de contraseña con mas de 4 digitos
			escribir "Usa 4 caracteres como mínimo para la contraseña";
			esperar 1 Segundos;
			escribir "Escribe la nueva contraseña:";
			leer clave_Mo;	
			Borrar Pantalla;
		FinMientras
	
		escribir "La modificación fue exitosa";
		esperar 1 segundo;
		Borrar Pantalla;
	SiNo
		escribir "Se canselo la modificación:";
		esperar 1 segundo;
		Borrar Pantalla;
	FinSi
FinFuncion


Funcion Baja(palabra_B Por Referencia, clave_B Por Referencia)
	definir opcion Como Caracter;
	escribir "******************** Baja ********************";
	escribir "Desea realizar la Baja del sistema";
	escribir "Presione (s) o (S) para comfirmar:";
	esperar 1 segundo;
	escribir "Presione cualquier otra tecla para canselar la baja:";
	leer opcion;
	
		Si (opcion = "s") o (opcion = "S") Entonces  	//Confirmacion de baja del sistema
			palabra_B <- " ";  
			clave_B <- " ";
			Borrar Pantalla;
			escribir "La baja del sistema fue exitosa";
			esperar 1 segundo;
			Borrar Pantalla;
		SiNo
			escribir "Se canselo la baja del sistema";
			esperar 1 segundo;
			Borrar Pantalla;
		FinSi
FinFuncion


Funcion Registro(palabra_R por Referencia,clave_R Por Referencia)
	escribir "******************** Registro ********************";
	escribir "ingrese el usuario para registrarse:";
	leer palabra_R;
	Borrar Pantalla;
	escribir "ingrese una contraseña ";
	leer clave_R;
	Borrar Pantalla;
	
	mientras Longitud(clave_R) < 4 Hacer  	//Ciclo de verificación de contraseña con mas de 4 digitos
		escribir "Usa 4 caracteres como mínimo para la contraseña";
		esperar 1 Segundos;
		escribir "ingrese una contraseña ";
		leer clave_R;	
		Borrar Pantalla;
	FinMientras
	
	Borrar Pantalla;
	escribir "¡ Felicidades su registro fue Exitoso !";
	esperar 1 segundos;
	Borrar Pantalla;
FinFuncion


Funcion  Login(palabra_L Por Referencia,clave_L Por Referencia)
	definir palabra_ingresada, clave_ingresada Como Caracter;
	escribir "******************** LOGIN ********************";
	
	repetir  //coincidencias de usuario y contraseña 
		escribir "Ingrese Ususario";
		leer palabra_ingresada;
		escribir "Ingrese contraseña";
		leer clave_ingresada;
		Borrar pantalla;
		
		si (palabra_ingresada <> palabra_L) o (clave_ingresada <> clave_L) Entonces 
			escribir "el usuario o la comtraseña es incorrecto:";
		FinSi
		
		esperar 1 segundos;
		Borrar pantalla;
	hasta que (palabra_ingresada = palabra_L) y (clave_ingresada = clave_L)
	
	escribir "Ingreso al sistema";
	esperar 1 Segundos;
	Borrar pantalla;
FinFuncion


Funcion Retorna <- Verificacion(palabra_V, clave_V)
	Definir Retorna Como Logico; 
	Si (palabra_V = " ") o (clave_V = " ") Entonces  //Verifica si estan vacios las variables
		Retorna <- Verdadero;
	SiNo  //Verifica si estan cargadas las variables
		Retorna <- Falso;
	FinSi
FinFuncion


Funcion Menu(palabra_M, clave_M)
	definir opcion como entero;
	
	Repetir  //cartelera del Menu
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
				Registro(palabra_M, clave_M);
				
			2: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si Verificacion(palabra_M, clave_M) Entonces  //Condicion de verificacion de Registro 
					Escribir "Ustede no a realizado el registro:";
					esperar 2 segundos;
					Borrar Pantalla;
				SiNo
					Login(palabra_M, clave_M);
				FinSi
				
			3: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si Verificacion(palabra_M, clave_M) Entonces  //Condicion de verificacion de Registro
					Escribir "Ustede no a realizado el registro:";
					esperar 2 segundos;
					Borrar Pantalla;
				SiNo
					Modificar(palabra_M, clave_M);
				FinSi
				
			4: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si Verificacion(palabra_M, clave_M) Entonces 	 //Condicion de verificacion de Registro
					Escribir "Ustede no a realizado el registro:";
					esperar 2 segundos;
					Borrar Pantalla;
				SiNo
					Baja(palabra_M, clave_M);
				FinSi
				
			De Otro Modo:
				escribir "Fin del proceso";
		FinSegun
		
	Hasta Que  opcion >= 5
FinFuncion


Proceso ABM_login_mono_usuario  //Programa principla
	definir palabra, clave Como Caracter;
	
	palabra <- " ";
	clave <- " ";
	Menu(palabra,clave);
FinProceso
