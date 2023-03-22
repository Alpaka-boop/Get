import RPi.GPIO as GP

GP.setwarnings(False)
GP.setmode(GP.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux  = [22, 23, 27, 18, 15, 14, 3, 2]

for x in leds:
    GP.setup(x, GP.OUT)

for x in aux:
    GP.setup(x, GP.IN)

GP.cleanup()
# while (1):
#     for i in range(len(leds)):
#         GP.output(leds[i], GP.input(aux[i]))

