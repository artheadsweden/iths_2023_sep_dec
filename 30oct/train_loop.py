import tensorflow as tf
from tensorflow import keras
from keras.optimizers import Adam
from discriminator import build_discriminator
from generator import build_generator
import numpy as np
import matplotlib.pyplot as plt


def load_real_data(filename):
    with open(filename, 'r') as infile:
        return [float(line.strip()) for line in infile]


def generate_fake_samples(generator, n_samples):
    # Generate random noise
    noise = np.random.normal(0, 1, (n_samples, 10))
    # Generate fake data
    return generator.predict(noise)

def plot_data(real_data, fake_data):
    plt.figure(figsize=(12, 6))
    plt.hist(real_data, bins=30, alpha=0.5, label='Real Data')
    plt.hist(fake_data, bins=30, alpha=0.5, label='Fake Data')
    plt.legend()
    plt.show()

def custom_mse_with_weighted_penalty(y_true, y_pred, alpha=1.0):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))

    penalty = tf.reduce_mean(tf.where(y_pred < 0, -y_pred, 0)) + tf.reduce_mean(tf.where(y_pred > 1, y_pred -1, 0))

    return mse + alpha * penalty

def train_gan(generator, discriminator, gan_model, real_data, epochs=1000, batch_size=128, visualize=False):
    half_batch = batch_size // 2

    for epoch in range(epochs):
        # Train discriminator
        # Select a random half batch of real data
        idx = np.random.randint(0, len(real_data), half_batch)
        real_samples = np.array([real_data[i] for i in idx])

        # Generate a half batch of fake data
        fake_samples = generate_fake_samples(generator, half_batch)

        real_labels = np.ones((half_batch, 1))
        fake_labels = np.zeros((half_batch, 1))

        # Train the discriminator
        d_loss_real = discriminator.train_on_batch(real_samples, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_samples, fake_labels)

        # Train the generator
        noise = np.random.normal(0, 1, (batch_size, 10))
        valid_labels = np.ones((batch_size, 1))
        g_loss = gan_model.train_on_batch(noise, valid_labels)

        print(f'Epoch: {epoch+1}/{epochs}, D Loss Real: {d_loss_real}, D Loss Fake: {d_loss_fake}, G Loss: {g_loss}')

        if epoch % 1000 == 0:
            generator.save(f'generator_model_{epoch}.keras')

    if visualize:
        plot_data(real_data, fake_samples)

def create_gan_model(alpha=2.0, descrimiator_lr=0.0001, generator_lr=0.0001, epochs=1000, save_model=False, model_path='./30oct/models/gan_model.keras'):
    
    discriminator_optimizer = Adam(learning_rate=descrimiator_lr)
    generator_optimizer = Adam(learning_rate=generator_lr)
    discriminator = build_discriminator(optimizer=discriminator_optimizer)

    generator = build_generator()

    # Build combined GAN model
    initial_noise = tf.keras.Input(shape=(10,))
    initial_fake = generator(initial_noise)
    discriminator.trainable = False
    validity = discriminator(initial_fake)
    gan_model = tf.keras.Model(initial_noise, validity)

    loss_function = lambda y_true, y_pred: custom_mse_with_weighted_penalty(y_true, y_pred, alpha=alpha)

    gan_model.compile(optimizer=generator_optimizer, loss=loss_function, metrics=['accuracy'])

    real_data = load_real_data('./30oct/random_numbers.txt')

    # Train GAN
    train_gan(generator, discriminator, gan_model, real_data, epochs=epochs, visualize=False)

    if save_model:
        print(f'Saving model {model_path}')
        generator.save(model_path)

create_gan_model(epochs=10_000, alpha=2.3, save_model=True, model_path='./30oct/models/gan_model_new.keras')