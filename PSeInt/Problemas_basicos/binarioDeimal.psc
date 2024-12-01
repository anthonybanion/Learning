//Se recibe un binario de 3 digitos. Una funcion debera convertirla a decimal
//y debera mostrarse por pantalla desde el programa principal
//dia: 26/07/2024
//version 1.0


Funcion decimal <- convertidorBD(num_binario)
	
	Definir decimal, i Como Entero;
	Definir letra, txt Como Caracter;
	
	decimal <- 0;
	txt <- ConvertirATexto(num_binario);
	
	para i <- 1 Hasta Longitud( txt) Con Paso 1 Hacer 
		//Guardo cada caracter de derecha a izquierda, los valores solo pueden tomar {1,0} por ser binario
		letra <- Subcadena(txt, Longitud(txt) -i,Longitud(txt) -i);
		//Decinmal es un sumador, suma 2 elevado a la posicion, contando la posicion de derecha a izquierda
		//si la variable letra tiene valor 1 se realiza la suma, pero si tiene valor 0 se suma cero
		decimal <- decimal + (2 ^ (i-1)) * ConvertirANumero(letra);
	FinPara
FinFuncion


//Programa principal
Proceso binario_decimal
	
	Definir num_binario Como Entero;
	
	Escribir'Ingrese el numero binaraio:';
	Leer num_binario;
	Escribir convertidorBD(num_binario);	
FinProceso
