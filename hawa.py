import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome( executable_path='C:/chrome_driver/chromedriver.exe',options=options)

def url(title, location):
    return 'https://www.linkedin.com/jobs/search?keywords=' + title + '&location=' + location + '&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

email = 'kawasotihero@gmail.com'
password = 'HP!65j.GKVXxe-?'

def login():
    driver.get("https://www.linkedin.com")
    driver.find_element_by_id('session_key').send_keys(email)
    el = driver.find_element_by_id('session_password')
    el.send_keys(password)
    el.send_keys(Keys.ENTER)
    print('logged' + driver.page_source)


def login_code(code):
    el = driver.find_element_by_id('input__email_verification_pin')
    el.send_keys(str(code))
    el.send_keys(Keys.ENTER)
    print('done')




login()
input = input('Inter Code: ')
login_code(input)


