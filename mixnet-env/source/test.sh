#! /bin/bash

out=$((ls ./logs | grep entry > out.txt) && (wc -l out.txt | grep -Eo '[[:digit:]]{2}' | tr -d "\n"))

echo $out
