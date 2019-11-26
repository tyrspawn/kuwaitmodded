# Run from cloned local repo, has a dependency on being run from an LFS enabled repo directory
import os
import zipfile
import git
import shutil
import time
import stat
from git import Repo

tempWorkingDir = "../repoCheckOutTemp"

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

try:
    print("Trying to delete working dir")
    shutil.rmtree(tempWorkingDir, ignore_errors=False, onerror=handleError)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

print ("git clone starting...")
# Had to do this because git clone is throwing access denied without it, probably due to a race condition with rmtree
time.sleep(2)
Repo.clone_from("https://github.com/tyrspawn/kuwaitmodded", tempWorkingDir)
print("git clone done")

def get_theater_version():
    with open(os.path.join(tempWorkingDir, 'TerrData', 'theaterdefinition', 'kuwait.tdf'), 'r') as tdf:
        for line in tdf:
            if line.startswith('desc'):
                version_token = line.split()[-1].strip()
                print (version_token)
                return version_token
    raise ValueError("Version not found in theater")

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, _, files in os.walk(path):
        for file in files:
            if not file.startswith('.git') and not file.endswith('.py'):
                filesystem_path = os.path.normpath(os.path.join(root, file))
                if filesystem_path.startswith('.git'):
                    continue
                
                archive_path = os.path.join('Add-On Kuwait UOAF', filesystem_path)
                print(filesystem_path)
                ziph.write(filesystem_path, arcname=archive_path)
    ziph.write('README.md')

if __name__ == '__main__':
    ver = get_theater_version()
    with zipfile.ZipFile(os.path.join('..', 'Kuwait UOAF.{}.zip'.format(ver)), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(tempWorkingDir, zipf)
        try:
            print("Try deleting working dir")
            shutil.rmtree(tempWorkingDir, ignore_errors=False, onerror=handleError)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        print(filesystem_path)