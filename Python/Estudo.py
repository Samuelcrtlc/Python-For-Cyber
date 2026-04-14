username = input("enter a username: ")


if len(username) > 12:
    print("username is not valid")
elif not username.find(" ") == -1:
    print("username is not valid, because of the spaces")
elif not username.isalpha():
    print("username is not valid, because it contains special characters, or numbers")
else:
    print(f"Welcome, {username}!")