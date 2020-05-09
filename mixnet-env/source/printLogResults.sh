#! /bin/bash

outputCount=$( (ls ./logs | grep entry > out.txt) && (wc -l out.txt | grep -Eo '[[:digit:]]{4}') )

for i in $(seq 1 20); do
	echo "entry message count $i: " $(wc -l ./logs/entry$i.txt)
	echo "exit message count $i: " $(wc -l ./logs/exit$i.txt)
	echo ""
done
