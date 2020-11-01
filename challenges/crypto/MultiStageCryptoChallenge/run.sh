#!/bin/bash
set -euo pipefail

WORKERS=${WORKERS:-1}
WORKER_CLASS=${WORKER_CLASS:-gevent}
ACCESS_LOG=${ACCESS_LOG:--}
ERROR_LOG=${ERROR_LOG:--}
WORKER_TIMEOUT=${WORKER_TIMEOUT:-60}
WORKER_PORT=${WORKER_PORT:-1337}

# Start app
echo "Starting App"
exec gunicorn 'main:app' \
    --bind "0.0.0.0:$WORKER_PORT" \
    --workers $WORKERS \
    --timeout $WORKER_TIMEOUT \
    --worker-class "$WORKER_CLASS" \
    --access-logfile "$ACCESS_LOG" \
    --error-logfile "$ERROR_LOG"