from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

CHROME_EXE_URL = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PROFILE = r'C:\Users\kureed\AppData\Local\Google\Chrome\User Data'

def tg_post():
    # options
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + PROFILE)
    options.binary_location = CHROME_EXE_URL

    url = 'https://tgstat.ru/search'

    driver = webdriver.Chrome(options=options)

    posts = []

    try:
        driver.maximize_window()
        driver.get(url=url)
        time.sleep(2)

        search_post = driver.find_element(By.CLASS_NAME, "form-control.form-control-lg")
        search_post.send_keys('уфанет')
        search_post.send_keys(Keys.ENTER)
        time.sleep(2)

        bar_news = driver.find_element(By.CLASS_NAME, "posts-list.lm-list-container")
        uri = bar_news.find_elements(By.CLASS_NAME, "dropdown.mt-1.mr-2.mr-sm-0.float-right.text-muted")
        texts = bar_news.find_elements(By.CLASS_NAME, "row.my-2")
        for i in range(len(uri)):
            p = uri[i].find_element(By.CLASS_NAME, "dropdown-menu.dropdown-menu-right")
            t = texts[i].find_element(By.CLASS_NAME, "post-text").text
            posts.append([t, str(p.find_element(By.TAG_NAME, "a").get_attribute("href")).replace("ttttt", "t")])

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    
    return posts