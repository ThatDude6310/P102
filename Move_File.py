import os
import shutil

source = "C:/Pankil/Python/Projects/P102-organiser/Downloads/"
destination = "C:/Pankil/Python/Projects/P102-organiser"
listOfFiles = os.listdir(source)



for i in listOfFiles:

    path1 = source + "/" + i
    path2 = destination + "/" + "Document_File"
    path3 = destination + "/" + "Document_Files" + "/" + i

    root,extension = os.path.splitext(i)

    if extension == "":
        continue

    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:

        if os.path.exists(path2):
            print("Moving"+ i)
            shutil.move(path1,path3)
        else:
            print("Creating folder and moving" + i)
            os.mkdir(path2)
            shutil.move(path1,path3)
         