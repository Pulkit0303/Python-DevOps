import shutil
import os
import datetime

def backupfiles(source,destination):
    today = datetime.date.today()
    backupfile_name = os.path.join(destination,f"backup{today}")
    shutil.make_archive(backupfile_name,"zip",source)

source = r"C:\Users\pulki\Desktop\Code\Python"
destination = r"C:\Users\pulki\Desktop\Code\Python\Backups"
backupfiles(source,destination)