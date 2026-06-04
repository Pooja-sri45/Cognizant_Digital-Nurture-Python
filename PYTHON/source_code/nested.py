def login(user, pwd):

    if user == "" or pwd == "":
        print("Username or Password cannot be empty")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Incorrect Password")
    else:
        print("Invalid Username")


user = "admin"
pwd = "pass123"
login(user, pwd)

