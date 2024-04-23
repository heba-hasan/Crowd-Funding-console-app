import handling_user as hs


# userid=""
# wrongpass=0


def empty(word):
    if word.strip() and word.isalpha():
        return True

    else:
        print("filed should not be empty")
        return False
    pass


if __name__ == '__main__':
    while True:

        option = input("select from this menu:\n1-login\n2-Register\n3-Exit\n")
        if option == '1':
            hs.login()
        elif option == '2':
           hs.register()
        elif option == '3':
            exit()
        else:
            print("your option invalid")
