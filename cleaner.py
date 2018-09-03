from sys import platform as _platform
import shutil
import os
from os.path import expanduser

#####################
##### VARIABLES #####
#####################
home = expanduser("~")

# Types of files
pictures = ('.png', '.jpeg')
documents = ('.docx', '.pdf', '.txt')
scripts = ('.sh', '.py',)
media = ('.mp3', '.avi', '.mkv')

# Check which OS is running and
# Create the required directory variables
# linux or MAC OS X
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    if os.path.isdir(home+"/Desktop/"):
        search_dir = home+"/Desktop/"
        pictures_dir = search_dir+"pictures/"
        documents_dir = search_dir+"documents/"
        scripts_dir = search_dir+"scripts/"
        media_dir = search_dir + "media/"
        misc_dir = search_dir+"misc/"
    else:
        desktop = "Your " + _platform + " does not have a Desktop Directory"
# Windows 32-bit or 64-bit
elif _platform == "win32" or _platform == "win64":
    if os.path.isdir(home+"\Desktop"):
        search_dir = home+"\Desktop\\"
        pictures_dir = search_dir+"\pictures\\"
        documents_dir = search_dir+"\documents\\"
        scripts_dir = search_dir+"\scripts\\"
        media_dir = search_dir + "\media\\"
        misc_dir = search_dir+"\misc\\"
    else:
        desktop = "Your " + _platform + " does not have a Desktop Directory"

####################
#### FUNCTIONS #####
####################


# Check if Directory exist, otherwise create it.
def directoryCheck(pdir):
    if os.path.isdir(str(pdir)):
        return True
    else:
        os.system('mkdir -v ' + str(pdir))
        return True


def moveFile(src, dst):
    filetomove = (str(search_dir) + str(src))
    shutil.move(filetomove, str(dst))


# Checks the extension of the file to the Tuple at the start
def searchInList(filetocheck, array):
    if filetocheck.endswith(array):
        return True
    else:
        return False

####################
#### THE MEAT #####
####################


# Walk through the Desktop Directory
for folderName, subfolders, filenames in os.walk(search_dir):
    print('The current folder is ' + folderName, '\n')
    for file in filenames:
        # Pictures
        try:
            if searchInList(file, pictures):
                directoryCheck(pictures_dir)
                moveFile(file, pictures_dir)
            elif searchInList(file, documents_dir):
                directoryCheck(documents_dir)
                moveFile(file, documents_dir)
            elif searchInList(file, scripts_dir):
                directoryCheck(scripts_dir)
                moveFile(file, scripts_dir)
            elif searchInList(file, media_dir):
                directoryCheck(media_dir)
                moveFile(file, media_dir)
            else:
                directoryCheck(misc_dir)
                moveFile(file, misc_dir)
        except shutil.Error as err:
            print("Nothing to do.")
            break

    print('')
