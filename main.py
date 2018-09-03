import os, shutil

####################
#### VARIABLES #####
####################

# Types of files
pictures = ('.png', '.jpeg')
documents = ('.docx', '.pdf', '.txt')
scripts = ('.sh', '.py',)
media = ('.mp3', '.avi', '.mkv')

# Username
mac_username = 'marcomarques'

# Directories needed
search_dir = '/Users/' + mac_username + '/Desktop/'
pictures_dir = '/Users/' + mac_username + '/Desktop/pictures/'
documents_dir = '/Users/' + mac_username + '/Desktop/documents/'
scripts_dir = '/Users/' + mac_username + '/Desktop/scripts/'
media_dir = '/Users/' + mac_username + '/Desktop/media/'
misc_dir = '/Users/' + mac_username + '/Desktop/misc/'

ignore_folders = [pictures_dir, documents_dir, scripts_dir,
                  media_dir, misc_dir]


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
        try:
            if searchInList(file, pictures):        # Pictures
                directoryCheck(pictures_dir)
                moveFile(file, pictures_dir)
            elif searchInList(file, documents):     # Docs
                directoryCheck(documents_dir)
                moveFile(file, documents_dir)
            elif searchInList(file, scripts):       # Scripts
                directoryCheck(scripts_dir)
                moveFile(file, scripts_dir)
            elif searchInList(file, media):         # Media
                directoryCheck(media_dir)
                moveFile(file, media_dir)
            else:
                directoryCheck(misc_dir)            # Other/Misc
                moveFile(file, misc_dir)
        except shutil.Error as err:
            print("Nothing to do.")
            break
    print('')