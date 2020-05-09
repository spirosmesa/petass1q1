#! /bin/bash

outputCount=$( (ls ./$1 | grep entry > out.txt) && (wc -l out.txt | grep -Eo '[[:digit:]]{4}') )

for i in $(seq 1 60); do
	echo "entry message count $i: " $(wc -l ./$1/entry$i.txt)
	echo "exit message count $i: " $(wc -l ./$1/exit$i.txt)
	echo ""
done
