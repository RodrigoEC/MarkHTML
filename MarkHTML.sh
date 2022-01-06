#!/bin/bash

MarkHTML() {
	if [ -e $1 ]
	then
		local base_path=$(echo $1 | awk -F/ '{
			for (x=2; x<=NF-1; x++) {
						printf("/%s", $x)
						
			}}')
		echo $2
		if [ -z $2 ]
		then
			local output_path="$base_path/output.html"
			cp "$(pwd)/style.css" $base_path

		else
			local output_path=$2
			local css_path=$(echo $output_path | awk -F/ '{
			for (x=2; x<=NF-1; x++) {
						printf("/%s", $x)
						
			}}')
			cp "$(pwd)/style.css" $css_path
		fi

		exec python3 script.py $1 $output_path $3
		

	else
		echo "File path passed is not valid"
	fi
	
}

MarkHTML $1 $2 $3
