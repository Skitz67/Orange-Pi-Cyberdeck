#!/.venv/bin/python3

from Adafruit_PN532 import PN532_I2C
from digitalio import DigitalInOut
import busio
import board

#sets clock and data pins
SCLPin = 0
SDAPin = 0

#begin setting up i2c connection
i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
# I have no idea what the FUCK this means ^^^
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
# Configure PN532 to communicate with MiFare cards
# MiFare cards are just a brand name version of rfid cards with different versions
pn532.SAM_configuration()

emulate = False
write = False

def SaveCard(cardName, cardData):
    print(f"Saving card as {cardName}")
    f = open(cardName, "w")
    f.write(cardData)
    f.close()

def GetData(cardName):
    print(f"Getting data from {cardName}")
    f = open(cardName, "r")
    return f.read()

def ReadCard():
    while True:
        id = pn532.read_passive_target(timeout=0.5)
        if id is None:
            continue
        print(f"card data found: {id}")
        #read code on card, somthing  about blocks and block numbers idfk
        #seriously you gotta make progress here



def EmulateCard(cardName):
    emulate = True
    #getData from cardName
    while emulate == True:
        print("test emulate")
        #emulate cardData
        #check if back button pressed
        #stop emulating

def WriteCard(cardName):
    write = True
    #getData from cardName
    while write == True:
        print("test write")
        #detect if card present
        #write cardData to card
