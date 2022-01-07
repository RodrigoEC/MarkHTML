import sys
from markdown import markdown
from markdown.extensions.toc import TocExtension
from jinja2 import FileSystemLoader, Environment
from bs4 import BeautifulSoup

def parse_markdown(file_path):
    file = open(file_path, 'r')
    
    text = file.read()

    return markdown(
        text,
        output_format='html5',
        extensions=['codehilite', 'extra', 'fenced_code', TocExtension(baselevel=1)]
    )

def create_html(title, css_path, html):
    loader = FileSystemLoader('.')
    env = Environment(loader=loader)
    template = env.get_template('base.html')

    parsed_html = template.render(
        title=title,
        css_path=css_path,
        parsed_html=html
    )

    soup = BeautifulSoup(parsed_html, features="html.parser")

    return soup.prettify()

def main():
    file_path=sys.argv[1]
    output_path=sys.argv[2]

    title = 'HTML file'
    css_path = './style.css'

    if (len(sys.argv) > 3): title = sys.argv[3]
    if (len(sys.argv) > 4): css_path = sys.argv[4]

    parsed_html = parse_markdown(file_path)
    
    final_html = create_html(title, css_path, parsed_html)

    output_file = open(output_path, 'w')
    output_file.write(final_html)
    output_file.close()


if __name__ == '__main__':
    main()

