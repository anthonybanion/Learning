#Brief: Pizza
#Date: 05/11/2024
#Version: 1.0

#la pizeria ofrece piza vegetariana o no vegetariana 
# los ingredientes para cada tipo de piza son: 
# ingredientes vegetariano: pimiento y tofu 
# no vegetariano: peperoni , jamon , y zalmon
#escribir un programa que pregunte al usuario si quiere una pizza
#vegetariana y en funcion a su respuesta 
#le muestre un menu con los ingresdientes
#solo puede elegir un ingrediente ademas del tomate y la muzarela 
# que estan en ytodas las piza 
# al final se debe mostrar por pantalla si la pizza es vegetariana o no
# y todos los ingredientes que lleva 

opcion1 = int(input("Que tipo de pizza desea: \n 1) Vegetariana \n 2) No vegetariana \n Ingrese un ingrediente: "))
if (opcion1 == 1):
    ingrediente = input(" Ingredientes \n 1) Pimiento\n 2) Tofu \n Ingrese un ingrediente: ")
    tipo_piza = "vegetariana"
elif (opcion1 == 2):
    ingrediente = input(" Ingredientes \n 1) Pimiento\n 2) Tofu \n Ingrese un ingrediente: ")
    tipo_piza = "no vegetariana"