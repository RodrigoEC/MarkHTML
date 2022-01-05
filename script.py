import sys
from markdown import markdownFromFile

def main():
    file_path=sys.argv[1]
    output_path=sys.argv[2]
    print(file_path)
    print(output_path)


    markdown_string = markdownFromFile(
        input=file_path,
        output=output_path,
        encoding='utf8',
        extensions=['codehilite', 'extra', 'fenced_code']
    )



if __name__ == '__main__':
    main()

