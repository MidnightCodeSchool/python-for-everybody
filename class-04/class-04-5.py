# using time.time()

import time
from time import sleep

prev_time = 0
while True:
    now = time.time()
    print(now - prev_time)
    prev_time = now
    sleep(1)