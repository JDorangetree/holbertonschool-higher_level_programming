#!/bin/bash
#displays only the status code of the response.
curl -s -w "%{http_code}" -o /tmp/null "$1"
