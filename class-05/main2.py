from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from rich import inspect
from selenium.webdriver.chrome.service import Service

def price_to_float(price):
    """แปลงราคาจาก string เป็น float
    ตัดคำว่า "฿" ออก
    """
    price = price.replace("฿", "")
    price = float(price)

    return price


url = "https://www.lazada.co.th/"
# xpath = "/html/body/div[4]/div/div[3]/div[2]/div/div[1]/div[8]/div/div/span"
search_field_xpath = "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]"

service = Service('/Users/m/Projects/python-for-everybody/class-05/chromedriver')
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(10)
try:
    driver.get(url)
except Exception:
    pass
search_field = driver.find_element(By.XPATH, search_field_xpath)
search_field.send_keys("กระเป๋า")
search_field.submit()
sleep(15)
els = driver.find_elements(By.CLASS_NAME, "ooOxS")

prices = []
for el in els:
    price = price_to_float(el.text)
    prices.append(price)


max_price = max(prices)
min_price = min(prices)
average_price = sum(prices) / len(prices)
print(f"max: {max_price}")
print(f"min: {min_price}")
print(f"average: {average_price}")

# el = driver.find_element(By.XPATH, xpath)
# price_text = el.text
# price_text = price_text.replace("฿", "")
# price = float(price_text)
# driver.close()
driver.close()