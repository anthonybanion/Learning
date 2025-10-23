//El usuario escribira la fecha de hoy y su fecha de nacimiento, ambos en formato dd/aaaa
//una funcion debera determinar su edad, la edad se mostrara mediante el programa principal 
//dia: 26/07/2024
//version: 1.0

Funcion calculo <- edad(f_nacimiento)
	Definir calculo Como Entero;
	//El calculo de la edad se realiza solo restando los años
	//que ocupan la posicion 6 hasta el 9
	calculo <-  ConvertirANumero(Subcadena(ConvertirATexto(FechaActual()),0,3)) - ConvertirANumero(Subcadena(f_nacimiento,6,9));
FinFuncion

//Programa princip
Proceso calculo_edad
	Definir fecha_hoy, fecha_nacimiento  Como Caracter;
	
	Escribir 'Ingrese la fecha de nacimiento en formato dd/mm/aaaa';
	Leer fecha_nacimiento;
	Escribir 'Su edad es: ', edad(fecha_nacimiento);
FinProceso
