import requests
from bs4 import BeautifulSoup as bs
s = requests.Session()
def url(title, location) :
  return 'https://www.linkedin.com/jobs/search?keywords=' + title +'&location='+ location +'&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

login_url = "https://www.linkedin.com/uas/login-submit"

main = requests.get('https://www.linkedin.com')
soup = bs(main.content, features="lxml").find_all('input', {'name': 'loginCsrfParam'})[0].get('value')
# print(soup)
payload = {
    'loginCsrfParam': soup,
    'session_key': 'kawasotihero@gmail.com',
    'session_password': 'HP!65j.GKVXxe-?',
    'trk': 'homepage-basic_signin-form_submit',
    'controlId': 'p_homepage-guest-home-homepage-basic_signin-form_submit-button',
    'pageInstance': 'urn:li:page:p_homepage-guest-home_jsbeacon;Ad+v/hmBQ+SmEx/OyW3Bmw=='
}
login = s.post(login_url , payload, headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
})
# print(login.cookies)


print(url('developer', 'Nepal'))
resp = s.get(url('developer', 'Nepal'))
cards = bs(resp.content, features="lxml").find('ul', {'class' : 'jobs-search__results-list'})
# print(bs(resp.content, features="lxml").prettify())
# print(bs(resp.content).prettify())
print(cards)




