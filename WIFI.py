#!/.venv/bin/python3
import wireless
from wifi import Cell
from scapy.all import *

#setup interface for wifi network searching
wifi1 = wireless.Wireless()
interface = wifi1.interface()




def FindNetworks():
    #using interface to search for networks within range
    wifiNetworks = Cell.all(interface)
    
    for wifi in wifiNetworks():
        print(f"Network Name: {wifi.ssid}")
        print(f"Network Address: {wifi.address}")
        print(f"Network Channel: {str(wifi.channel)}")
        print(f"Network Quality: {str(wifi.quality)}")
    #return list of networks

def Deauth(network):
    print(f"Deauthing {network}")
    #send deauth packet to network

def SaveNetwork(network):
    print(f"saving {network}")
    #save network data to file of networks saved

def EmulateNetwork(network):
    print(f"emulating {network}")
