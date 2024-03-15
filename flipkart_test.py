from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver instance
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.flipkart.com")

# Search for the product
search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Samsung Galaxy S10")
search_box.submit()

# Apply filters
brand_filter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@title='SAMSUNG']")))
brand_filter.click()

# Wait for assurance filter to appear
flipkart_assured_filter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_24_Dny _3tCU7L']")))

# Click on the flipkart assured filter
flipkart_assured_filter.click()

# Sort by Price - High to Low
sort_by_price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Price -- High to Low']")))
sort_by_price.click()

# Wait for results to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "_1AtVbE")))

# Get product information
product_names = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
prices = driver.find_elements(By.CLASS_NAME, "_30jeq3")
product_links = driver.find_elements(By.CLASS_NAME, "_1fQZEK")


driver.quit()
