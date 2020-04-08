#!/bin/bash
#sends a request to that URL, and displays the size of the body of the response
curl --head -s "$1" | grep "Content-Length" | awk '{print $2}'
