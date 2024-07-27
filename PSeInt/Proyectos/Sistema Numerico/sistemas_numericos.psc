//Sistemas_numericos es un programa que realize el pasaje:
//1) de base 10 a base {2, 8, 16}
//2) de base {2, 8, 16} a base 10
//3) de base {2, 8, 16} a base {2, 8, 16}

//observacion: la validación tiene que ser por cada base en particular, por ejemplo para la base (2) numeros menores a {0;1}
//dia 26/07/2024
//Version 1.0


Funcion retorna <- decimal_binario(numero_ingresado, base_salida)  //Para pasar de decimal a binario
	Definir digito, union_de_digitos, retorna Como Cadena;
	Definir numero_auxiliar Como Entero;
	
	digito           <- ' ';
	union_de_digitos <- ' ';
	numero_auxiliar  <- ConvertirANumero(numero_ingresado);
	
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
	Definir retorna, i Como Entero;
	Definir letra Como Caracter;
	retorna <- 0;

	para i <- 1 Hasta Longitud( numero_ingresado)  Con Paso 1 Hacer  	//CIclo de conversion
		letra <- Subcadena(numero_ingresado, Longitud(numero_ingresado) -i,Longitud(numero_ingresado) -i);  //Tomo de derecha a izquierda cada digito
		
		Si base_entrada = 16  Entonces  //La base 16, abre la posibilidad de usar las letras {A; B; C; D; E; F}
			
			Si  letra = 'A' entonces  //Como la estructura "Segun" no acepta letras y solo numeros implementamos If anidados
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
		
		retorna <- retorna + (base_entrada ^ (i-1)) * ConvertirANumero(letra);  //Metodo exponencial
	FinPara
FinFuncion

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

SubProceso Validacion(numero_ingresado Por Referencia, base_entrada Por Referencia, base_salida Por Referencia)
	Definir i, j Como Entero;
	Definir correcto, correcto2 Como Logico;
	
	correcto <- Falso;
	
	Repetir  //Validacion de base de entrada, solo se admiten valores: {2, 8, 10, 16}
		
		Si (base_entrada = 2) o (base_entrada = 8) o (base_entrada = 16) o (base_entrada = 10)   Entonces
			correcto <- Verdadero;
		SiNo 
			Borrar Pantalla;
			Escribir 'Ingrese de vuelta la base de entrada';
			leer base_entrada;
		FinSi
		
    Hasta Que 	correcto = Verdadero;
	correcto <- Falso;
	//Validacion de base de salida, solo se admiten valores: {2, 8, 16}
	Repetir
	Si (base_salida = 2) o (base_salida = 8) o (base_salida = 16) o (base_salida = 10)   Entonces
		correcto <- Verdadero;
	SiNo 
		Borrar Pantalla;
		Escribir 'Ingrese de vuelta la base de salida';
		leer base_salida;
	FinSi
	Hasta Que correcto = Verdadero;
	
	correcto <- Falso;
	//Validacion del numero de entrada, solo se admite valores por digito del 0 al 9 
	//En caso que la base es 16, se admiten letras {A; B; C; D; E; F}
	Si (base_entrada = 2) o (base_entrada = 8)  o (base_entrada = 10) Entonces
		
		repetir 
			
			Para i <- 0 Hasta Longitud(numero_ingresado)-1 Con Paso 1 Hacer
				
				Para j <- 0 Hasta 9 Con Paso 1 Hacer
					
					Si  (Subcadena(numero_ingresado,i,i) = ConvertirATexto(j) ) Entonces
						correcto <- Verdadero;
						j <- 9;
					SiNo
						correcto <- Falso;
					Finsi
					
				FinPara
				
				si correcto = Falso Entonces
					i<- Longitud(numero_ingresado)-1;
				FinSi
				
			FinPara
			escribir correcto;
			SI correcto = Falso Entonces
				Borrar Pantalla;
				Escribir 'Ingrese de vuelta numero entrada';
				leer numero_ingresado;
			FinSi
		
		Hasta Que correcto = Verdadero
		
	SiNo Si (base_entrada = 16) entonces
			
			repetir 
				
				Para i <- 0 Hasta Longitud(numero_ingresado)-1 Con Paso 1 Hacer
					
					Para j <- 0 Hasta 9 Con Paso 1 Hacer
						
						Si  (Subcadena(numero_ingresado,i,i) = ConvertirATexto(j) o (Subcadena(numero_ingresado,i,i) = 'A') o (Subcadena(numero_ingresado,i,i) = 'B') o (Subcadena(numero_ingresado,i,i) = 'C') o (Subcadena(numero_ingresado,i,i) = 'D') o (Subcadena(numero_ingresado,i,i) = 'E') o (Subcadena(numero_ingresado,i,i) = 'F')) Entonces
							correcto <- Verdadero;
							j <- 9;
						SiNo
							correcto <- Falso;
						Finsi
						
					FinPara
					
					si correcto = Falso Entonces
						i<- Longitud(numero_ingresado)-1;
					FinSi
					
				FinPara
				escribir correcto;
				SI correcto = Falso Entonces
					Borrar Pantalla;
					Escribir 'Ingrese de vuelta numero entrada';
					leer numero_ingresado;
				FinSi
				
			Hasta Que correcto = Verdadero
		FinSI
	FinSi
FinSubProceso

SubProceso Menu(numero_ingresado, base_entrada, base_salida)
	Escribir 'Ingrese el numero:';
	Leer numero_ingresado;
	Escribir 'Ingrese la base de entrada ';
	Leer base_entrada;
	Escribir 'Ingrese la base de salida:';
	Leer base_salida;
	validacion(numero_ingresado, base_entrada, base_salida);  //Validacion de datos de entrada
	
	Si (base_salida = 10 y base_entrada= 2) o (base_salida = 10 y base_entrada= 8) o (base_salida = 10 y base_entrada= 16) Entonces  //De base {2, 4, 8} a base 10
		Escribir binario_decimal(numero_ingresado, base_entrada);
		
	SiNo Si (base_salida = 2 y base_entrada= 10) o (base_salida = 8 y base_entrada= 10) o (base_salida = 16 y base_entrada= 10) Entonces // De base 10 a base {2, 4, 8}
			Escribir decimal_binario(numero_ingresado, base_salida);
		FinSi
		
	FinSi
FinSubProceso


SubProceso Inicializacion(numero_ingresado Por Referencia, base_entrada Por Referencia, base_salida Por Referencia)
	numero_ingresado <- '';
	base_entrada     <- 0;
	base_salida      <- 0;
FinSubProceso


Proceso sistemas_numericos  //Programa principal
	Definir  base_entrada, base_salida Como Entero;
	Definir numero_ingresado como caracter;
	
	Portada();  //Pantalla inicial
	Inicializacion(numero_ingresado, base_entrada, base_salida);
	Menu(numero_ingresado, base_entrada, base_salida);
FinProceso














