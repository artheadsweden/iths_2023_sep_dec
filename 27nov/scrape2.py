import requests_html
from bs4 import BeautifulSoup

session = requests_html.HTMLSession()

page = session.get('https://time-time.net/timer/digital-clock.php')

page.html.render()

if page.ok:
    html = page.html.html
    soup = BeautifulSoup(html, 'html.parser')
    current_time = soup.find('div', id='timenow')
    print(current_time.text)
    # with open('digital_clock.html', 'w') as f:
    #     f.write(page.html.html)