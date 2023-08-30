import os
import shutil

# Creates CleanedUp folder and copies content of the Desktop to it. Hopefully this remains within SOLID principles.


# create directory CleanedUp or drop an Exception.
def create_dir(destination, dir_name):
    path = os.path.join(destination, dir_name)
    try:
        os.mkdir(path)
        print(f"Directory {dir_name} has been created.")
    except FileExistsError:
        print(f"Directory {dir_name} already exists.")
    except Exception as e:
        print(f"Directory {dir_name} couldn't been made.")
        raise e
    print()
    return path


# Check if desktop exists.
def desktop_exists(desktop_path) -> bool:
    if not os.path.exists(desktop_path):
        return False
    return True


# return path to desktop
def ret_desktop_path():
    user_path = os.path.expanduser("~")
    desktop_p = os.path.join(user_path, "Desktop")
    return desktop_p
    

# list directory (desktop) content
def list_dir_content(dir_content):
    print("Content of the desktop:\n")
    for obj in dir_content:
        print(obj)
    return True


# return content of desktop directory or drop an Exception.
def ret_desktop_content(desktop):
    try:
        content = os.listdir(desktop)
        return content
    except FileNotFoundError:
        print(f"{desktop} doesn't exist.\n")
    except FileExistsError:
        print(f"Cannot access {desktop}.\n")
    except Exception("Unknown exception when accessing the desktop\n") as e:
        raise e
    return False


# Creates subfolders based on folders dictionary.
def create_subdirs(folders, dst):
    for obj in folders:
        path = create_dir(dst, obj)
        if type(path) != str:
            return False
        # here
    return True


# Copy content of desktop to CleanedUp
def cp_content(src, dest, dir_content):
    tmp = src
    try:
        for obj in dir_content:
            src = tmp
            src = os.path.join(src, obj)
            shutil.copy(src, dest)
            print(f"{obj} copied to {dest}.")
    except Exception as e:
        print("Copied failed.\n")
        raise e
    print("Copied successfully.\n")
    

def main():
    # Make the folder CleanedUp/
    term_msg = "Program is terminating"
    destination = input("Where do you want to create CleanedUp folder.\n")
    cleanedup = create_dir(destination, "CleanedUp")
    if type(cleanedup) != str:
        print(term_msg)
        return False

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

    # Return desktop content
    content = ret_desktop_content(desktop_path)
    # List the files in the desktop/ folder
    list_dir_content(content)
    
    # Creates subfolders based on folders dictionary.
    if not create_subdirs(folders, cleanedup):
        print(term_msg)
        return False

    # For each file in the Desktop/ folder copy the file to the CleanedUp/ folder
    cp_content(desktop_path, cleanedup, content)


main()