import RPi.GPIO as GP
import time
import random 

GP.setwarnings(False)
GP.setmode(GP.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
# num = [0, 1, 0, 0, 0, 0, 1, 0]
# num = [1] * len(dac)
num = [0, 0, 0, 0, 0, 1, 0, 1]
# for i in range(8 - len(num)):
#     num.append(1)

# for i in range(len(num)):
#     num[i] *= random.randint(0, 1)

for i in range(len(num)):
    GP.setup(dac[i], GP.OUT)

for i in range(len(num)):
    GP.output(dac[i], num[i])

time.sleep(15)

for i in dac:
    GP.output(i, 0)

