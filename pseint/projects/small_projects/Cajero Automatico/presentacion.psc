
SubProceso Logo
	definir i como entero;
	definir pausa Como Caracter;
	
	i <- 0;
	pausa <- " ";
Borrar Pantalla;
	Repetir
		para i <- 0 hasta 14 con paso 1 hacer
			segun i Hacer
		
			0:Escribir " ";
			1:Escribir "         ||||||||||";
			2:Escribir "       ||          ||";
			3:Escribir "      ||  |||||||   ||";
			4:Escribir "     ||   ||    ||   ||";
			5:Escribir "    ||    ||    ||    ||";
			6:Escribir "   ||     ||||||||     ||";
			7:Escribir "    ||    ||    ||    ||";
			8:Escribir "     ||   ||    ||   ||";
			9:Escribir "      ||  |||||||   ||";
			10:Escribir"       ||          ||";
			11:Escribir"         ||||||||||";	
			12:Escribir" ";
			13:Escribir"    ¡Estamos hay siempre! ";	
			FinSegun
			esperar 1 segundo;
		FinPara
		Esperar 1 Segundos;
		Borrar Pantalla;
	Hasta Que pausa <> " ";
FinSubProceso



Proceso presentacion
	Logo();	
	
FinProceso
