from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### load selenium driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('[크롬 드라이버 경로 입력]',options=options)
driver.set_window_size(1920, 1080)

url="https://www.google.com/search?q=[##URL인코딩된 검색어 입력##]+site:linkedin.com/in&newwindow=1&start="
## url_sample="https://www.google.com/search?q=  %22구글%22+OR+%22google%22+-%22오탐인+회사명%22  +site:linkedin.com/in&newwindow=1&start="

x = 9
page_url=url + str(x)

driver.get(page_url)
sleep(1)

y = 1
str_y = str(y)
xpath_front = '//*[@id="rso"]/div['
xpath_back_user = ']/div/div/div[1]/div/a/h3'
xpath_back_url = ']/div/div/div[1]/div/a'

xpath_user = xpath_front + str_y + xpath_back_user
xpath_url = xpath_front + str_y + xpath_back_url


### get username and password input boxes path
linked_user = driver.find_element("xpath", xpath_user)
linkedin_url = driver.find_element("xpath", xpath_url)

get_link = linkedin_url.get_attribute('href')

print(linked_user.text)
print(get_link)
