#!/bin/bash

# wait-for-it.sh
# Script to wait until a service (like MySQL) is ready to accept connections
TIMEOUT=500
INTERVAL=10
HOST=$1
PORT=$2
shift 2
CMD=$@

# echo "Host is: $HOST"
# echo "Port is: $PORT"

# Function to check if the service is up
wait_for_service() {
    timeout=$TIMEOUT
    while ! nc -z $HOST $PORT; do
        timeout=$((timeout - INTERVAL))
        if [ $timeout -le 0 ]; then
            echo "Service $HOST:$PORT not available after waiting for $TIMEOUT seconds"
            exit 1
        fi
        echo "Waiting for $HOST:$PORT to be ready..."
        sleep $INTERVAL
    done
}

# Wait for the service to be ready
wait_for_service

# Run the command after the service is ready
echo "$HOST:$PORT is ready, running command: $CMD"
exec $CMD