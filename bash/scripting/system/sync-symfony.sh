#!/bin/bash

# Ruta de origen (Symfony en Linux, donde Apache2 apunta)
SRC="/home/anthony/server/php/symfony/"

# Ruta de destino (carpeta del repo LearnFW)
DEST="/media/anthony/Elena/program/practic/github/LearnFW/Symfony/projects/small_projects/"

echo "🔄 Syncing Symfony projects from:"
echo "   $SRC"
echo "   to:"
echo "   $DEST"
echo

# Ejecuta la sincronización, excluyendo carpetas .git para evitar conflictos
rsync -av --delete --exclude='.git' --exclude='vendor' "$SRC" "$DEST"

echo
echo "✅ Sync complete!"

# para ejecutar ~/scripts/sync-symfony.sh

