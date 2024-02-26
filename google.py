from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from auth_data import PROFILE, CHROME_EXE_URL

def google_post():
    # options
    options = webdriver.ChromeOptions()
    options.add_argument(PROFILE)
    options.add_argument("--headless")
    options.binary_location = CHROME_EXE_URL

    url = 'https://www.google.ru/search?q=%D1%83%D1%84%D0%B0%D0%BD%D0%B5%D1%82&newwindow=1&sca_esv=730ffcc1e347e49a&tbm=nws&sxsrf=ACQVn0_oItw9-F2c-Hyiq4z4oYOZ4GYUBg:1708668166448&source=lnt&tbs=sbd:1&sa=X&ved=2ahUKEwiNl-b45MCEAxWIKRAIHcnGBQUQpwV6BAgCEBk&biw=1440&bih=760&dpr=1'

    driver = webdriver.Chrome(options=options)

    posts = []

    try:
        driver.maximize_window()
        driver.get(url=url)
        time.sleep(2)

        search_item = driver.find_element(By.ID, "search")
        all_element = search_item.find_elements(By.CLASS_NAME, "SoaBEf")
        time.sleep(2)

        for item in all_element:
            p = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            t = item.find_element(By.CLASS_NAME, "GI74Re.nDgy9d").text
            posts.append([t, p])

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    return posts
