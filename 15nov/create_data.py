from mongeasy import create_document_class
import datetime


Temps = create_document_class('Temps', 'temps')

temps = [float(value) for value in open('./15nov/temps.txt', 'r').read().split()]
date = datetime.datetime(2023, 1, 1, 0, 0, 0)

for temp in temps:
    data = {
        'date': date.strftime('%Y-%m-%d'),
        'time': date.strftime('%H:%M:%S'),
        'temperature': temp
    }

    temp_data = Temps(data)
    temp_data.save()

    date += datetime.timedelta(seconds=10)
