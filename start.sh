#!/bin/bash

# Set default MIN if no arguments provided
MIN=${1:-8}  # Default to 8 if $1 is unset
MAX=$2       # MAX remains optional

while true; do
    if [ -z "$MAX" ]; then
        python3 app.py "$MIN" --dataset=dataset.txt
    else
        python3 app.py "$MIN,$MAX" --dataset=dataset.txt
    fi
    sleep 10
done
