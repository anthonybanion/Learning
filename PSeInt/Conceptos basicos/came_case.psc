//Programa recibe una palabra y lo muestra en formato CameCase
// formato Came Case : holaMundo
//dia: 26/07/2024
//Version: 1.0

Proceso Came_Case
	definir palabra1, palabra2 como caracter;
	escribir "ingrese la primera palabra:";
	leer palabra1;
	escribir "ingrese la segunda palabra:";
	leer palabra2;
	//Genera una cadena de otra cadena Subcadena(cadena, posicion inicial, posicion final) 
	escribir palabra1, mayusculas(Subcadena(palabra2,0,0)), subcadena(palabra2,1,longitud(palabra2));
FinProceso
