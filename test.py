from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

file_path = "readme.pdf"
file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": "1LT_8TnwcvA38N4SjMD8OQmJ3RgYjyFuz"}]})
file1.SetContentFile(file_path)
file1.Upload()