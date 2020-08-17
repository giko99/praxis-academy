#!/bin/bash
file='env.txt'
while read line; do
echo $line
done < $file
