#!/.venv/bin/python3

from adafruit_pn532.i2c import PN532_I2C

SCLPin = 0
SDAPin = 0
i2c = (SCLPin, SDAPin)

detect = False
emulate = False
write = False

def SaveCard(cardName, cardData):
    print(f"Saving {cardName}")
    #write card data to file named cardName
    #save file

def GetData(cardName):
    print(f"Getting data from {cardName}")
    #read file
    #return file contents

def ReadCard():
    detect = True

    while detect == True:
        print("test read")
        #detect shit
        #if detected grab data
        #save card

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
