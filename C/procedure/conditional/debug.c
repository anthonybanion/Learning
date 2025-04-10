#include <stdio.h>

int main() {
    char nombre[50];
    int numero;

    printf("Ingresa tu nombre: ");
    scanf("%s", nombre);

    printf("Hola %s, ingresa un número: ", nombre);
    scanf("%d", &numero);

    if (numero % 2 == 0) {
        printf("El número %d es PAR.\n", numero);
    } else {
        printf("El número %d es IMPAR.\n", numero);
    }

    return 0;
}
