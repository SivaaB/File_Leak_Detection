import pickle
from time import sleep
from random import random
from threading import Thread  
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

# Function to save the company dictionary to a binary file
def save_company():
    with open("company.bin", "wb") as f:
        pickle.dump(company,f)

def load_company():
    try:
        with open("company.bin", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def upload():
    with open("web.bin", "wb") as f:
        pickle.dump(web, f)

def load_web():
    try:
        with open("web.bin", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

web={}
web=load_web()  #this becomes satatype string instead of dict -->issue fixed
# Load the existing users from the binary file
users = load_users()
company=load_company()

def save_mail(usera,subject,data):

    globals()[usera] = {}
    a=globals()[usera]
    a[subject]=data
    print(type(a))
    with open(usera,"wb") as f:
        pickle.dump(a,f)

def load_mail(user):
    a=globals()[user]
    try:
        with open(user,"rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def view_mail(user):
    a=load_mail(user)
    for key in a:
        print(key)
    subject=input('enter name of mail to open')
    print(a[subject])

#submenu3
def submenu3():
    while True:
        print("Submenu 3:")
        print("1. send mail")
        print("2. recieve mail")
        print("3. quit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            print('send mail')
            print('select the user you want to send the mail to')
            for keys in users:
                print(keys)
            usera = input("Enter a username ")
            subject=input('enter the subject')
            data=input("enter your data ")
            save_mail(usera,subject,data)
        elif choice==2:
            print('recieve mail')
            user=input('enter your username')
            view_mail(user)
        elif choice==3:
            break
        else:
            print("Invalid choice")

#submenu2
def submenu2():
    while True:
        print("Submenu 2:")
        print("1. mail")
        print("2. create")
        print("3. open")
        print("4. Back to previuos menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            submenu3()
        elif choice == 2:
            print("create")
            filename = input("Enter your filename: ")
            if filename not in company:
                data = input("Enter your data: ")
                company[filename] = data
                save_company()
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
                web[filename]=company[filename]
                upload()
                sleep(1)
            elif reply=='no':
                break
                #exit to list of files
            else:
                print('you have entered incorrect option')
        elif choice==4:
            main_menu()
        else:
            print("Invalid choice.")

#main menu
def main_menu():
    while True:
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
                with open (username,"w") as f:
                    f.close()
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
                    submenu2()
                else:
                    print("Incorrect password")
            else:
                print('User does not exist')
        elif choice == 3:
            exit()
        else:
            print("Invalid choice.")

def background_task():
    global company
    global web
    while True:
        for key in company.keys():
            for sub in web.copy():
                if key==sub:
                    usera = 'admin'
                    subject='leak detected'
                    data="there has been a leak of foldername:",key," and has been dealt with"
                    print("leak detected")
                    del web[key]
                    save_mail(usera,subject,data)
        sleep(0.1)

daemon = Thread(target=background_task, daemon=True)
daemon.start()

'''for key in company.keys():
    print(key)
print(type(company))
print(type(users))

print('----------------------------')
print(type(web))
for key in web.keys():
    print(key)
'''

main=Thread(target=main_menu,daemon=False)
main.start()
