import schedule
from time import sleep
import time

count = 0


def job():
    global count
    count += 1
    print(f"{int(time.time())} - I'm working...{count}")


schedule.every(3).seconds.do(job)


while True:
    schedule.run_pending()  # ถ้ามีงานค้างอยู่รันมันซะ
    sleep(1)
