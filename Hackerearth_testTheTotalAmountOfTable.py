from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()
expectedTotalPrices= float(251.00)

# Open a website
driver.get("https://the-internet.hackerearth.com")

driver.find_element(By.XPATH, "//div[@id='content']//a[@href='/tables']").click()
listPrices = driver.find_elements(By.XPATH, "//table[@id='table1']//tr/td[4]")

currentTotalPrices = float()
for price in listPrices:
    eachPrice = float(price.text.removeprefix("$"))
    print("Each price => ",eachPrice)
    currentTotalPrices += eachPrice

print("Current Total price => ",currentTotalPrices)
print("Expected Total price => ",expectedTotalPrices)

# Assert that The Subtotal price should be equal as the sum of item prices
assert expectedTotalPrices == currentTotalPrices,"The current total prices should be equal as expected price" 