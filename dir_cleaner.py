import os
import shutil


def create_dir(destination):
    path = destination + "/CleanedUp"
    try:
        os.mkdir(path)
        print("File has been created.\n")
    except FileExistsError:
        print("Directory couldn't been made, file exists.\n")
    except Exception as err:
        print("Directory couldn't been made.\n")
        raise err
    return True


def ret_desktop_content(desktop):
    home = is_linux()

    if not home:

        try:
            content = os.scandir(desktop)
            print(content)
            return content
        except FileNotFoundError:
            print(f"{desktop} doesn't exist.\n")
        except FileExistsError:
            print(f"Cannot access {desktop}.\n")
        except Exception("Unknown exception when accessing the desktop\n") as e:
            raise e

    elif type(home) == str:
        try:
            content = os.listdir(desktop)
            return content
        except FileNotFoundError:
            print(f"{desktop} doesn't exist.\n")
        except FileExistsError:
            print(f"Cannot access {desktop}.\n")
        except Exception as e:
            print("Unknown exception when accessing the desktop\n")
            raise e
    return False


def is_linux() -> str | bool:
    home = os.getenv("HOME")
    if type(home) == str:
        return home
    else:
        print("Windows operating system.\n")
        return False


def ret_desktop_path():
    home = is_linux()
    win_desktop = "%UserProfile%\\Desktop\\"
    lin_desktop = f"{home}/Desktop"

    if not is_linux():
        print("Windows OS.\n")
        return win_desktop

    elif type(is_linux()) == str:
        return lin_desktop

    else:
        raise Exception("Unknown OS or unknown exception.\n")


def list_dir_content(content):
    for obj in content:
        print(obj.name)
    return True


def cp_content(src, dest, content):
    dest = dest + '/' + 'CleanedUp'
    try:
        for obj in content:
            src = src + '/' + obj
            shutil.copyfile(src,dest)
            print(f"{obj} copied to {dest}.")
    except Exception as e:
        print("Unknown exception encountered.\n")
        raise e
    return False


def main():
    # Make the folder CleanedUp/
    destination = input("Where do you want to create CleanedUp folder.\n")
    access_modes = [
        os.F_OK,
        os.R_OK,
        os.W_OK,
        os.X_OK
    ]
    path_exist: bool = os.access(destination, access_modes[0])
    if not path_exist:
        print("Path doesn't exist.\n")
        return FileNotFoundError
    elif path_exist:
        create_dir(destination)
    # Return desktop path
    desktop_path = ret_desktop_path()
    # List the files in the desktop/ folder
    content = ret_desktop_content(desktop_path)
    for obj in content:
        print(obj)
    # For each file in the Desktop/ folder copy the file to the CleanedUp/ folder
    cp_content(desktop_path,destination, content)


main()