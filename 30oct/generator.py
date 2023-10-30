from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, LeakyReLU

# def build_generator(input_dim=10):
#     model = Sequential()

#     # Input layer
#     model.add(Dense(32, activation='relu', input_dim=input_dim))

#     # Hidden layers
#     model.add(Dense(64, activation='relu'))
#     model.add(Dense(128, activation='relu'))

#     # Ouput layer
#     model.add(Dense(1, activation='linear'))

#     return model

def build_generator(input_dim=10):
    model = Sequential()

    # Input Layer
    model.add(Dense(32, input_dim=input_dim))

    # Hidden Layer
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(64))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(128))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))

    model.add(Dropout(0.5))

    # Output Layer
    model.add(Dense(1, activation='sigmoid'))

    return model