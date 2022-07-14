import shutil
import time
import os


def main():
    deleted_folders = 0
    deleted_files = 0

    path = "path where you have to delete files"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= getFileOrFoldersAge(path):
                remove_folder(root_folder)
                deleted_folders += 1
                break
            else:
                for folder in folder:
                    folderPath = os.path.join(root_folder, folder)
                    if seconds >= getFileOrFoldersAge(folderPath):
                        remove_folder(folderPath)
                        deleted_folders += 1

                for file in files:
                    filePath = ios.path.join(root_folder, file)
                    if seconds >= getFileOrFoldersAge(filePath):
                        remove_file(filePath)
                        deleted_files += 1
        else:
            if seconds >= getFileOrFoldersAge(path):
                remove_file(path)
                deleted_files += 1
    else:
        print(f'{path} is not found.')
        deleted_files += 1

    print(f"Total Files Deleted: {deleted_files}")
    print(f"Total Folder Deleted: {deleted_folders}")


def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully!")
    else:
        print(f"Unable to delete {path}")


def remove_file(path):
    if os.remove(path):
        print(f"{path} is removed successfully!")
    else:
        print(f"Unable to delete {path}")


def getFileOrFoldersAge(path):
    ctime = os.stat(path).st_ctime
    return ctime


main()
