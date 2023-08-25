import os

def main():

    #Make the folder CleanedUp/
    destination = input("Where you want to create CleanedUp folder.\n")
    access_modes = [
        os.F_OK,
        os.R_OK,
        os.W_OK,
        os.X_OK
    ]
    if not os.access(destination, access_modes[0]):
        print("Path doesn't exist.")
        return FileNotFoundError
    else:
        os.mkdir()
        return
    #List the files in the Desktop/ folder
    #For each file in the Desktop/ folder move the file to the CleanedUp/ folder


main()