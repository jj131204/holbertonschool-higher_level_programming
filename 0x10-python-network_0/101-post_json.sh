#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
