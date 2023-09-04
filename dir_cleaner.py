import os
import shutil
import pathlib

# Creates CleanedUp folder and copies content of the Desktop to it. Hopefully this remains within SOLID principles.


# Ask user about action that will be performed.
def check_action():
    while True:
        decision = input("Do you want to copy or move files?\n")
        if decision == "move":
            return True
        elif decision == "copy":
            return False


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
def path_exists(dir_path) -> bool:
    if not os.path.exists(dir_path):
        return False
    return True


# return path to desktop
# def ret_desktop_path():
#     user_path = os.path.expanduser("~")
#     desktop_p = os.path.join(user_path, "Desktop")
#     return desktop_p
    

# list directory (desktop) content
def list_dir_content(dir_content):
    print("Content of the desktop:\n")
    for obj in dir_content:
        print(obj)
    return True


# return content of desktop directory or drop an Exception.
def ret_dir_content(dire):
    try:
        content = os.listdir(dire)
        return content
    except FileNotFoundError:
        print(f"{dire} doesn't exist.\n")
    except FileExistsError:
        print(f"Cannot access {dire}.\n")
    except Exception(f"Unknown exception when accessing the {dire}.\n") as e:
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


# Copy/moves content of desktop to destination folder by file extension.
def perform_action(action, src, folders, cleanedup, dir_content):
    tmp = src
    for obj in dir_content:
        ext = check_ext(obj)
        src = tmp
        src = os.path.join(src, obj)
        dest = ret_dest(ext, folders)
        dest = os.path.join(cleanedup, dest)
        if os.path.isfile(src) and not action:
            try:
                shutil.copy(src, dest)
                print(f"{obj} copied to {dest}.")
            except Exception as e:
                print("Copied failed.")
                raise e
            print("Copied successfully.")
        elif os.path.isfile(src) and action:
            try:
                shutil.move(src, dest)
                print(f"{obj} moved to {dest}.")
            except Exception as e:
                print("Moving failed.")
                raise e
            print("Moved successfully.")
    

# returns file extension
def check_ext(file):
    try:
        return pathlib.Path(file).suffix
    except Exception as e:
        raise e


# returns destination by file extension
def ret_dest(ext, folders):
    for dirname in folders:
        for exts in folders[dirname]:
            if exts == ext:
                return dirname
    return "Other"


def main():
    # Make the folder CleanedUp/
    term_msg = "Program is terminating"
    dst = input("Where do you want to create CleanedUp folder.\n")
    src = input("Where do you want to clean up?\n")
    decision = check_action()

    cleanedup = create_dir(dst, "CleanedUp")
    if type(cleanedup) != str:
        print(term_msg)
        return False

    folders = {
        "Images": [".jpeg", ".jpg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".xls", ".epub", ".eml", ".odt", ".odt#", ".html"],
        "Archives": [".zip", ".rar", ".tar", ".7z", ".tar.gz"],
        "Shortcuts": [".lnk", ".desktop"],
        "Scripts": [".sh", ".ps"],
        "Other": [],
    }

    # Return desktop path
    # desktop_path = ret_desktop_path()
    # Check if desktop exists
    path_exist: bool = path_exists(src)
    if not path_exist:
        print("Path doesn't exist.\n")
        raise Exception(FileNotFoundError)

    # Return desktop content
    content = ret_dir_content(src)
    # List the files in the desktop/ folder
    list_dir_content(content)
    
    # Creates subfolders based on folders dictionary.
    if not create_subdirs(folders, cleanedup):
        print(term_msg)
        return False

    # For each file in the source folder copy/move the file to the destination/CleanedUp folder
    perform_action(decision, src, folders, cleanedup, content)


main()
