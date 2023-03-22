import RPi.GPIO as GPIO

def dectobin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)

try:
    while(True):
        str = input()
        if str == 'q':
            break
        elif int(str) < 0:
            print("Negative number")
        elif int(str) > 255:
            print("More than 255")
        else:
            decin = int(str)
            x = dectobin(decin)
            for i in range(8):
                GPIO.output(dac[i], x[i])
            print(3.3 * decin / 256)
    
finally:
    for i in dac:
        GPIO.output(dac, 0)
    GPIO.cleanup()
