import toOpenAppPass


passAsking = input("what is the password to use PASSWORD MANAGER? ")

if passAsking == toOpenAppPass.password:
    pass
elif passAsking != toOpenAppPass.password:
    print("Invalid Password! You have to choose the correct password to use PASSWORD MANAGER!")

def view_pass():
    with open("passwords.txt", 'r') as f:
        for lines in f.readlines():
            print("\n", lines.rstrip())


def store_pass():
    userName = input("Enter your user name: ")
    password = input("Enter your password: ")

    with open("passwords.txt", 'a') as f:
        fileContent = f"User Name - {userName}\nPassword - {password}\n\n"
        f.write(fileContent)


while True:
    askingMode = input("Say which type of mode you want to use? (view/store) and q to quit: ").lower()

    if askingMode == "view".lower():
        view_pass()
    elif askingMode == "store".lower():
        store_pass()
    elif askingMode == "q".lower():
        quit()
    else:
        print("Invalid choice given by the user!")
        quit()
