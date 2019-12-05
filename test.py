from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import keyboard
makeRelease = 0
print ("Press the G key to automatically upload the zip to google drive release folder afterwards, otherwise press any other key to continue")
while True:
    try:
        if keyboard.is_pressed('g'):
            makeRelease = 1
            print('The release will be uploaded after zip!')
            break
    except:
        break

if (makeRelease == 1):

    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()
    print ("Try to load saved client credentials")
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        print ("No credential found, web auth attempt starting, credentials will be generated later")
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        print ("Access token expired, refreshing...")
        gauth.Refresh()
    else:
        print ("Initializing saved credentials")
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    print ("Attempting Google Drive API auth")

    drive = GoogleDrive(gauth)
    print ("Uploading release to google drive")
    file_path = "readme.pdf"
    file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": "1LT_8TnwcvA38N4SjMD8OQmJ3RgYjyFuz"}]})
    file1.SetContentFile(file_path)
    file1.Upload()
    print ("Upload complete")
   