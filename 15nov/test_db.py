from mongeasy import create_document_class

Temp = create_document_class('Temp', 'temps')

temp = Temp.find({'date': '2023-01-03', 'time': '12:23:10'}).first()

if temp is None:
    print('Did not find any data')
else:
    print(temp.date)
    print(temp.time)
    print(temp.temperature)
