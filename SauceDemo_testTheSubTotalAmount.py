#===================================================================================
# Assert that The Subtotal price should be equal as the sum of item prices selected
# https://www.saucedemo.com/
#===================================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.saucedemo.com/")


# Login Page , do login with standart user
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Inventory page, add 2 productos into the cart and go to the cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "shopping_cart_container").click()

#Cart page => do the checkout
driver.find_element(By.ID, "checkout").click()


# Checkout StepcOne Page, enter name, surname and zip and continue
driver.find_element(By.ID, "first-name").send_keys("Klajdi is stupid")
driver.find_element(By.ID, "last-name").send_keys("and you know it")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Checkout Step One Page, check that subtotal amout is equal as the sum of item prices
listElem =  driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-price']")
sumOfPrices = float()
for item in listElem:
   price =  float(item.text.split("$")[1])
   sumOfPrices = sumOfPrices + price

print("Sum of Item Prices ",sumOfPrices)

priceSubTotal =  float(driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text.split("$")[1])
print("Subtotal Price",priceSubTotal)


# Assert that The Subtotal price should be equal as the sum of item prices
assert sumOfPrices == priceSubTotal,"The Subtotal price should be equal as the sum of item prices" 

# Close the browser
driver.quit()