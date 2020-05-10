#! /bin/bash

outputCount=$( (ls ./$1 | grep entry > out.txt) && (wc -l out.txt | grep -Eo '[[:digit:]]{4}') )

for i in $(seq 1 100); do
	entry=$(wc -l ./$1/entry$i.txt | sed 's/\s.*$//') 
	exite=$(wc -l ./$1/exit$i.txt | sed 's/\s.*$//')
	echo "entry message count $i: "  "$(($entry-1))" 
	#echo "entry log is:"
	#cat ./$1/entry$i.txt
	echo ""
	echo "exit message count $i: " "$(($exite-1))" 
	echo "exit log is:"
	cat ./$1/exit$i.txt
	echo ""
	echo ""
done
