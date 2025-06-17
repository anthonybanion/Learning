#!/bin/bash

echo $1
#grep -w $1 historial.txt  # grep me busca todos las palabras pasadas por $1

#grep -w $1 historial.txt | cut -d " " -f6  me recorta las columnas

#wc -l $1.txt  contador de lineas

#grep -w $1 historial.txt | wc -l  # cantidad de lineas de historial

#find (aca va la ruta) -type f -name "*.txt" -size -2| wc -l  busco por tipo, nombre, tamaño, y un pay, cuento las caltidades listadas    


numero_linea=$(grep -w $1 historial.txt | wc -l)
echo "pesos 1 es:" $numero_linea


#----- ultimas lineas
echo $1

tail -$1 historial.txt > ultimos.txt
#-----
# Buscar
find $1 -size $2 | wc -l

#eexec()
#sed  modificar
#open abrir cosas

1997  head -2 prueba2.txt
 1998  head -4 prueba2.txt
 1999  head -2 prueba2.txt
 2000  tail -2 prueba2.txt
 2001  history 
 2002  nano hola.c
 2003  wc -l hola.c
 2004  wc -m hola.c
 2005  wc -w hola.c
 2006  man wc
 2007  grep hola hola.c
 2008  grep "hola" hola.c
 2009  nano hola.c
 2010  grep mundo hola.c
 2011  grep -w mundo hola.c
 2012  grep  mun hola.c
 2013  grep  -w mun hola.c
 2014  grep -w mun hola.c
 2015  grep -w mundo hola.c
 2016  nano hola.c
 2017  grep -w argentina hola.c
 2018  man grep
 2019  history
 2020  history >> historial.txt
 2021  ls
 2022  cat historial.txt
 2023  nano historial.txt
 2024  history > historial.txt

