"""from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')

url="https://us.ecco.com/men/shoes/"

time.sleep(4)

soup=BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

books=list()
k={}

try:
    Title = soup.find_all("div", {"class":"product-detail-name"})
except:
    Title = None

try:
    Price = soup.find_all("span", {"class":"price display-inline-block arrange-fit price price-main"})
except:
    Price = None

for i in range(0 , len(Title)):
    try:
        k["Title{}".format(i+1)] =  Title[i].find("span").text
    except:
        k["Title{}".format(i+1)] = None


    try:
        k["Price{}".format(i+1)] = Price[i].find("div", {"class", "price-standard plp-tile"}).find("span",{"class":"value"}).text
    except:
        k["Price{}".format(i+1)]=None

        books.append(k)

        k={}
"""

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import json

BROWSERLESS_API_KEY = "414d772d-f0ae-4d12-bc75-6611a52ed83e"

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', BROWSERLESS_API_KEY)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
try:
    driver = webdriver.Remote(
        command_executor='https://chrome.browserless.io/webdriver',
        options=chrome_options 
    )
    driver.get("https://www.adidas.com/us/men-new_arrivals")
    allProductCardElements = driver.find_elements(By.CLASS_NAME, 'glass-product-card')
    products = []
    # productstemp = []
    for productCardTemp in allProductCardElements:
        infoUrl = productCardTemp.find_element(By.CLASS_NAME, 'glass-product-card__assets').find_element(By.CLASS_NAME, 'glass-product-card__assets-link').get_attribute('href')
        imgUrl = productCardTemp.find_element(By.CLASS_NAME, 'glass-product-card__assets').find_element(By.CLASS_NAME, 'glass-product-card__image').get_attribute('src')
        imgUrlHover = productCardTemp.find_element(By.CLASS_NAME, 'glass-product-card__assets').find_element(By.CLASS_NAME, 'glass-product-card__image-hover').get_attribute('src')
        # price = productCardTemp.find_element(By.CLASS_NAME, 'glass-product-card__assets').find_element(By.CLASS_NAME, 'product-card-content-badges-wrapper___2RWqS').find_element(By.CLASS_NAME, 'badge-container___1TJjk').find_element(By.CLASS_NAME, 'gl-price--inline___3nMlh').find_element(By.CLASS_NAME, 'gl-price-item').text
        products.append({
            'infoUrl': infoUrl,
            'imgUrl': imgUrl,
            'imgUrlHover': imgUrlHover,
            })
    for productsInfo in products:
        driver.get(productsInfo['infoUrl'])
        category = driver.find_element(By.CLASS_NAME, "sidebar-wrapper___3uF26").find_element(By.CLASS_NAME, 'sidebar___29cCJ').find_element(By.CLASS_NAME, 'product-description___1TLpA').find_element(By.CLASS_NAME, 'pre-header___3bx4D')[0].text
        product_title = driver.find_element(By.CLASS_NAME, "sidebar-wrapper___3uF26").find_element(By.CLASS_NAME, 'sidebar___29cCJ').find_element(By.CLASS_NAME, 'product-description___1TLpA').find_element(By.CLASS_NAME, 'name___120FN').text
        price = driver.find_element(By.CLASS_NAME, "sidebar-wrapper___3uF26").find_element(By.CLASS_NAME, 'sidebar___29cCJ').find_element(By.CLASS_NAME, 'product-description___1TLpA').find_element(By.CLASS_NAME, 'product-price___2Mip5').find_element(By.CLASS_NAME, 'price___Z74_w').find_element(By.CLASS_NAME, 'price-wrapper___2Pj9R').text
        productsInfo['Info'] = {
            'product_title' : product_title,
            'product_category' : category,
            'price' : price,
        }
        del productsInfo['infoUrl']
except Exception as error:
    print("There was an error: %s" % error)

finally:
    driver.quit()
print(products)

