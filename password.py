import random
import string

def generate_password(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    password = ''.join(random.choice(letters + numbers + symbols) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Ingrese la longitud de la contraseña: "))
    password = generate_password(length)
    print("Su contraseña aleatoria es: ", password)
