class Something:
    def __init__(self, data: dict):
        self.__dict__ = data

    def __str__(self):
        # str_rep = ''
        # for key, value in self.__dict__.items():
        #     str_rep += f'{key} = {value}, '
        # return str_rep
        return ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])
 

data_dict1 = {
    'a': 10,
    'b': 20,
    'name': 'One'
}
data_dict2 = {
    'c': 15,
    'd': 25,
    'name': 'Two'
}

s1 = Something(data_dict1)
s2 = Something(data_dict2)
print(s1)
print(s2)