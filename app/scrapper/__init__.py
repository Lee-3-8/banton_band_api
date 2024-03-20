from selenium import webdriver
from dotenv import dotenv_values

options = webdriver.ChromeOptions()
# headless option
options.add_argument('headless')
options.add_argument("no-sandbox")

# window size
options.add_argument('window-size=1920x1080')

# fake options
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# driver load
chromeDriver = webdriver.Chrome(options=options)

# secret, config load
config = dotenv_values(".env")
