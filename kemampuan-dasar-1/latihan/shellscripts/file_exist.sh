#!/bin/bash
filename=$1
if [ -f "$filename" ]; then
echo "File exists"
else
echo "file does not ecist"
fi

