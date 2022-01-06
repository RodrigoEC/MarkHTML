#!/bin/bash

# $1 - file_path: Where the markdown file is (required)
# $2 - output_path: Where the html file is going to be saved (not-required)
# $3 - html_title: The title of the html file that's going to be created (not-required)


findExtension() {
	return $extension
}

MarkHTML() {
	if [[ -e $1 && ! -d $1 ]]
	then
		local file_extension=$(echo $1 | awk -F. '{ print $2 }')

		if [ $file_extension != "md" ]
		then
			echo "Invalid file format, .md extension required"
			exit 2
		fi
			
		if [ ! -z $2 ]
		then 
			local output_path=$2
		fi

		if [ -z $4 ]
		then
			local css_path="./style.css"
		else
			local css_path=$4
		fi


 		exec python3 script.py $1 $output_path $3 $4
		

	else
		echo "File path given is not valid"
		exit 2
	fi
	
}

MarkHTML $1 $2 $3 $4 $5
