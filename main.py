import pickle

# Create a dictionary to store usernames and passwords

users = {}

company={}

# Function to save the user dictionary to a binary file

def save_users():

    with open("users.bin", "wb") as f:

        pickle.dump(users, f)


# Function to load the user dictionary from the binary file

def load_users():

    try:

        with open("users.bin", "rb") as f:

            return pickle.load(f)

    except FileNotFoundError:

        return {}


# Load the existing users from the binary file

users = load_users()


def save_company():

    with open("company.bin", "wb") as f:

        pickle.dump(company,f)


def load_company():

    try:

        with open("company.bin", "rb") as f:

            return pickle.load(f)

    except FileNotFoundError:

        return {}


company=load_company()


def upload():

    with open("web.bin", "wb") as f:

        pickle.dump(company[filename], f)


def scan():

    






def main_menu():

    print("Main Menu:")

    print("1. Sign-in")

    print("2. Login")

    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        username = input("Enter your username: ")


        if username not in users:

            password = input("Enter your password: ")

            users[username] = password

            save_users()

            print("User created!")

        else:

            print('User already exists')

    elif choice == 2:

        username = input("Enter your username: ")


        if username in users:

            password = input("Enter your password: ")

            # If the username exists, check if the password matches

            if users[username] == password:

                print("Login successful!")

                submenu()

            else:

                print("Incorrect password")

        else:

            print('User does not exist')

    elif choice == 3:

        exit()

    else:

        print("Invalid choice.")

        main_menu()




def submenu2():

    print("Submenu 2:")

    print("1. mail")

    print("2. create")

    print("3. open")

    print("4. Back to previuos menu")


    choice = int(input("Enter your choice: "))


    if choice == 1:

        print("mail")

        

    elif choice == 2:

        print("create")

        filename = input("Enter your filename: ")


        if filename not in company:

            data = input("Enter your data: ")

            company[filename] = data

            save_comapny()

            print("File created!")

        else:

            print('Filename already exists')


    elif choice == 3:

        print('open')

        for key in company.keys():

            print(key)

        filename=input('enter filename to open')

        print(company[filename])

        reply=input('Do you want to upload it to the web, reply with yes or no')

        if reply=='yes':

            upload()

        elif reply=='no':

            #exit to list of files

        else:

            print('you have entered incorrect option')


    elif choice==4:

        main_menu()

    else:

        print("Invalid choice.")

        submenu2()

main_menu()
