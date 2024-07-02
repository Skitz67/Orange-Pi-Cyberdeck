import time
import logging
from OPIGPIO.opi_gpio import OPIGPIO

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the GPIO class
gpio = OPIGPIO()

# Run any setup code
gpio.setup()

#Set pin variables
IRDATA = 12
# Set the mode of pin 12 as output
gpio.pinMode(IRDATA, "out")


#ir spamming function
def Spam(reps=1, delay=1):
    for i in range(reps):
        gpio.digitalWrite(IRDATA, 1)
        time.sleep(delay)
        gpio.digitalWrite(IRDATA, 0)

def OnSig():
    #turns on lol
    gpio.digitalWrite(IRDATA, 1)
    
def OffSig():
    #turns off lol
    gpio.digitalWrite(IRDATA, 0)