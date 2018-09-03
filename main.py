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
pictures_dir = '/Users/' + mac_username + '/Desktop/pictures'
documents_dir = '/Users/' + mac_username + '/Desktop/documents'
scripts_dir = '/Users/' + mac_username + '/Desktop/scripts'
media_dir = '/Users/' + mac_username + '/Desktop/media'
misc_dir = '/Users/' + mac_username + '/Desktop/misc'


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


def moveFile(folder, src, dst):
    filetomove = (str(folder) + str(src))
    movingfileto = (str(dst) + str(file))
    shutil.move(filetomove, movingfileto)


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

    # Print all files inside the Desktop Directory
    # print('FILES INSIDE ' + folderName + ': ')
    # for filename in filenames:
    #     print(filename)
    for file in filenames:
        if searchInList(file, pictures):
            directoryCheck(pictures_dir)
            moveFile(search_dir, file, pictures_dir)

    print('')