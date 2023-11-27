import requests

page = requests.get('https://time-time.net/timer/digital-clock.php')

with open('digital_clock.html', 'w') as f:
    f.write(page.text)