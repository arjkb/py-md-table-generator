import argparse

from string import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="path to input file")
    args = parser.parse_args()

    t = Template("|$sno|[$title]($link){:target='_blank'}|$author|")

    with open(args.file) as f:
        for i, line in enumerate(f, 1):
            title, auth, link = line.split('|')

            s = t.substitute(sno=i,
                            title=title.strip(),
                            link=link.strip(),
                            author=auth.strip() )
            print(s)

if __name__ == '__main__':
    main()
