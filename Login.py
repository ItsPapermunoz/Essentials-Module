# Module imports

import pickle
import IEM as iem

# Variable Definitions

__author__ = "Rodrigo 'ItsPaper' Muñoz"
__version__ = "Alpha"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
clear = iem.cls
pause = iem.pause

# Class Definitions


class User:
    def __init__(self, username, password):
        username = self.username
        password = self.password


    def authentication(self):
        clear()
        attempts = 0
        while attempts < 10:
            if attempts > 0:
                print("Password attempts: {} (10 max)".format(attempts))
            try:
                password_attempt = input("Please enter password...")
            except:
                password_attempt = input("Please enter valid password...")
            if password_attempt == self.password:
                print("Authentication succesfull!")
                pause()
                return True
            else:
                attempts += 1
        print("Authentication failed!")
        return False


# Function Definitions

def read_users():
    try:
        user_list = pickle.load(open("Users.data", "rb"))
    except FileNotFoundError:
        print("No previous user detected, creating new user file...")
        user_list = []
        pickle.dump(user_list, open("Users.data", "wb"))
    finally:
        return user_list

def login():
    clear()
    user = input("Please enter username... ")
    for username in user_list:
        if user == username.username:
            print("User Found!")
            pause()
            authentication = username.authentication()
            if authentication:
                return username.username
            else:
                print("Login unsuccesful...")
                pause()
                return False
    print("User not found please try again!")
    pause()


def new_user():
    clear()
    user = input("Please enter your new username!")
    password = input("Please enter your new password!")
    new_user = User(user, password)
    user_list.append(new_user)
    pickle.dump(user_list, open("Users.data", "wb"))
    print("New User Created and stored!")
    pause()


def del_user():
    clear()
    i = 0
    user_selection = input("Enter username to delete... ")
    for user in user_list:
        if user_selection == user.username:
            print("User found")
            confirmation = iem.confirm()
            if confirmation:
                user_list.remove(user_list[i])
        i += 1

# Main Code
read_users()
new_user()
login()
