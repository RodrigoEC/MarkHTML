#!/bin/bash

MarkHTML() {
	if [ -e $1 ]
	then
		if [ -z $2 ]
		then
			local output_path=$(echo $1 | awk -F/ '{
			for (x=1; x<=NF-1; x++) {
					if (x == NF-1) {
						printf("%s/output.html", $x)
					} else {
						printf("%s/", $x)
					}
				}
			}')
		else
			local output_path=$2
		fi

		echo "Saída: $output_path"
		exec python3 script.py $1 $output_path $3
		

	else
		echo "File path passed is not valid"
	fi
	
}

MarkHTML $1 $2 $3
