import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder not found!")
else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension = filename.split(".")[-1]

            new_folder = os.path.join(folder_path, extension.upper() + "_FILES")
            os.makedirs(new_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(new_folder, filename))

    print("Files organized successfully!")
