import secrets

def generate_secure_random_numbers(n=1000):
    max_value = 1 << 64  # Use 64 bits for precision
    return [secrets.randbelow(max_value) / max_value for _ in range(n)]

def save_to_file(filename, data):
    with open(filename, 'w') as out_file:
        for value in data:
            out_file.write(str(value) + '\n')

random_numbers = generate_secure_random_numbers()
save_to_file('./23oct/data/random_numbers.txt', random_numbers)