# ทำงานทุก ~10 วินาที
import time
from time import sleep
from datetime import datetime

def job():
    print("I'm working...")

count = 0
while True:
    now = time.time()
    if int(now) % 5 == 0:
        job()
        count += 1
    print(f"I worked {count} times")
    sleep(0.1) # หน่วงเวลา 10 วินาที