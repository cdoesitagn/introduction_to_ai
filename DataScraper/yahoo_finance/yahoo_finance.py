import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()
url = "https://finance.yahoo.com/topic/stock-market-news/"

# Navigate to the web page
driver.get(url)

# Scroll down the page to load content
scroll_pause_time = 2  # Adjust as needed
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 10);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight * 10")
    if new_height == last_height:
        break
    last_height = new_height

# Wait for the desired element to become visible
wait = WebDriverWait(driver, 30)
element = wait.until(EC.presence_of_element_located((By.ID, 'Fin-Stream')))

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the element containing the headlines
div = soup.find(id='Fin-Stream')
a_tags = div.find_all('a')

# Extract headlines and print them
headlines = [a.text for a in a_tags if len(a.text) > 2]
if "" in headlines or " " in headlines:
    print("Yes")

pd.DataFrame(headlines).to_csv("data/yahoo_finance_headlines.csv")
# Quit the WebDriver
driver.quit()
