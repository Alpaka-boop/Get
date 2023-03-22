import RPi.GPIO as GPIO
import time

def dectobin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)

try:
    for i in range(10):
        for j in range(256):
            x = dectobin(j)
            for k in range(8):
                GPIO.output(dac[k], x[k])
            time.sleep(0.00585938)

        for j in range(256):
            x = dectobin(256 - j - 1)
            for k in range(8):
                GPIO.output(dac[k], x[k])
            time.sleep(0.00585938)

finally:
    for i in dac:
        GPIO.output(dac, 0)
    GPIO.cleanup()
