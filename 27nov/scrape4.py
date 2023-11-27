import requests_html
from bs4 import BeautifulSoup
import time
import datetime


def create_csv(filepath):
    with open(filepath, 'w') as csv_file:
        csv_file.write('date,time,last_price,change_percent\n')

def append_csv(filepath, data):
     with open(filepath, 'a') as csv_file:
            csv_file.write(data + '\n')

oids = [334578, 334593, 334580, 334584, 334586, 334591, 334581, 334577, 334603, 334597, 334602]
url = 'https://www.avanza.se/marknadsoversikt.html'

session = requests_html.HTMLSession()

# Get the branch names
page = session.get(url)
page.html.render()

if page.ok:
    for oid in oids:
            html = page.html.html
            soup = BeautifulSoup(html, 'html.parser')
            # Find the <tr> we are interested in
            tr = soup.find('tr', {'data-oid': oid, 'data-delayed': 'true'})
            branch = tr.find('a', {'class': 'link'}).text.strip()
            create_csv(f'./27nov/data/{branch}_data.csv')

    for i in range(10):
        page = session.get(url)
        page.html.render()

        if page.ok:
            for oid in oids:
                try:
                    html = page.html.html
                    soup = BeautifulSoup(html, 'html.parser')
                    # Find the <tr> we are interested in
                    tr = soup.find('tr', {'data-oid': oid, 'data-delayed': 'true'})

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

                    # Get current date
                    current_date = datetime.datetime.now().strftime('%Y-%m-%d')    
            
                    # Get branch name
                    branch = tr.find('a', {'class': 'link'}).text.strip()
                    append_csv(f'./27nov/data/{branch}_data.csv', f'{current_date},{updated},{last_price},{change_percent}')
                except Exception as e:
                    print(f'Error with iteration {i + 1}')
                    exit()

            print(f'Done with iteration {i + 1}')
            if i == 9:
                break  
            time.sleep(60)      


