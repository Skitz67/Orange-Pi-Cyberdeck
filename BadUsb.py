import shutil

def WriteUsb(appName, label, icon, usbName, fileSuffix):
    if icon == None:
        icon = appName + fileSuffix
    #create and write startup file
    f = open("autorun.txt", "w")
    f.write(f"[Autorun]\nOpen={appName}{fileSuffix}\nAction=Start {appName}\nLabel={label}\nIcon={icon}")
    f.close()
    #move file to root usb
    shutil.move("path to file", "C://")

WriteUsb("appname.exe", "testLabel", "icon.ico", "usbname", ".exe")