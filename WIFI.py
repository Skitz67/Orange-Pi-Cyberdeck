#!/.venv/bin/python3
import wireless
from wifi import Cell
import scapy.all as scapy
import subprocess as sub



def FindNetworks():
    # using the check_output() for having the network term retrieval 
    devices = sub.check_output(['netsh','wlan','show','network'])
    # decode it to strings 
    devices = devices.decode('ascii') 
    devices= devices.replace("\r","") 
    #return list of networks found
    devices = devices.split("\n")
    
    return devices

def ScanNetwork(network):
    print(f"scanning {network}")

def Deauth(network):
    print(f"Deauthing {network}")
    #send deauth packet to network

def SaveNetwork(network):
    print(f"saving {network}")
    #save network data to file of networks saved

def EmulateNetwork(network):
    print(f"emulating {network}")

print(FindNetworks())