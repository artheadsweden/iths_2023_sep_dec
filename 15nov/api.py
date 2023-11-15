from flask import Flask, request
import json
from mongeasy import create_document_class
import pickle
import numpy as np

class KNNClassifier:
    def __init__(self, k=5):
        self.k = k
        self.X = None
        self.y = None

    def _calculate_distance(self, x1, x2):
        """
        Calculate the Eucledian distance between two data points, x1 and x2
        """
        return ((x1 - x2)**2).sum() ** 0.5

    def _knn_predict(self, x):
        return sorted([
            (self._calculate_distance(x, measurment), self.y[i])
            for i, measurment in enumerate(self.X)
        ])[:self.k]

    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)

    def _predict(self, neighbors):
        labels = [n[1] for n in neighbors]
        label, count = np.unique(labels, return_counts=True)
        max_count = np.max(count)
        if np.sum(count == max_count) > 1:
            tied_labels = label[count == max_count]
            return min(tied_labels, key=labels.index)

        return label[np.argmax(count)]

    def predict(self, X):
        # X = [(178, 86), (164, 52)]
        predictions = []
        for x in X:
            neighbors = self._knn_predict(x)
            prediction = self._predict(neighbors)
            predictions.append(prediction)
            
        return predictions

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'name': 'John Doe',
        'age': 34
    }
    return json.dumps(data)

@app.post('/temps')
def temps_post():
    in_data = request.get_json()
    Temp = create_document_class('Temp', 'temps')

    temp = Temp.find(in_data).first()
    if temp is None:
        return "This date and time does not have a temp"
    return temp.to_json()

@app.post('/size')
def post_size():
    in_data = request.get_json()
    model = pickle.load(open('./15nov/knn.pkl', 'rb'))
    height = int(in_data['height'])
    weight = int(in_data['weight'])
    prediction = model.predict([(height, weight)])
    return f'Your predicted t-shirt size is {prediction[0]}'


app.run(debug=True)