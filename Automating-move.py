import shutil
import os

source = "C:/Users/user/Downloads/"
#C:\Users\user\Documents\Old Data\Download\stellio-player\backup << python does not recognize these back slashes

files = os.listdir(source)
#try:
for file in files:
              if file.endswith((".docx", ".pdf", ".doc", ".epub", ".txt", ".xlsx", "pptx", ".cbz", ".torrent", ".csv")):
                     destination = "C:/Users/user/Documents/Libraries"
                     #Split name and extension
                     data = os.path.splitext(file)
                     only_name = data[0]
                     extension = data[1]
                     #Adding the new name
                     new_base = only_name + '_new' + extension
                     # construct full file path
                     new_name = os.path.join(destination, new_base)
                     # move file
                     shutil.move(source+file, new_name)
                
              elif file.endswith((".avi", ".3gp", ".3g2", ".mp4", ".m4v", ".mov", ".mkv", ".wmv", ".mpg", ".mpeg", ".m4a", "wma", ".3gpp")):
                     destination = "C:/Users/user/Videos"
                     data = os.path.splitext(file)
                     only_name = data[0]
                     extension = data[1]
                     #
                     new_base = only_name + '_new' + extension
                     #
                     new_name = os.path.join(destination, new_base)
                     #
                     shutil.move(source+file, new_name)
                     
              elif file.endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".gif", ".psd")):
                     destination = "C:/Users/user/Pictures"
                     data = os.path.splitext(file)
                     only_name = data[0]
                     extension = data[1]
                     #
                     new_base = only_name + '_new' + extension
                     #
                     new_name = os.path.join(destination, new_base)
                     #
                     shutil.move(source+file, new_name)
                     
              elif file.endswith((".exe", ".iso", ".bin", ".bat", ".apk", ".msi", ".cgi")):
                     destination = "C:/Users/user/Documents/Apps"
                     data = os.path.splitext(file)
                     only_name = data[0]
                     extension = data[1]
                     #
                     new_base = only_name + '_new' + extension
                     #
                     new_name = os.path.join(destination, new_base)
                     #
                     shutil.move(source+file, new_name)
                     
              elif file.endswith((".mp3", ".aac", ".wav", ".flac", ".mpeg", ".ogg")):
                     destination = "C:/Users/user/Music"
                     data = os.path.splitext(file)
                     only_name = data[0]
                     extension = data[1]
                     #
                     new_base = only_name + '_new' + extension
                     #
                     new_name = os.path.join(destination, new_base)
                     #
                     shutil.move(source+file, new_name)
                     
#except shutil.Error as err:
     #errors.extend(err.args[0])
     #pass
    