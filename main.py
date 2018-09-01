import os

# Types of files
pictures = ['.png', '.jpeg']
documents = ['.docx', '.pdf']
scripts = ['.sh', '.py']
media = ['.mp3', '.avi', '.mkv']

# Username
mac_username = str(os.system('echo $USER'))

search_dir = '/Users/' + mac_username + '/Desktop/'

target_folders = ['/Users/' + mac_username + '/Desktop/pictures',
                  '/Users/' + mac_username + '/Desktop/documents',
                  '/Users/' + mac_username + '/Desktop/scripts',
                  '/Users/' + mac_username + '/Desktop/media']

