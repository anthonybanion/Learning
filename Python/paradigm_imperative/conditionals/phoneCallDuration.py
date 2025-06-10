#Brief: Phone call duration
#Date: 05/11/2024
#Version: 1.0

#REnunciado: Dado la duracion(en minutos) de una llamada telefonica, calcular su costo_total, 
# de la siguiente manera: Hasta 5 min el costo_total es 0.9. Por encima de 5 min el, 
#costo_total es 0.9 + 0.2 por cada minuto adicional a los 5 primeros minutos. 
CUOTA_BASICA = 0.9
DURACION_BASICA = 5
CUOTA_PREMIUN = 1.1
costo_total = 0

duracion = float(input("ingrese la duración de la llamada en minutos: "))

if duracion < 0:
    print("La duración no puede ser negativa")
    exit
else:
    if duracion <= 1:
        costo_total = CUOTA_BASICA
        print(f"El costo_total de la llamada es: {costo_total}")

    elif (duracion > 1) or (duracion <= DURACION_BASICA):
        costo_total = CUOTA_BASICA * duracion
        print(f"El costo_total de la llamada es: {costo_total.__round__(2)}")

    else:
        duracion = duracion - DURACION_BASICA
        costo_total = DURACION_BASICA*CUOTA_BASICA + (duracion * CUOTA_PREMIUN)
        print(f"El costo_total de la llamada es: {costo_total.__round__(2)}")

