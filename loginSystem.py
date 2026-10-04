print("1. Login")
print("2. Create Account")
print("3. Exit")
choice =int(input("Enter your choice: "))
if choice == 1:
    a=input("Enter username: ")
    b=input("Enter your password: ")
    print("You've Logged in!")
    c = int(input("Press '3' to exit"))
    print(c)
    if c == 3:
        print("Exiting...")
        exit()
elif choice == 2:
    username = input("Create Username: ")
    password = input("Create Password: ")
    print("Account Created Successfully!")
    exit = int(input("Press '3' to exit: "))
    if exit == 3:
        print("Exiting...")
        exit()
elif choice == 3:
    print("Exiting...")
    exit()
else:
    print("Invalid choice")