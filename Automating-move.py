import shutil
import os

def move_files(source, destination):
    """
    Moves files from the source directory to the appropriate category directories in the destination directory.
    """
    files = os.listdir(source)
    errors = []

    for file in files:
        try:
            # Categorize files based on their extensions
            if file.endswith((".docx", ".pdf", ".doc", ".epub", ".txt", ".xlsx", ".pptx", ".cbz", ".torrent", ".csv", ".cbr")):
                move_file(source, file, destination, "Documents")
            elif file.endswith((".avi", ".3gp", ".3g2", ".mp4", ".m4v", ".mov", ".mkv", ".wmv", ".mpg", ".mpeg", ".m4a", ".wma", ".3gpp")):
                move_file(source, file, destination, "Videos")
            elif file.endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".gif", ".psd")):
                move_file(source, file, destination, "Pictures")
            elif file.endswith((".exe", ".iso", ".bin", ".bat", ".apk", ".msi", ".cgi")):
                move_file(source, file, destination, "Apps")
            elif file.endswith((".mp3", ".aac", ".wav", ".flac", ".mpeg", ".ogg")):
                move_file(source, file, destination, "Music")
            else:
                move_file(source, file, destination, "Other")
        except Exception as err:
            errors.append((file, err))
    
    if errors:
        print("Errors occurred while moving files:")
        for file, err in errors:
            print("Error moving '{}': {}".format(file, err))

def move_file(source, file, destination, category):
    """
    Moves a file to the appropriate category directory within the destination directory.
    """
    data = os.path.splitext(file)
    only_name = data[0]
    extension = data[1]
    
    if not extension:
        raise ValueError("File '{}' has no extension.".format(file))
    
    new_base = only_name + '_new' + extension
    category_dir = os.path.join(destination, category)
    os.makedirs(category_dir, exist_ok=True)
    new_name = os.path.join(category_dir, new_base)
    shutil.move(os.path.join(source, file), new_name)

if __name__ == "__main__":
    # Define source and destination directories
    source_dir = "C:/Users/user/Downloads/"
    destination_dir = "C:/Users/user/Documents/Libraries"
    
    # Organize files
    move_files(source_dir, destination_dir)
