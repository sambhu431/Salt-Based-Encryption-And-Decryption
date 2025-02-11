import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def save_salt(salt, file_name):
    with open(file_name, "wb") as salt_file:
        salt_file.write(salt)


def load_salt(file_name):
    with open(file_name, "rb") as salt_file:
        return salt_file.read()

def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)


if __name__ == "__main__":
    folder_path = "Images/Encrypted_Images"
    salt_file = "common_salt/saltImages.salt"

    # Prompt user for a password
    password = "password"

    # Check if the salt file exists or create a new one
    if not os.path.exists(salt_file):
        salt = os.urandom(16)
        save_salt(salt, salt_file)
        print(f"New salt generated and saved to '{salt_file}'.")
    else:
        salt = load_salt(salt_file)
        print(f"Salt loaded from '{salt_file}'.")

    # Derive the encryption key from the password
    key = derive_key_from_password(password, salt)
    
    
decrypt_folder(folder_path, key)
print(f"Folder '{folder_path}' has been decrypted.")

        