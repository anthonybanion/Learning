#!/bin/bash
# ==========================================
#
# Script para montar una partición NTFS
#
# File: montar.sh
# Author: Anthony Bañon
# Created: 2025-06-15
# Last Updated: 2025-06-15
# ==========================================



# Definir el punto de montaje
MONTAJE="/media/anthony/D"
PARTICION="/dev/sda5"

# Verificar si el directorio de montaje existe
if [ ! -d "$MONTAJE" ]; then
  echo "Creando el directorio de montaje en $MONTAJE"
  sudo mkdir -p "$MONTAJE"
fi

# Intentar reparar la partición NTFS
echo "Reparando la partición NTFS..."
sudo ntfsfix "$PARTICION"

# Montar la partición
echo "Montando la partición $PARTICION en $MONTAJE"
sudo mount -t ntfs-3g "$PARTICION" "$MONTAJE"

# Verificar si el montaje fue exitoso
if mount | grep "$MONTAJE" > /dev/null; then
  echo "La partición se ha montado correctamente en $MONTAJE."
else
  echo "Hubo un error al montar la partición."
fi

#Ejecutar: ~/scripts/montar_d.sh
