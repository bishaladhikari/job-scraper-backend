from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="C:\\Users\\Bishal\\Downloads\chromedriver_win32\\chromedriver.exe",options=options)

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





# import os
# import time
# from os import remove
# from shutil import move
# from flask import Flask, jsonify
# from flask import request
# from flask.helpers import send_file, send_from_directory
# from flask_cors import CORS, cross_origin
# import indeed_job_scraper
# from linkedin_job_scraper import Linkedin
# from decouple import config
# import gulftalent_job_scraper
#
#
# OUTPUT_DIR = config('OUTPUT_DIR', '')
#
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
#
#
# @app.route("/hello")
# def hello():
#     return "Hello, World! aws"
#
#
# @cross_origin(origin='*')
# @app.route("/", methods=['GET', 'POST'])
# def scraper():
#     domain = request.args.get('domain')
#     date_posted = request.args.get('date_posted')
#     title = request.args.get('title')
#     loc = request.args.get('loc')
#     if 'linkedin' in domain:
#         Linkedin.Scrape(title, loc, OUTPUT_DIR + 'results.xlsx', date_posted  )
#     elif 'indeed' in domain:
#         indeed_job_scraper.main("ae.indeed.com", date_posted, title, loc, OUTPUT_DIR + 'results.xlsx')
#     else:
#         gulftalent_job_scraper.main("gulftalent.com", date_posted, title, loc, OUTPUT_DIR + 'results.xlsx')
#     return download_file(title)
#
#
# def download_file(title):
#     # if os.path.exists('output/' + title + '.xlsx'):
#     #     remove('output/' + title + '.xlsx')
#     # move('output//var/www/html/flaskapp/results.xlsx', 'output/' + title + '.xlsx')
#     # time.sleep(1)
#     return send_file(OUTPUT_DIR + 'results.xlsx', as_attachment=True)
