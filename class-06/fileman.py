import os
import shutil
from pathlib import Path
import send2trash

# สร้างโฟลเดอร์
os.mkdir('test')

# ดูว่าว่ามีโฟลเดอร์/ไฟล์อะไรบ้าง
os.listdir()

# หา home folder
Path.home()

# join path
os.path.join(Path.home(), 'test')

# copy file
shutil.copy('test.txt', 'test2.txt')

# เปลี่ยนชื่อ หรือ ย้ายที่
shutil.move('test2.txt', 'test3.txt')
os.mkdir('move')
shutil.move('test3.txt', os.path.join('move', 'test3.txt'))

# ลบไฟล์ (ส่งเข้าถังขยะ)
send2trash.send2trash('test.txt')