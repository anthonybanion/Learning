#!/bin/bash

REPO="anthonybanion/LearnFW"  # <-- Cambiá esto por tu repo

jq -c '.[]' label.json | while read -r label; do
  NAME=$(echo "$label" | jq -r '.name')
  COLOR=$(echo "$label" | jq -r '.color')
  DESCRIPTION=$(echo "$label" | jq -r '.description')

  echo "Creando o actualizando etiqueta: $NAME"
  # Intentar crear primero, si ya existe, se edita
  gh api repos/$REPO/labels \
    -f name="$NAME" \
    -f color="$COLOR" \
    -f description="$DESCRIPTION" \
    --silent || \
  gh api repos/$REPO/labels/"$NAME" \
    -X PATCH \
    -f new_name="$NAME" \
    -f color="$COLOR" \
    -f description="$DESCRIPTION"
done

echo "Etiquetas importadas correctamente."

