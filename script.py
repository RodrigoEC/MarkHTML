import sys
from markdown import markdown
from markdown.extensions.toc import TocExtension

def main():
    file_path=sys.argv[1]
    output_path=sys.argv[2]

    title = 'HTML file'
    css_path = './style.css'

    if (len(sys.argv) > 3): title = sys.argv[3]
    if (len(sys.argv) > 4): css_path = sys.argv[4]

    HTML_HEAD = f'''

    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href={css_path}>
    </head>

    '''


    file = open(file_path, 'r')
    
    text = file.read()

    markdown_string = markdown(
        text,
        output_format='html5',
        extensions=['codehilite', 'extra', 'fenced_code', TocExtension(baselevel=1)]

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

