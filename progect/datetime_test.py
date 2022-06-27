from datetime import datetime
import imp
import sys
import math
from time import sleep

fmt = '%Y-%m-%d %H:%M:%S'
plot = [1, 23,23]
print(len(plot))
d1 = datetime.now()
sleep(61)
d2 = datetime.now()

daysDiff = (d2-d1).seconds

print(d1)
print(d2)
print((d2-d1).seconds)
# Convert days to minutes
minutesDiff = daysDiff / 60

print(math.floor(minutesDiff))