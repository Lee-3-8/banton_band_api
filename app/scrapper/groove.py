from . import chromeDriver, config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def get_status():

    chromeDriver.get(config['GROOVE_URL'])
    chromeDriver.switch_to.frame('main')
    chromeDriver.implicitly_wait(5)

    chromeDriver.find_element(by=By.LINK_TEXT, value='Reservation 사당').click()
    chromeDriver.implicitly_wait(5)

    chromeDriver.find_element(by=By.ID, value='login_id').send_keys(
        config['GROOVE_ID'])
    chromeDriver.find_element(by=By.ID, value='login_pw').send_keys(
        config['GROOVE_PWD'])
    # chromeDriver.find_element(by=By.CLASS_NAME, value='login_box').find_element(
    #     by=By.TAG_NAME, value='span').find_element(
    #     by=By.TAG_NAME, value='input').click()
# chromeDriver.find_element(locate_with(By.TAG_NAME, "input").near({By.ID: "login_pw"})).click()
    chromeDriver.find_element(locate_with(By.TAG_NAME, "span").to_right_of(
        {By.ID: "login_pw"})).click()
    chromeDriver.implicitly_wait(5)

    # login_button = chromeDriver.find_element(By.LINK_TEXT, 'Login')
    # login_button = chromeDriver.find_element(By.CLASS_NAME, 'util_w')
    # login_button.click()
    # print(login_button)
    # chromeDriver.implicitly_wait(5)

    chromeDriver.get_screenshot_as_file('groove4.png')    # capture

    return
