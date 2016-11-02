# A good chunk of this file was taken from @Jenfoxbot here
# https://github.com/jenfoxbot/SoilSensorAPI/blob/master/JenFoxBotSMSV1c.py
# I've made modifications since:
# Remove the file write


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Define function to measure charge time
def RC_Analog(Pin):
    counter=0
    start_time = time.time()
    #Discharge capacitor
    GPIO.setup(14, GPIO.OUT)
    GPIO.output(14, GPIO.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    GPIO.setup(14, GPIO.IN)
    #Count loops until voltage across capacitor reads high on GPIO
    while (GPIO.input(14)==GPIO.LOW):
        counter=counter+1
    end_time = time.time()
    return end_time - start_time

while True:
    time.sleep(1)
    ts = time.time()
    reading = RC_Analog(4) #store counts in a variable
    counter = 0
    time_start = 0
    time_end = 0
    
    print ts, reading  #print counts using GPIO4 and time

    while (reading < 10.00):
        time_start = time.time()
        counter = counter + 1
        if counter >= 50:
            break
    time_end = time.time()
    if (counter >= 25 and (time_end - time_start) <= 60): # if you get 25 measurements that indicate dry soil in less than one minute, need to water
        print('Not enough water for your plants to survive! Please water now.') #comment this out for testing
    #else:
        #print('Your plants are safe and healthy, yay!')

GPIO.cleanup()