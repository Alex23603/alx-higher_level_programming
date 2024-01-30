#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request, get the body size, and display it in bytes
response_size=$(curl -s "$url" | wc -c)
echo "$response_size"
