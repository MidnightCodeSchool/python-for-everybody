import streamlit as st
import random

st.title("แดชบอร์ดของฉัน")
st.caption("อันนี้เอาไว้แสดงอะไรดี")

age = st.text_input("อายุของคุณ", 20)
# height = st.text_input("ส่วนสูงของคุณ", 170)
height = st.slider("ส่วนสูงของคุณ (cm)", 100, 200, 170)
# weight = st.text_input("น้ำหนักของคุณ", 70)
weight = st.slider("น้ำหนักของคุณ (kg)", 40, 150, 70)
# weight = st.number_input("น้ำหนักของคุณ", 40, 150, 70)


if st.button("คำนวณ"):
    bmi = float(weight) / ((float(height) / 100) ** 2)
    st.write("ค่า BMI ของคุณคือ", bmi)

# st.metric("อุณหภูมิในบ้าน", 35, 1)
# st.metric("อุณหภูมินอกบ้านบ้าน", 35, -1)



# เขียนบนหน้าจอ
# st.write("Hello world2222")
# v_dict = {"a": "b"}
# v_num = random.randint(1, 10)
# v_list = [1, 2, 3, 4, 5]
# st.write(v_dict)
# st.write(v_num)
# st.write(v_list)