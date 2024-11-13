#!/bin/bash
#Skript creates a new folder TXT and moves all txt files within home directory there and outputs the number moved
mkdir "TXT"
count=0
for i in $HOME/*.txt; do
    mv "$i" "TXT/"      
    count=$((count + 1))
done

echo "$count txt files moved"