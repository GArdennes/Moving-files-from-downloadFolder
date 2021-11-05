import shutil
import os

source = "C:/Users/user/Downloads"
#C:\Users\user\Documents\Old Data\Download\stellio-player\backup << python does not recognize these back slashes

files = os.listdir(source)
#try:
for file in files:
              if file.endswith((".docx", ".pdf", ".doc", ".epub", ".txt", ".xlsx")):
                     destination = "C:/Users/user/Documents/Libraries"
                     new_path = shutil.move(f"{source}/{file}", destination)
                     #print(new_path) 
              elif file.endswith((".avi", ".3gp", ".3g2", ".mp4", ".m4v", ".mov", ".mkv", ".wmv", ".mpg", ".mpeg", ".m4a")):
                     destination = "C:/Users/user/Videos"
                     new_path = shutil.move(f"{source}/{file}", destination)
                     #print(new_path)
              elif file.endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".gif", ".psd")):
                     destination = "C:/Users/user/Pictures"
                     new_path = shutil.move(f"{source}/{file}", destination)
                     #print(new_path)
              elif file.endswith((".exe", ".iso", ".bin", ".bat", ".apk", ".msi", ".cgi")):
                     destination = "C:/Users/user/Documents/Apps"
                     new_path = shutil.move(f"{source}/{file}", destination)
                     #print(new_path)
              elif file.endswith((".mp3", ".aac", ".wav", ".flac", ".mpeg", ".ogg")):
                     destination = "C:/Users/user/Music"
                     new_path = shutil.move(f"{source}/{file}", destination)
                     #print(new_path)
#except shutil.Error as err:
     #errors.extend(err.args[0])
     #pass