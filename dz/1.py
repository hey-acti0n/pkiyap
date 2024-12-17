from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
def pars():
    url = "https://music.yandex.ru/users/alexemel2/playlists/3"


    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome()


    try:
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(3)
        cancel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[22]/div/span").click()



        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        with open("/Users/acti0n/Documents/proga/dz/pars_code_YANDEX_music.html", "w") as file:
            file.write(driver.page_source)


    

        time.sleep(50)
    except Exception as ex:
        print(ex)
    finally:
            driver.close()
            driver.quit()

pars()