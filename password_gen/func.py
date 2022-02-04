import secrets
import string
import os

passes_directory = "Passes_directory_created_by_pass_gen_for_the_purpose_of_passcodes_saving"

default_path = "C:\\Users\\admin\\Passes_directory_created_by_pass_gen_for_the_purpose_of_passcodes_saving"

def initial_setup():
    # directory = passes_directory   
    address = "C:\\Users\\admin"    
    path = os.path.join(address, passes_directory)
    try: 
        os.mkdir(path) 
    except OSError as error: 
      pass
    print("//you might consider to hide folder of passes via cmd// \n")

    
    
def generator():
    length = int(input('Enter the length of password: '))                      

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    global password
    password = ''.join(secrets.choice(all) for i in range(length))



def default_save():
    purpose = (input("what this is for:"))
    filename = default_path + ("\\" + purpose + " password" +".txt")
    write =open(filename, "w")
    write.write(password + " \nis passcode for " + purpose) # ignore the error
    write.close()

def save():   
    purpose = (input("what this is for:"))
    filename = location + "\\" + purpose + " password" +".txt"# ignore the error
    write =open(filename, "w")
    write.write(password + " \nis passcode for " + purpose) # ignore the error
    write.close()

def exit_message():
    print("saved!")

def open_file(): # Change this formula
    address = ( default_path + "\\")
    global file_name

    path="C:\\Users\\admin\\Passes_directory_created_by_pass_gen_for_the_purpose_of_passcodes_saving"

    list = []

    for (root, dirs, txt_file_name) in os.walk(path):
        for txt_file in txt_file_name:
            if '.txt' in txt_file:
                print(txt_file)

    file_name = input("please search for your file and type the name only - ")
    file =  address + file_name + " password.txt"
    content = open(file, 'r')
    print(content.readline())

def purge():
    import shutil
    shutil.rmtree(default_path)