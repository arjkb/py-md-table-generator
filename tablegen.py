def main():
    with open('input.txt') as f:
        for i, line in enumerate(f, 1):
            title, link, auth = line.split('|')

            print(i)
            print(title.strip())
            print(link.strip())
            print(auth.strip())

if __name__ == '__main__':
    main()
