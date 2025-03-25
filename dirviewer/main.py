# DirViewer
import os, time

def dirData():
    holder = os.listdir()
    return holder # Returns the data in {holder} to {data}

print("Initializing...")
time.sleep(3)
print("Successful!")

while True:
    dirswitch = input("Dir Name to switch >> ")
    try:
        os.chdir(dirswitch) # Switches the directory based on the user's input in {dirswitch}
        currentDir = os.getcwd() # Gets the current working Directory
        print(f"You are in {currentDir}")
        time.sleep(1)
        print("Getting files...")
        data = dirData()
        time.sleep(7)
        print("Getting folders...")
        time.sleep(2)
        print(f"Directory List: {data}") # Displays the files and folders in the dir.
    except FileNotFoundError:
        print("Directory doesn't exist!")
