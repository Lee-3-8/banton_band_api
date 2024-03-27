from . import chromeDriver, config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_reservation_info():

    chromeDriver.get(config['GROOVE_URL'])
    chromeDriver.switch_to.frame('main')
    chromeDriver.implicitly_wait(5)

    chromeDriver.find_element(by=By.LINK_TEXT, value='Reservation 사당').click()
    chromeDriver.implicitly_wait(5)

    chromeDriver.find_element(by=By.ID, value='login_id').send_keys(
        config['GROOVE_ID'])
    chromeDriver.find_element(by=By.ID, value='login_pw').send_keys(
        config['GROOVE_PWD'])
    chromeDriver.find_element(
        by=By.XPATH, value='//*[@id="sc_zone"]/div/div/div[2]/div/div/div/div[2]/form/div/div/div[1]/span/input').click()
    chromeDriver.find_element(
        by=By.XPATH, value='//*[@id="sc_zone"]/div/div/div[2]/div/div/div/div[2]/form/div/div/div[1]/span/input').click()

    # 로그인 클릭이 안된다... 도움 도움!

    chromeDriver.implicitly_wait(10)

    chromeDriver.get_screenshot_as_file('groove4.png')    # captsure

    return
