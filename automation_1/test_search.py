from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(1)
driver.maximize_window()
time.sleep(1)
print(driver.title)

search = driver.find_element(By. XPATH, "//input[@type = 'search']").send_keys("ca")
time.sleep(2)
driver.execute_script("window.scrollBy(0,100);")

product_name = driver.find_elements(By.XPATH, "//div//h4")
for name in product_name:
  text = name.text.lower()
  print(text)

assert "ca" in text
print("Test passed")  