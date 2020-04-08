#!/bin/bash
#script that sends a JSON POST request to a URL
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98"
