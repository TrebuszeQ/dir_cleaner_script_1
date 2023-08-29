import os
import shutil

# Creates CleanedUp folder and copies content of the Desktop to it. Hopefully this remains within SOLID principles.

# create directory CleanedUp or drop an Exception.
def create_dir(destination):
    path = os.path.join(destination, "CleanedUp")
    try:
        os.mkdir(path)
        print("File has been created.\n\n")
    except FileExistsError:
        print("Directory couldn't been made, file exists.\n\n")
    except Exception as err:
        print("Directory couldn't been made.\n\n")
        raise err
    return path


# Check if desktop exists.
def desktop_exists(desktop_path) -> bool:
    if not os.path.exists(desktop_path):
        return False
    return True


#return path to desktop
def ret_desktop_path():
    user_path = os.path.expanduser("~")
    desktop_p = os.path.join(user_path, "Desktop")
    return desktop_p
    

# list directory (desktop) content
def list_dir_content(dir_content):
    for obj in dir_content:
        print(obj)
    return True


# return content of desktop directory or drop an Exception.
def ret_desktop_content(desktop, home):
    if not home:

        try:
            content = os.listdir(desktop)
            return content
        except FileNotFoundError:
            print(f"{desktop} doesn't exist.\n\n")
        except FileExistsError:
            print(f"Cannot access {desktop}.\n\n")
        except Exception("Unknown exception when accessing the desktop\n\n") as e:
            raise e

    elif type(home) == str:
        try:
            content = os.listdir(desktop)
            return content
        except FileNotFoundError:
            print(f"{desktop} doesn't exist.\n\n")
        except FileExistsError:
            print(f"Cannot access {desktop}.\n\n")
        except Exception as e:
            print("Unknown exception when accessing the desktop\n\n")
            raise e
    return False


# Creates subfolders based on folders dictionary.
def create_subdirs(folders): 
    for dir in folders:
        print(dir)
        # here
    return False


# Copy content of desktop to CleanedUp
def cp_content(src, dest, dir_content):
    try:
        for obj in dir_content:
            src = os.path.join(src, obj)
            shutil.copyfile(src, dest)
            print(f"{obj} copied to {dest}.\n")
    except Exception as e:
        print("Unknown exception encountered.\n\n")
        raise e
    

def main():
    # Make the folder CleanedUp/
    cleanedup = ""
    destination = input("Where do you want to create CleanedUp folder.\n")

    folders = {
        "Images": [".jpeg", ".jpg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".xlsx"],
        "Archives": [".zip", ".rar", ".tar", ".7z", ".tar.gz"],
        "Shortcuts": [".lnk"]
    }

    # Return desktop path
    desktop_path = ret_desktop_path()
    # Check if desktop exists
    path_exist: bool = desktop_exists(desktop_path)
    if not path_exist:
        print("Path doesn't exist.\n")
        raise Exception(FileNotFoundError)
    elif path_exist:
        cleanedup = create_dir(destination)
    
    
    # List the files in the desktop/ folder
    content = ret_desktop_content(desktop_path)
    list_dir_content(content)
    
    # Creates subfolders based on folders dictionary.
    create_subdirs(folders)
    # For each file in the Desktop/ folder copy the file to the CleanedUp/ folder
    cp_content(desktop_path, destination, content)


main()