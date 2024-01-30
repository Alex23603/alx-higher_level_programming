#!/bin/bash
# bash Sends a JSON POST request to the URL with the JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
