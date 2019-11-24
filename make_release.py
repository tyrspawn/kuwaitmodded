import os
import zipfile

def get_theater_version():
    with open(os.path.join('TerrData', 'theaterdefinition', 'kuwait.tdf'), 'r') as tdf:
        for line in tdf:
            if line.startswith('desc'):
                version_token = line.split()[-1].strip()
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
                if filesystem_path.lower().startswith('campaign'):
                    if filesystem_path.lower().endswith('.cam'):
                        f = file.lower()
                        if f not in ('save0.cam', 'save1.cam', 'save2.cam'):
                            continue

                    
                archive_path = os.path.join('Add-On Kuwait UOAF', filesystem_path)
                print(filesystem_path)
                ziph.write(filesystem_path, arcname=archive_path)
    ziph.write('README.md')

if __name__ == '__main__':
    ver = get_theater_version()
    with zipfile.ZipFile(os.path.join('..', 'Kuwait UOAF.{}.zip'.format(ver)), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('.', zipf)
    
