#Import-> To use/import python libraries
import os
import datetime

#To Print System Info using User Function
def sys_info(command):
    print(os.system(command))
sys_info("systeminfo")

#To Print Date of Today using User Function
def date_today():
    return datetime.datetime.today()
print(date_today())