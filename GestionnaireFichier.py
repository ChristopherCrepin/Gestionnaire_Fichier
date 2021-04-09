import os,time,stat

one_minute_ago = time.time() - 86400
folder = '/data/usbshare/Share/'
os.chdir(folder)
for somefile in os.listdir('.'):
    mtime=os.path.getmtime(somefile)
    if mtime < one_minute_ago:
        os.unlink(somefile)