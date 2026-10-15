#!/usr/bin/env sh
set -eu

root=${1:-"$(pwd)"}
cd "$root"

printf '%s\n' '{'
printf '%s\n' '  "checks": ['
printf '%s\n' '    {"check":"env-ignore","status":"'"$(grep -q '^\.env\*' .gitignore 2>/dev/null && printf ok || printf unverified)'"'"},'
if command -v docker >/dev/null 2>&1 && [ -f docker-compose.yml ]; then
  docker compose config --quiet >/dev/null && compose_status=ok || compose_status=unverified
else
  compose_status=not-applicable
fi
printf '%s\n' '    {"check":"docker-compose","status":"'"$compose_status"'"}'
printf '%s\n' '  ]'
printf '%s\n' '}'
