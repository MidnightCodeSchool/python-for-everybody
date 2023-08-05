# Calculate BMI
weight = input("น้ำหนักของคุณเท่าไหร่? (kg) ")
height = input("ส่วนสูงของคุณเท่าไหร่? (cm) ")
weight = int(weight)
height = int(height)
height = height / 100
bmi = weight / height ** 2
print("ค่า BMI ของคุณคือ " + str(bmi))
