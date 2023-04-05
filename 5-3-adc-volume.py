import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24,25,8,7,12,16,20,21]
comp = 4
troyka = 17
levels = 2 ** len(dac)
maxV = 3.3

GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)
for i in leds:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def dectobin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]


def adc():
    for i in range(256):
        x = dectobin(i)
        GPIO.output(dac, x)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            GPIO.output(dac, 0)
            return i
    return 256

def newadc():
    l = 0
    r = 255
    while r - l > 1:
        i = (r + l) // 2
        GPIO.output(dac, dectobin(i))
        time.sleep(0.001)
        if not(GPIO.input(comp)):
            r = i
        else:
            l = i

    return r

try:
    while (True):
        v = newadc()
        n = v // 32
        # n = min(8, n)
        GPIO.output(leds, [1] * n + [0] * (8 - n))


finally:
    for i in dac:
        GPIO.output(dac, 0)
    GPIO.cleanup()

