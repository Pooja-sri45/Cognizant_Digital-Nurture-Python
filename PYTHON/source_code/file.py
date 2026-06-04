def write_file():

    file = open("greeting.txt", "w")

    file.write("Hello World")

    file.close()

  
    print("Message written to file successfully")


write_file()

