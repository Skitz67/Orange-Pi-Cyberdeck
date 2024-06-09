from adafruit_pn532.i2c import PN532_I2C

SCLPin = 0
SDAPin = 0
i2c = (SCLPin, SDAPin)

detect = False
emulate = False
write = False

def ReadCard():
    detect = True

    while detect == True:
        print("test read")
        #detect shit
        #if detected grab data
        #save data

def EmulateCard(card):
    emulate = True

    while emulate == True:
        print("test emulate")
        #emulate card variable
        #check if back button pressed
        #stop emulating

def WriteCard(card):
    write = True
    
    while write == True:
        print("test write")
        #detect if card present
        #write card variable to 
