# not recommend for real-world work

from cryptography.fernet import Fernet


#in order to make the master_password to incript all password
#we must type "pip install cryptography" in the terminal first

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key() '''
#only need to use the write_key() once, then we must make it comment

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            #rstrip() will not read the new line code
            user, passw = data.split("|")
            #split() will break string into list based on the string inside its bracket, in this case "|"
            #we use only user, passw because we know that after the split, our list will contain only two values
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # it is better to use "with" to open file because it will close the file automatically

    # "w" mode will overwrite the file when you open it (delete what exist and write new one)
    # "r" mode can only read mode
    # "a" mode will add something to the end of a file and can read the file, or it will create new file of there is no file exists
    with open("password.txt", "w") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)?, press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

