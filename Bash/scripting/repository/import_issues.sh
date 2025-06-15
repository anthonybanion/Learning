#!/bin/bash

REPO="anthonybanion/LearnFW"  # ← Cambiá por el tuyo

jq -c '.[]' issues.json | while read -r issue; do
  title=$(echo "$issue" | jq -r '.title')
  body=$(echo "$issue" | jq -r '.body')
  labels=$(echo "$issue" | jq -r '.labels | join(",")')

  echo "Creando issue: $title"
  gh issue create --repo "$REPO" --title "$title" --body "$body" --label "$labels"
done
echo "Issues importados correctamente."
# Asegúrate de tener el archivo issues.json en el mismo directorio que este script.
# Puedes ejecutar el script con:
# chmod +x import_issues.sh
# ./import_issues.sh