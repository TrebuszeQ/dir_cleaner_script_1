import os
import shutil


def create_dir(destination):
    path = destination + "/CleanedUp"
    try:
        os.mkdir(path)
        print("File has been created.\n\n")
    except FileExistsError:
        print("Directory couldn't been made, file exists.\n\n")
    except Exception as err:
        print("Directory couldn't been made.\n\n")
        raise err
    return True


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


def is_linux() -> str | bool:
    home = os.getenv("HOME")
    if type(home) == str:
        return home
    else:
        return False

def get_user_w() -> str | bool:
    userprofile = os.getenv("USERPROFILE")
    if type(userprofile) == str:
        return userprofile
    else:
        print("Coudln't get %UserProfile%")
        return False


def ret_desktop_path(home):
    user_w = get_user_w()
    win_desktop = f"{user_w}\\Desktop\\"
    lin_desktop = f"{home}/Desktop"

    if not home:
        return win_desktop

    elif type(home) == str:
        return lin_desktop

    else:
        raise Exception("Unknown OS or unknown exception.\n\n")


def list_dir_content(content):
    for obj in content:
        print(obj)
    return True


def cp_content(src, dest, content, system):
    sign = ''
    if system:
        sign = '/'
    try:
        for obj in content:
            src = src + sign + obj
            shutil.copyfile(src, dest)
            print(f"{obj} copied to {dest}.\n")
    except Exception as e:
        print("Unknown exception encountered.\n\n")
        raise e
    


def main():
    # Make the folder CleanedUp/
    destination = input("Where do you want to create CleanedUp folder.\n")
    access_modes = [
        os.F_OK,
        os.R_OK,
        os.W_OK,
        os.X_OK
    ]
    system: str | bool = is_linux()
    path_exist: bool = os.access(destination, access_modes[0])
    if not path_exist:
        print("Path doesn't exist.\n")
        return FileNotFoundError
    elif path_exist:
        create_dir(destination)
    # Return desktop path
    desktop_path = ret_desktop_path(system)
    # List the files in the desktop/ folder
    content = ret_desktop_content(desktop_path, system)
    list_dir_content(content)
    # For each file in the Desktop/ folder copy the file to the CleanedUp/ folder
    cp_content(desktop_path, destination, content, system)


main()