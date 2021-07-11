import os
import time
from os import remove
from shutil import move
from flask import Flask, jsonify
from flask import request
from flask.helpers import send_file, send_from_directory
from flask_cors import CORS, cross_origin
import indeed_job_scraper
import linkedin_job_scraper
from decouple import config
import gulftalent_job_scraper


OUTPUT_DIR = config('OUTPUT_DIR', '')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/hello")
def hello():
    return "Hello, World! aws"


@cross_origin(origin='*')
@app.route("/", methods=['GET', 'POST'])
def scraper():
    domain = request.args.get('domain')
    date_posted = request.args.get('date_posted')
    title = request.args.get('title')
    loc = request.args.get('loc')
    if 'linkedin' in domain:
        linkedin_job_scraper.main("linkedin.com", date_posted, title, loc, OUTPUT_DIR + 'results.xlsx')
    elif 'indeed' in domain:
        indeed_job_scraper.main("ae.indeed.com", date_posted, title, loc, OUTPUT_DIR + 'results.xlsx')
    else:
        gulftalent_job_scraper.main("gulftalent.com", date_posted, title, loc, OUTPUT_DIR + 'results.xlsx')
    return download_file(title)


def download_file(title):
    # if os.path.exists('output/' + title + '.xlsx'):
    #     remove('output/' + title + '.xlsx')
    # move('output//var/www/html/flaskapp/results.xlsx', 'output/' + title + '.xlsx')
    # time.sleep(1)
    return send_file(OUTPUT_DIR + 'results.xlsx', as_attachment=True)
