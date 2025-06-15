#!/bin/bash

REPO="anthonybanion/LearnFW"  # <-- Cambiá esto por tu repo

jq -c '.[]' milestones.json | while read -r milestone; do
  TITLE=$(echo "$milestone" | jq -r '.title')
  DESC=$(echo "$milestone" | jq -r '.description')
  DUE=$(echo "$milestone" | jq -r '.due_on')

  echo "Creando milestone: $TITLE"
  gh api repos/$REPO/milestones \
    -f title="$TITLE" \
    -f description="$DESC" \
    -f due_on="$DUE"
done
echo "Milestones importados correctamente."