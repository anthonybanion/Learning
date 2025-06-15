//Dado 3 numeros {a, b, c} ordenarlos de mayor a menor
//Dia: 26/07/2024
//Version: 1.0


Proceso mayor_a_menor
	Definir a, b, c Como Entero;
	Leer a,b,c;
	
	//metodo de arbol
	Si (a > b) Entonces
		Si (a > c) Entonces
			Si (b > c) Entonces
				Escribir a , b, c;
				SiNo Si (b < c) Entonces
					Escribir a , c, b;
				FinSi		
			FinSi
		SiNo Si (a < c) Entonces
				Si ( b < c ) Entonces
					Escribir c , a, b;
				FinSi						
			FinSi
		FinSi
	SiNo Si (a<b) Entonces
			Si (a < c) Entonces
				Si (b < c) Entonces
					Escribir c , b, a;
				SiNo Si (b > c) Entonces
						Escribir b , c, a;
					FinSi		
				FinSi
			SiNo Si (a > c) Entonces
					Si ( b > c ) Entonces
						Escribir b , a, c;
					FinSi						
				FinSi
			FinSi
		FinSi
			
	FinSi
	
	
	
	
	
	
	
	
	
	
	
	
	
FinProceso
