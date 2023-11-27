import requests_html
from bs4 import BeautifulSoup
import time
import datetime

url = 'https://www.avanza.se/marknadsoversikt.html'
energy_oid = '334578'

with open('./27nov/data/energy_data.csv', 'w') as csv_file:
    csv_file.write('date,time,last_price,change_percent\n')

session = requests_html.HTMLSession()

for i in range(10):
    page_data = session.get(url)
    page_data.html.render()

    if page_data.ok:
        html = page_data.html.html
        soup = BeautifulSoup(html, 'html.parser')
        # Find the <tr> we are interested in
        tr = soup.find('tr', {'data-oid': energy_oid, 'data-delayed': 'true'})
        
        # Get the change percent
        change_percent = tr.find('td', {'class': 'changePercent'}).text.strip()
        change_percent = change_percent.replace(',', '.')
        change_percent = float(change_percent)

        # Get last price
        last_price = tr.find('td', {'class': 'lastPrice'}).text.strip()
        last_price = last_price.replace('\xa0', '').replace(',', '.')
        last_price = float(last_price)

        # Get the last updated time
        updated = tr.find('td', {'class': 'updated'}).text.strip()

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        with open('./27nov/data/energy_data.csv', 'a') as csv_file:
            csv_file.write(f'{current_date},{updated},{last_price},{change_percent}\n')

        print(f'Done with iteration {i + 1}')
        if i == 9:
            print('Done scraping')
            break
        time.sleep(60)
    else:
        break