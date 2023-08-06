# Calculate area of a circle

PI = 3.141

radius = input("Enter radius: ")  # มี type เป็น str เสมอ จะต้องเปลี่ยนเป็นค่าที่เราใช้ได้
radius = float(radius)
area = PI * radius ** 2
print("Area of circle is: ", area)  # print สามารถรับ ค่า (object) ได้หลายตัว โดยใช้ , คั่น

