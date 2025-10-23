#!/bin/bash

echo "⏳ Iniciando importación completa..."

# Verificar si los scripts existen
if [[ ! -f import_labels.sh ]]; then
  echo "❌ Falta el archivo import_labels.sh"
  exit 1
fi

if [[ ! -f import_milestones.sh ]]; then
  echo "❌ Falta el archivo import_milestones.sh"
  exit 1
fi

if [[ ! -f import_issues.sh ]]; then
  echo "❌ Falta el archivo import_issues.sh"
  exit 1
fi

# Ejecutar cada uno
echo "📌 Importando etiquetas..."
bash import_labels.sh

echo "📅 Importando hitos (milestones)..."
bash import_milestones.sh

echo "📝 Importando issues..."
bash import_issues.sh

echo "✅ ¡Importación completa de labels, milestones e issues!"
echo "🚀 ¡Listo para usar tu repositorio!"