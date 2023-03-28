import os

def cwd():
    path = os.getcwd() #gets current directory
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):#gets list of content for current directory
        print(file)

def run():
    print("Processing...")
    cwd()

run()
