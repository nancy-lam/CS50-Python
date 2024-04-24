def main():
    text = input('Enter text: ')
    print(convert(text))


def convert(text):
    faces = text.replace(':)', '🙂').replace(':(', '🙁')
    return faces

main()
