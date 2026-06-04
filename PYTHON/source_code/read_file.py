
def read_file():

    try:
        file = open("greeting.txt", "r")

        content = file.read()

        print("File Content:", content)

        file.close()

    except FileNotFoundError:
        print("File not found")


read_file()