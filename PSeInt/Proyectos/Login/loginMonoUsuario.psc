//Implementar un login y alta de un solo usuario

//Detalle: Para no usar las mismas variables en todas las funcion, le posponemos al nombre de la variables, la primera letra en mayucula
//del nombre la funcion, por ejemplo en Menu(palabra_M, clave_M)
//De esta manera llevamos el control de las variables, evitando la sobre escritura. 

//Dia: 26/07/2024
//version: 1.0


Funcion Registro(palabra_R por Referencia,clave_R Por Referencia)
	escribir "******************** Registro ********************";
	escribir "ingrese el usuario para registrarse:";
	leer palabra_R;
	Borrar Pantalla;
	escribir "ingrese una contraseña ";
	leer clave_R;
	Borrar Pantalla;
	
	mientras Longitud(clave_R) < 4 Hacer  //Ciclo de verificación de contraseña con mas de 4 digitos
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

	repetir  //Ciclo de coincidencias de usuario y contraseña 
		escribir "******************** LOGIN ********************";
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


Funcion Menu(palabra_M, clave_M)
	definir opcion como entero;

	Repetir  	//cartelera del Menu
		escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";	 
		escribir "******************** MENU ********************";
		escribir "Opcion 1: Registro";
		escribir "Opcion 2: Login";
		escribir "Opcion 3: cerrar";
		escribir "ingrese la opcion que desea realizar:";
		leer opcion;
		esperar 1 Segundos;
		Borrar Pantalla;	
		
		segun opcion hacer 
			1: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				Registro(palabra_M, clave_M);
				
			2: escribir "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@";
				
				si (palabra_M = " ") o (clave_M = " ") Entonces  //Verifiación de registro
					Escribir "Ustede no a realizado el registro:";
					esperar 1 segundos;
					Borrar Pantalla;
				SiNo
					Login(palabra_M, clave_M);
				FinSi

			3: 
				Borrar Pantalla;
				escribir "Fin del programa";
				esperar 1 Segundos;
			
			De Otro Modo:
				Borrar Pantalla;
				escribir "Valor incorrecto";
				esperar 1 Segundos;
		FinSegun
		
	Hasta Que  opcion >= 3
FinFuncion


Proceso login_mono_usuario  //Programa principal
	definir palabra, clave Como Caracter;
	
	palabra <- " ";  //Inicialización de las variables
	clave <- " ";
	Menu(palabra,clave);
FinProceso
