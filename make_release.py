# Run from cloned local repo, has a dependency on being run from an LFS enabled repo directory
import os
import zipfile
import git
import shutil
import time
import stat
from git import Repo

tempWorkingDir = "../repoCheckOutTemp/Add-On Kuwait UOAF"
tempWorkingDirRoot = "../repoCheckOutTemp/"
'''
Error handler function
It will try to change file permission and call the calling function again,
'''
def handleError(func, path, exc_info):
    print('Handling Error for file ' , path)
    print(exc_info)
    # Check if file access issue
    if not os.access(path, os.W_OK):
       # Try to change the permision of file
       os.chmod(path, stat.S_IWUSR)
       # call the calling function again
       func(path)

def deleteFolderAndFiles(path):
    try:
        print("Trying to delete ",path)
        shutil.rmtree(path, ignore_errors=False, onerror=handleError)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))    

deleteFolderAndFiles(tempWorkingDirRoot)

print ("git clone starting...")
time.sleep(2) # Had to do this because git clone is throwing access denied without it, probably due to a race condition with rmtree
Repo.clone_from("https://github.com/tyrspawn/kuwaitmodded", tempWorkingDir)
print("git clone done")

#copy readme.md to working dir root
shutil.copyfile(os.path.join(tempWorkingDir, "README.md"), os.path.join(tempWorkingDirRoot, "README.md"))

def get_theater_version():
    with open(os.path.join(tempWorkingDir, 'TerrData', 'theaterdefinition', 'kuwait.tdf'), 'r') as tdf:
        for line in tdf:
            if line.startswith('desc'):
                version_token = line.split()[-1].strip()
                print ("Preparing version ", version_token)
                return version_token
    raise ValueError("Version not found in theater")

ver = get_theater_version()

# delete black list files from working dir
blackListFiles = [".gitattributes",".gitignore", "make_release.py"]

for file in blackListFiles:
    if os.path.isfile(os.path.join(tempWorkingDir,file)):
        os.remove(os.path.join(tempWorkingDir,file))

# delete .git dir from working dir
deleteFolderAndFiles(os.path.join(tempWorkingDir,".git"))

print ("Starting zip archive to ", os.path.dirname(os.path.abspath(__file__ + "/..")))
shutil.make_archive((os.path.join('..', 'Kuwait UOAF.{}'.format(ver))), 'zip', tempWorkingDirRoot)
print ("Finished archive")

deleteFolderAndFiles(tempWorkingDirRoot)