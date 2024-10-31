#!/bin/bash

URL="http://web:8000/"
RETRY_INTERVAL=5  # Time in seconds between each check

echo "Checking server availability at $URL..."

while true; do
    # Check if the server is reachable (ignore response code)
    if curl --output /dev/null --silent --head "$URL"; then
        echo "Server is up and responding."
        exit 0  # Exit the script successfully
    else
        # echo "Server is not available. Retrying in $RETRY_INTERVAL seconds..."
        sleep $RETRY_INTERVAL  # Wait before checking again
    fi
done
