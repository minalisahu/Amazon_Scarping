# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Define the URL of the Amazon website
url = "https://www.amazon.in/ref=nav_logo"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL in the Chrome browser
driver.get(url)

# Find the search bar input field using XPath
searchbar_input = driver.find_element("xpath","//input[@id='twotabsearchtextbox']")

# Type "bluetooth headset" into the search bar
searchbar_input.send_keys("bluetooth headset")

# Press Enter to submit the search query
searchbar_input.send_keys(Keys.ENTER)

# Print the current URL after performing the search
print(f"{driver.current_url=}")

# Wait for the search results to load by waiting for the presence of all search result products
products = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))

# Loop through each search result product
for product in products:
    # Check if the product is sponsored or not
    print("Sponsored:",True if "Sponsored" in products[0].text else False)

    # Extract and print the product name
    name = product.find_elements(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')[0].text
    print("Product Name:", name)

    # Extract and print the price
    price = product.find_elements(By.XPATH,'.//span[@class="a-price-whole"]')[0].text
    print("Price:",price)

    # Extract and print the ASIN (Amazon Standard Identification Number)
    data_asin = product.get_attribute("data-asin")
    print("ASIN:",data_asin)

    # Print a separator for clarity
    print("-"*80)
    
# Quit the WebDriver to close the browser window    
driver.quit()


# Installement Cammands 
# python3 --version
# python3 -m pip install selenium
# python3 -m venv path/to/venv
# source path/to/venv/bin/activate
# pip install selenium

# Run 
# python3 -main.py