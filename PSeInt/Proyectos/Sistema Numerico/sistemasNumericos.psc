

//sistemasNumericos es un programa que realize el pasaje:
//1) de base 10 a base {2, 8, 16}
//2) de base {2, 8, 16} a base 10
//3) de base {2, 8, 16} a base {2, 8, 16}

//observacion: la validación tiene que ser por cada base en particular, por ejemplo para la base (2) numeros menores a {0;1}
//dia 26/07/2024
//Version 1.0


Funcion retorna <- decimal_binario(numero_ingresado, base_salida)  //Para pasar de decimal a binario
	Definir digito, union_de_digitos, retorna Como Cadena;
	Definir numero_auxiliar Como Real;
	
	digito           <- ' ';
	union_de_digitos <- ' ';
	numero_auxiliar  <- ConvertirANumero(numero_ingresado);  //aca hay un error en la capacidad que acepta por eso use real
	
	Repetir  //proceso de conversion por divisiones sucesivas 
		digito <- ConvertirATexto(numero_auxiliar mod base_salida) ;  //Guardo digito a digito el resto de dividir el numero ingredsado por entre base de salida
		numero_auxiliar <- Trunc(numero_auxiliar / base_salida);  //Trunco el resultado de la divicion, para eliminar la parte decimal
		
		si base_salida = 16 Entonces  //La base 16, abre la posibilidad de usar las letras {A; B; C; D; E; F}
			
			segun ConvertirANumero(digito) hacer  
				10: digito <- 'A';
				11: digito <- 'B';
				12: digito <- 'C';
				13: digito <- 'D';
				14: digito <- 'E';
				15: digito <- 'F';
			FinSegun
			
		FinSi
		
		union_de_digitos <- concatenar(digito, union_de_digitos);  //Para formar el numero de salida, necesito unir todos los digitos
	Hasta Que numero_auxiliar < base_salida
  
  retorna <- Concatenar(ConvertirATexto(numero_auxiliar), union_de_digitos);  //Agrego el ultimo digito. Por que el ultimo digito es menor que la base de salida
FinFuncion


Funcion retorna <- binario_decimal(numero_ingresado, base_entrada)  //Funcion que realiza el pasaje de binario a decimal
	Definir  i Como Entero;
	Definir letra, retorna Como Caracter;
	retorna <- '';

	para i <- 1 Hasta Longitud( numero_ingresado)  Con Paso 1 Hacer  	//CIclo de conversion
		letra <- Subcadena(numero_ingresado, Longitud(numero_ingresado) -i,Longitud(numero_ingresado) -i);  //Tomo de derecha a izquierda cada digito
		
		Si base_entrada = 16  Entonces  //La base 16, abre la posibilidad de usar las letras {A; B; C; D; E; F}
			//Como la estructura "Segun" no acepta letras; solo acepta numeros, entonces implementamos If anidados
			Si  letra = 'A' entonces  
				letra <- '10';
				
			SiNO Si letra = 'B' entonces
					letra <- '11';
					
				SiNO Si letra = 'C' entonces
						letra <- '12';
						
					SiNO Si letra = 'D' entonces
							letra <- '13';
							
						SiNO Si letra = 'E' entonces
								letra <- '14';
								
							SiNO Si letra = 'F' entonces
									letra <- '15';
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		retorna <- concatenar(retorna, ConvertirATexto((base_entrada ^ (i-1)) * ConvertirANumero(letra))) ;  //Metodo exponencial
	FinPara
FinFuncion

//Realiza el pasaje del numero en base binaro de entrada a decinaml, despues de decimal a binario
Funcion retorno <- binario_binario (numero_ingresado, base_entrada, base_salida) 
	Definir retorno Como Caracter;
	Escribir binario_decimal(numero_ingresado, base_entrada);
	retorno <- decimal_binario(binario_decimal(numero_ingresado, base_entrada), base_salida);
FinFuncion

