from tensorflow import keras
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np


def generate_samples_using_trained_model(model, n_samples=1000):
    noise = np.random.normal(0, 1, size=(n_samples, 10))
    return model.predict(noise)

def load_real_data(filename):
    with open(filename, 'r') as infile:
        return [float(line.strip()) for line in infile]

trained_generator = load_model('./25oct/models/gan_model.keras')

generated_samples = generate_samples_using_trained_model(trained_generator, n_samples=1000)
real_data = load_real_data('./25oct/random_numbers.txt')

print(f'Generated Mean: {generated_samples.mean()}')
print(f'Generated Min: {generated_samples.min()}')
print(f'Generated Max: {generated_samples.max()}')
print('-'*80)
print(f'Real Mean: {sum(real_data)/len(real_data)}')
print(f'Real Min: {min(real_data)}')
print(f'Real Max: {max(real_data)}')

# Sort the data
sorted_data = np.sort(generated_samples)

# Create an array of y values ranging from 0 to 1, with the same length as the sorted data
y_values = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# Plot the CDF
plt.plot(sorted_data, y_values, marker='.', linestyle='none')
plt.xlabel('Value')
plt.ylabel('CDF')
plt.title(f'Cumulative Distribution Function')
plt.grid(True)
plt.show()



