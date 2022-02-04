import secrets
import string
from func import *


initial_setup()

while quit != "q":

    menu = input("\n select operation:\n" + "1. new\n" + "2. open\n"+ "3. purge\n ")

    if(menu == "new"):
        generator()
        location = input('Where to save (path):')   
        if (location == "default"): # ignore the error
            default_save()
            exit_message()   
        else:
            print("//WARNING//-This a user defined location and program will not guarantee these Passes.")
            save()
            exit_message()
    elif(menu == "open"):
        open_file()
        exit_message()
    elif(menu == "purge"):
        print("//WARNING// Your all saved Passes are going to delete.")
        response = input("\n(y or n)- ")
        if (response == "y" or "yes"):
            purge()
            print("Task completed!")
    else:
        print("invalid response\n")
    quit = input("Type q to quit.")