//Verifica si en numero ingresado es menor que la base y ademas si son numeros enteros validos
Funcion  retorno <- esMenor (numero_ingresado Por Referencia, base_entrada)
	Definir  retorno, digitoCorrecto, numeroCorrecto Como Logico;
	Definir i,j Como Entero;
	numeroCorrecto <- Verdadero;  //Asumo que el numero es correcto por defecto y busco la falla
	// Verifico para las bases {2, 8, 10}
	Si (base_entrada = 2) o (base_entrada = 8) o (base_entrada = 10)   Entonces
		Para i <- 0 Hasta Longitud(numero_ingresado)-1 Con Paso 1 Hacer  // recorro toda la logitud del numero ingresado
			digitoCorrecto <- Falso; //Asumo que el digito es incorrecto por defecto 
			Para j <- 0 Hasta base_entrada-1 Con Paso 1 Hacer  //recorro todos los digitos menores que la base
				
				Si  (Subcadena(numero_ingresado,i,i) = ConvertirATexto(j) ) Entonces  //Comparo caracter por caracter
					digitoCorrecto <- digitoCorrecto o Verdadero; //Si encuentro un verdadero, significa que el digito es correcto
				SiNo
					digitoCorrecto <- digitoCorrecto o Falso; //Por defecto se que es falso
				FinSi
				
			FinPara
			numeroCorrecto <- numeroCorrecto y digitoCorrecto; //Si alguno digito es falso, significa que el numero es incorrecto
		FinPara
		retorno <- numeroCorrecto;
		// Verifico para la base 16
	SiNo Si (base_entrada = 16) Entonces
			Para i <- 0 Hasta Longitud(numero_ingresado)-1 Con Paso 1 Hacer
				digitoCorrecto <- Falso;
				Para j <- 0 Hasta 9 Con Paso 1 Hacer
					// considero los valores {A=10; B=11; C=12; D=13; E=14; F=15}
					Si  (Subcadena(numero_ingresado,i,i) = ConvertirATexto(j) o (Subcadena(numero_ingresado,i,i) = 'A') o (Subcadena(numero_ingresado,i,i) = 'B') o (Subcadena(numero_ingresado,i,i) = 'C') o (Subcadena(numero_ingresado,i,i) = 'D') o (Subcadena(numero_ingresado,i,i) = 'E') o (Subcadena(numero_ingresado,i,i) = 'F')) Entonces
						digitoCorrecto <- digitoCorrecto o Verdadero; 
					SiNo
						digitoCorrecto <- digitoCorrecto o Falso;
					FinSi
					
				FinPara
				numeroCorrecto <- numeroCorrecto y digitoCorrecto; 
			FinPara
			retorno <- numeroCorrecto;
		FinSi
		
	FinSi
FinFuncion

//Verifica si en numero ingresado es menor que la base y ademas si son numeros enteros validos
SubProceso numeroMenorQueBase(numero_ingresado Por Referencia, base_entrada)
	repetir
		Si esMenor(numero_ingresado, base_entrada) = Falso Entonces
			Escribir "Numero ingresado incorrectamente";
			Escribir 'Ingrese el numero:';
			Leer numero_ingresado;
		SiNo
			Escribir "Numero ingresado correctamente";
		FinSi
	Hasta Que esMenor(numero_ingresado, base_entrada) = Verdadero
	
FinSubProceso


//Validacion del numero de entrada, solo se admite valores por digito del 0 al 9 
//En caso que la base de entrada es 16, se admiten letras {A; B; C; D; E; F}
SubProceso validacionDeNumero(numero_ingresado Por Referencia, base_entrada)
	
	Segun base_entrada Hacer
		2:
			numeroMenorQueBase(numero_ingresado, base_entrada);
		8:
			numeroMenorQueBase(numero_ingresado, base_entrada);
		10:
			numeroMenorQueBase(numero_ingresado, base_entrada);
		16:
			numeroMenorQueBase(numero_ingresado, base_entrada);
		De Otro Modo:
			Escribir "Base de entrada incorrecta";
	FinSegun
