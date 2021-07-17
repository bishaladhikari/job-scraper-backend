from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin(origin='*')
def url(title, location):
    return 'https://www.linkedin.com/jobs/search?keywords=' + title + '&location=' + location + '&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

email = 'kolibew407@ovooovo.com'
password = 'actioncut98130'



@app.route("/hello")
def hello():
    return "Hello, World! aws"


@app.route("/login")
def login():
    driver.get("https://www.linkedin.com")
    driver.find_element_by_id('session_key').send_keys(email)
    el = driver.find_element_by_id('session_password')
    el.send_keys(password)
    el.send_keys(Keys.ENTER)
    return 'logged'


@app.route("/pin/<code>", methods=['GET', 'POST'])
def scraper(code):
    el = driver.find_element_by_id('input__email_verification_pin')
    el.send_keys(code)
    el.send_keys(Keys.ENTER)
    return 'done'

app.run(debug=True)
