from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

def build_generator(input_dim=10):
    model = Sequential()

    # Input layer
    model.add(Dense(32, activation='relu', input_dim=input_dim))

    # Hidden layers
    model.add(Dense(64, activation='relu'))
    model.add(Dense(128, activation='relu'))

    # Ouput layer
    model.add(Dense(1, activation='linear'))

    return model