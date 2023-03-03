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


from selenium import webdriver
from selenium.webdriver.common.by import By


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


    driver.get("https://www.imdb.com/what-to-watch/popular/?ref_=watch_fanfav_tab")

    allMovieCardElements = driver.find_elements(By.CLASS_NAME, 'ipc-poster-card')

    movies = []

    for movieCard in allMovieCardElements:
        rating = movieCard.find_element(By.CLASS_NAME, 'ipc-rating-star').text
        name = movieCard.find_element(By.CLASS_NAME, 'ipc-poster-card__title').text
        url = movieCard.find_element(By.CLASS_NAME, 'ipc-poster-card__title').get_attribute('href')
        movies.append({
            'rating': rating,
            'name': name,
            'url': url
            })
        
    for movieInfo in movies:
        driver.get(movieInfo['url'])
        metadata = driver.find_element(By.XPATH, "//ul[@data-testid='hero-title-block__metadata']").text
        movieInfo['metadata'] = metadata.split('\n')
        del movieInfo['url']

except Exception as error:
    print("There was an error: %s" % error)

finally:
    driver.quit()

print(movies)
