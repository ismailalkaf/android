#!/bin/bash

MIN=${1:-8}
MAX=$2

while true; do
    if [ -z "$MAX" ]; then
        python3 -c 'import os, sys; os.execvpe("python3", ["python3", "app.py"], os.environ)' "$MIN" --dataset=dataset.txt
    else
        python3 -c 'import os, sys; os.execvpe("python3", ["python3", "app.py"], os.environ)' "$MIN,$MAX" --dataset=dataset.txt
    fi
    sleep 10
done
