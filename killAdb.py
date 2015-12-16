import os
processToKill = ["adb.exe", "androidserver.exe", "360mobilemgr.exe"]
for process in processToKill:
    os.system("taskkill /F /IM %s" % process)
