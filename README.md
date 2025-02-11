<h1> Salt Based Encryption And Decryption </h1>

# Overview
This Python script offers a comprehensive solution for encrypting and decrypting files and folders using password-based methods. It addresses the core concerns, insecurities, and hesitations that individuals and companies face when sharing files, folders, or personal data over the internet due to the risk of hacking, leakage, and theft. With this salt-based encryption method, you can securely encrypt your personal, confidential data, files, and folders.


# Features
- **Password-Based Key Derivation**: Derives an encryption key from a password using PBKDF2HMAC.
- **Salt Management**: Generates, saves, and loads a salt to add complexity to the encryption process.
- **File Encryption**: Encrypts individual files using the derived key and Fernet.
- **Folder Encryption**: Recursively encrypts all files within a specified folder.
- **Decryption**: Uses the same generated salt key to decrypt the files and folder.
- **Utilizing Same Salt Key**: The same salt key can be used to encrypt any number of files and folder rather than creating keys everything for each files and folder.

# Requirements
- Python 
- `cryptography` library

# Installation
To install the required library, run:
pip install cryptography

# Usage
Derive Key from Password
The function derive_key_from_password(password, salt) is used to derive an encryption key from the given password and salt.
The program can be used to encrypt and decrypt multiple files and folder just using a common salt key. It also can be used to create multiple salt keys for each files and folders.

# Save and Load Salt
- save_salt(salt, file_name): Saves the salt to a specified file.

- load_salt(file_name): Loads the salt from a specified file.

# Encrypt File
The function encrypt_file(file_path, key) encrypts a file with the derived key using Fernet.

# Decrypt File
The function decrypt_file(file_path, key) dencrypts a file with the derived key using Fernet.

# Acknowledgments
This script utilizes the cryptography library for secure key derivation , decryption and encryption.

# Contributions
Please Feel free to contribute to this project by submitting issues or pull requests. 

Any enhancements, bug fixes, or optimizations are extremely welcomed!

