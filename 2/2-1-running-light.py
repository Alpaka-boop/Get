import RPi.GPIO as GP
import time

GP.setwarnings(False)
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GP.setmode(GP.BCM)

for x in leds:
    GP.setup(x, GP.OUT)

for i in range(3):
    for x in leds:
        GP.output(x, 1)
        time.sleep(0.2)
        GP.output(x, 0)

for x in leds:
    GP.output(x, 0)

GP.cleanup()
