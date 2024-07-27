//Escriba un programa que pida al usuario elegir entre "piedra", "papel","tijera"
//Una funcion realizara la jugada de la maquina, que tambien eligira entre las 3 posibilidades
//Otra funcion determinara quien gano. El programa se mostrara mediante el programa principal
//Dia: 26/07/2024
//Version 1.0


Funcion jugada <- maquina
	Definir  jugada Como Entero;
	
	jugada <- Aleatorio(1,3);  //valor de la jugada de la maquina que es aleatoria
	Escribir Sin Saltar'La maquina: ';
	segun jugada hacer
		1: Escribir 'Piedra';
		2: Escribir 'Papel';
		3: Escribir 'Tijera';			
	FinSegun
FinFuncion


Funcion resultado <- ganador(eleccion, jugada)
	Definir resultado Como Caracter;

	Si (eleccion = 1 y jugada = 3) o (eleccion = 2 y jugada = 1) o (eleccion = 3 y jugada = 2) Entonces  //Casos favorables donde gana el usuario
		resultado <- 'Usuario es el ganador ';
		SiNo 
		Si (eleccion = 1 y jugada = 2) o (eleccion = 2 y jugada = 3) o (eleccion = 3 y jugada = 1) Entonces  //Casos favorables donde gana la maquina
			resultado <-  'La maquina es el ganador';
			SiNo 
			Si eleccion = jugada Entonces  //Condicion de empate
			resultado<- 'Empate';
			FinSi
		FinSi
	FinSi	
FinFuncion


Proceso piedra_papel_tijera
	Definir eleccion Como Entero;
	
	Escribir '******* Piedra Papel o Tijera *******';
	Escribir '1) Piedra';
	Escribir '2) Papel';
	Escribir '3) Tijera';
	Escribir 'Elija una opcion';
	Leer eleccion;
	Escribir ganador(eleccion,maquina());
FinProceso
