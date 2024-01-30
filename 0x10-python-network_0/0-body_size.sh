#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request and display the size of the response body in bytes
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')
echo "Size of the response body: $response_size bytes"
