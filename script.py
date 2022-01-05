import sys
from markdown import markdown

HTML_HEAD = '''

<head>
    <meta charset="utf-8">
    <title>File</title>
</head>

'''


def main():
    file_path=sys.argv[1]
    output_path=sys.argv[2]

    file = open(file_path, 'r')
    
    text = file.read()

    markdown_string = markdown(
        text,
        extensions=['codehilite', 'extra', 'fenced_code']
    )


    html_final_string = f'''
<html>
        {HTML_HEAD}
<body>
        {markdown_string}
</body>
</html>
    '''
    
    output_file = open(output_path, 'w')
    
    output_file.write(html_final_string)



if __name__ == '__main__':
    main()

