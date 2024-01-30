#!/bin/bash
# bash Sends a GET request 2 a url n disply the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
