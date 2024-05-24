#!/bin/bash
# Get the byte size of the HTTP response header for the given URL.
# curl -s "$1" | wc -c
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2