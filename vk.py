from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from auth_data import PROFILE, CHROME_EXE_URL

def vk_post():
    # options
    options = webdriver.ChromeOptions()
    options.add_argument(PROFILE)
    options.binary_location = CHROME_EXE_URL

    url = 'https://vk.com/feed?c%5Ballow_dups%5D=1&c%5Bq%5D=%F3%F4%E0%ED%E5%F2&section=search'

    driver = webdriver.Chrome(options=options)

    posts = []

    try:
        driver.maximize_window()
        driver.get(url=url)
        time.sleep(2)

        button_time = driver.find_element(By.CLASS_NAME, "segmentation_control_option").click()
        time.sleep(2)

        item_pages = driver.find_element(By.ID, "feed_rows")
        items = item_pages.find_elements(By.CLASS_NAME, "feed_row")
        time.sleep(2)
        for post in items:
            p = post.find_element(By.CLASS_NAME, "PostHeaderSubtitle__link").get_attribute("href")
            t = post.find_element(By.CLASS_NAME, "wall_post_text")
            a = [t.text, p]
            posts.append(a)
        time.sleep(2)
        
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    
    return posts