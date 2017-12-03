from string import Template

def main():
    t = Template("|$sno|[$title]($link){:target='_blank'}|$author|")

    with open('input.txt') as f:
        for i, line in enumerate(f, 1):
            title, auth, link = line.split('|')

            s = t.substitute(sno=i,
                            title=title.strip(),
                            link=link.strip(),
                            author=auth.strip() )
            print(s)

if __name__ == '__main__':
    main()
