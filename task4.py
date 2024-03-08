import os
import shutil

def organize_files(source_dir, destination_dir):
    # Ensure destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        # Get the full path of the file
        source_file = os.path.join(source_dir, filename)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(source_file):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]

            # Define the destination directory based on file extension
            destination_subdir = os.path.join(destination_dir, file_extension[1:])
            
            # Ensure destination subdirectory exists, if not, create it
            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)

            # Define the destination file path
            destination_file = os.path.join(destination_subdir, filename)

            # Move the file to the destination directory
            shutil.move(source_file, destination_file)

            print(f"Moved {filename} to {destination_subdir}")

# Example usage:
source_directory = "path"
destination_directory = "path"

organize_files(source_directory, destination_directory)