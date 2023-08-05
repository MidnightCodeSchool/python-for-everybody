# Calculate BMI
weight = input("น้ำหนักของคุณเท่าไหร่? (kg) ")
height = input("ส่วนสูงของคุณเท่าไหร่? (cm) ")
weight = float(weight)
height = float(height)
height = height / 100
bmi = weight / height ** 2
print("ค่า BMI ของคุณคือ " + str(bmi))
