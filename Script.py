import os
import shutil

# Function to organize files
def organize_files(folder_path):
    # Get all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create folders for each file extension
    for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        folder_name = file_extension.upper() + "_Files"

        # Create folder if it doesn't exist
        if not os.path.exists(os.path.join(folder_path, folder_name)):
            os.makedirs(os.path.join(folder_path, folder_name))

        # Move the file to the respective folder
        shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, folder_name, file))

    print("File organization complete.")

# Provide the folder path to organize
folder_path = "C:/Path/To/Folder"

# Call the organize_files function
organize_files(folder_path)
