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

search = driver.find_element(By. XPATH, "//input[@type = 'search']").send_keys("ap")
time.sleep(2)
driver.execute_script("window.scrollBy(0,100);")

list = []
list_2 = []

add_to_cart = driver.find_elements(By.XPATH, "//div[@class = 'product-action']")
for cart in add_to_cart:
#//div[@class = 'product-action'parent::div/p
  list.append(cart.find_element(By.XPATH,"parent::div/p").text)

#"//div[@class = 'product-action']/parent::div/h4"
  list_2.append(cart.find_element(By.XPATH,"parent::div/h4").text)
  cart.click()
# print(len(add_to_cart))
print("price of product", list)
print("Name of product",list_2)

time.sleep(1)
bag = driver.find_element(By.CSS_SELECTOR,'img[alt = "Cart"]').click()
time.sleep(1)

proceed_to_checkout = driver.find_element(By.XPATH,'//button[text() = "PROCEED TO CHECKOUT"]').click()
time.sleep(3)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_all_elements_located(driver.find_elements(By.CLASS_NAME,"p.product-name")))
# driver.execute_script("window.scrollBy(0,0);")

list_3 = []
product_name = driver.find_elements(By.CLASS_NAME, "product-name")
for product in product_name:
  text = product.text.strip()
  if text:
    list_3.append(text)
print("Products in cart", list_3)

assert list_2 == list_3
print("Test passed : All products are matching")


promo_text = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
time.sleep(2)

apply = driver.find_element(By.CLASS_NAME, 'promoBtn').click()
time.sleep(2)

originalAmount = driver.find_element(By.CLASS_NAME, "discountAmt").text
print("Original Amount:", originalAmount)

wait = WebDriverWait(driver,10)
promo_info = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
print(promo_info.text)
driver.execute_script("window.scrollBy(0, 100);")

discountAmount = driver.find_element(By.CLASS_NAME, "discountAmt").text
print("Discount Amount:", discountAmount)

assert float(discountAmount) < float(originalAmount)
print("Test passed : Discount applied successfully")

amounts = driver.find_elements(By.XPATH,'//tr//td[5]/p')
sum = 0
for amount in amounts:
  sum += int(amount.text)
print("Sum of all products:", sum)

total = int(driver.find_element(By.CLASS_NAME,'totAmt').text)
print("Total Amount: ", total)

assert sum == total
print("test passed")

place_order = driver.find_element(By.XPATH,'//button[text()= "Place Order"]').click()
time.sleep(3)

countries = Select(driver.find_element(By.XPATH,"//div[@class = 'wrapperTwo']//div//select"))

time.sleep(1)
countries.select_by_visible_text("India")

time.sleep(1)
check_box = driver.find_element(By.XPATH,'//input[@type = "checkbox"]').click()
time.sleep(1)

proceed = driver.find_element(By.XPATH,'//button[normalize-space()="Proceed"]').click()
time.sleep(1)

success_message = driver.find_element(By.XPATH,"//span[contains(text(), 'your order has been placed successfully')]")
print(success_message.text)

time.sleep(1)
driver.quit()