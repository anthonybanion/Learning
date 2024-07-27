//Dado 3 numeros determinar informar 
//1) Si los 3 numeros son iguales
//2) Si estan ordenados ascendentemente
//3) Si estan ordenados descendentemente
//4) Si estan desordenado
//dia: 26/07/20204
//version 2.0


Proceso anidado
	Definir num1 , num2 , num3 Como Entero;

	leer num1, num2, num3;
	Si (num1 <> num2) y (num2 <> num3) y ( num1<> num3) Entonces
		Si (num1 < num2 ) y (num2 < num3) Entonces
			Escribir 'Ascendente';
			//aca si pones Si en ves de Sino  te sale por pantalla acendente y desordenado
		sino Si (num1 > num2 ) y (num2 > num3) Entonces
				Escribir 'Descendente';
			Sino 
				Escribir 'Desordenado';
			FinSi
		FinSi
	Sino si (num1 = num2) y (num2 = num3) y ( num1= num3) Entonces
			
			Escribir 'Iguales';
		FinSi
FinSi
FinProceso