FinSubProceso

//Valida la base
SubProceso validacionDeBase( base Por Referencia)
	Definir correcto Como Logico;
	correcto <- Falso;
	
	Repetir  //Validacion de base de entrada, solo se admiten valores: {2, 8, 10, 16}
		
		Si (base = 2) o (base = 8) o (base = 16) o (base = 10)   Entonces
			correcto <- Verdadero;
		SiNo 
			Borrar Pantalla;
			Escribir 'Ingrese de vuelta la base, solo se admiten valores: {2, 8, 10, 16}';
			leer base;
		FinSi
		
    Hasta Que 	correcto = Verdadero;
FinSubProceso


SubProceso Menu(numero_ingresado, base_entrada, base_salida)
	Escribir 'Ingrese la base de entrada, solo se admiten valores: {2, 8, 10, 16}: ';
	Leer base_entrada;
	validacionDeBase(base_entrada);
	Escribir 'Ingrese el numero:';
	Leer numero_ingresado;
	validacionDeNumero(numero_ingresado, base_entrada);  //Validacioon de numero ingresado
	Escribir 'Ingrese la base de salida, solo se admiten valores: {2, 8, 10, 16}:';
	Leer base_salida;
	validacionDeBase(base_salida);
	
	Si (base_salida = 10 y base_entrada= 2) o (base_salida = 10 y base_entrada= 8) o (base_salida = 10 y base_entrada= 16) Entonces  //De base {2, 4, 8} a base 10
		Escribir binario_decimal(numero_ingresado, base_entrada);
		
	SiNo Si (base_salida = 2 y base_entrada= 10) o (base_salida = 8 y base_entrada= 10) o (base_salida = 16 y base_entrada= 10) Entonces // De base 10 a base {2, 4, 8}
			Escribir decimal_binario(numero_ingresado, base_salida);
	
	SiNo
		Escribir binario_binario(numero_ingresado, base_entrada, base_salida);
		FinSi
	FinSi
FinSubProceso


SubProceso Inicializacion(numero_ingresado Por Referencia, base_entrada Por Referencia, base_salida Por Referencia)
	numero_ingresado <- '';
	base_entrada     <- 0;
	base_salida      <- 0;
FinSubProceso

//Procedimiento de pantalla inicial
SubProceso Portada
	Escribir'                      ¡QUE BRUTO!  ';
	Escribir'********************************************************';
	Escribir'||||||  ||||||  ||||  ||  ||||||   ||||   ||      ||||||';
	Escribir'||  ||  ||  ||  ||||  ||  ||      ||  ||  ||      ||    ';
	Escribir'||||||  ||  ||  || || ||  || |||  ||||||  ||      ||||||';
	Escribir'||      ||  ||  ||  ||||  ||  ||  ||  ||  ||      ||    ';
	Escribir'||      ||||||  ||  ||||  ||||||  ||  ||  ||||||  ||||||';
	Escribir ' ';
	Escribir'         ||||||  ||||||  |||||   ||||||';
	Escribir'         ||      ||      ||  ||  ||  ||';
	Escribir'         ||      |||||   ||||||  ||  ||';
	Escribir'         ||      ||      ||  ||  ||  ||';
	Escribir'         ||||||  ||||||  ||  ||  ||||||';
	Escribir'????????????????????????????????????????????????????????';
	esperar 1 Segundos;
	Borrar Pantalla;
FinSubProceso

Proceso sistemasNumericos  //Programa principal
	Definir  base_entrada, base_salida Como Entero;
	Definir numero_ingresado como caracter;
	
	Portada();  //Pantalla inicial
	Inicializacion(numero_ingresado, base_entrada, base_salida);
	Menu(numero_ingresado, base_entrada, base_salida);
FinProceso














