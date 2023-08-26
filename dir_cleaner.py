import os


def create_dir(destination):
    path = destination + "/CleanedUp"
    try:
        os.mkdir(path)
        print("File has been created.\n")
    except FileExistsError:
        print("Directory couldn't been made, file exists.\n")
    except Exception as err:
        print("Directory couldn't been made.\n")
        print(err)
        print("\n")
    return True


def scan_desktop():
    win_desktop = "%UserProfile%\\Desktop\\"
    lin_desktop = "~/Desktop"
    print(lin_desktop)
    if not is_linux():

        try:
            content = os.scandir(win_desktop)
            print(content)
            return content
        except FileNotFoundError:
            print(f"{win_desktop} doesn't exist.\n")
        except FileExistsError:
            print(f"Cannot access {win_desktop}.\n")
        except:
            print("Unknown exception when accessing the desktop\n")

    elif is_linux():
        try:
            content = os.scandir(lin_desktop)
            print(content)
            return content
        except FileNotFoundError:
            print(f"{lin_desktop} doesn't exist.\n")
        except FileExistsError:
            print(f"Cannot access {lin_desktop}.\n")
        except:
            print("Unknown exception when accessing the desktop\n")
    return False


def is_linux():
    try:
        os.getenv("$PATH")
        return True
    except:
        print("Windows operating system.\n")
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
    # List the files in the Desktop/ folder
    scan_desktop()
    # For each file in the Desktop/ folder move the file to the CleanedUp/ folder


main()