#!/usr/bin/env bash
set -euo pipefail

function main {
  trap 'true' SIGINT SIGTERM

  start-app &
  start-proxy &

  wait -n || true
  kill -s SIGINT -1
  wait
}

function start-app {
  export PYTHONPATH="/app/src"
  exec /app/.venv/bin/python -m gunicorn \
    venue_site.wsgi:application \
    --bind=0.0.0.0:81 \
    --workers "${VENUE_WORKERS:-1}"
}

function start-proxy {
  exec caddy run --config /proxy/Caddyfile
}

main "$@"
