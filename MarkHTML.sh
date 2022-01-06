#!/bin/bash

MarkHTML() {
	if [ -e $1 ]
	then
		local base_path=$(echo $1 | awk -F/ '{
			for (x=2; x<=NF-1; x++) {
						printf("/%s", $x)
						
			}}')
		echo $base_path
		if [ -z $2 ]
		then
			local output_path="$base_path/output.html"

		else
			local output_path=$2
		fi

		echo "Saída: $output_path"
		exec python3 script.py $1 $output_path $3
		cp "$(pwd)/style.css" $base_path/templates
		

	else
		echo "File path passed is not valid"
	fi
	
}

MarkHTML $1 $2 $3
