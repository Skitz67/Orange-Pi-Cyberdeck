#!/.venv/bin/python3
import wireless
from wifi import Cell
import scapy.all as scapy



def FindNetworks():
    print(f"finding networks")
    #scan networks within area
    #return list of networks

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