# utils.py
import json
import os
from cryptography.fernet import Fernet

key_path = "key.data"

def write_file(file_path, data):
        # Takes data and writes it to the file_path in json format
        # Creates a new file if there isn't one yet
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)

def load_file(file_path):
        # Loads file_path file
    with open(file_path, "r") as json_file:
        return json.load(json_file)

def check_file(file_path):
        # Checks if file_path exists
        # If not then creates a file, and prepares it for json
        if os.path.isfile(file_path) == False:
                msg = {}
                write_file(file_path, msg)

def generate_key():
        # Generates secret encryption key
        if os.path.isfile(key_path) == False: # Checks if there is already a key generated
                key_data = Fernet.generate_key()
                key_file = open("key.data", "wb")
                key_file.write(key_data)
                key_file.close()

def load_key():
        # Loads the encryption key
        with open(key_path, "rb") as key:
                bin_key = key.read()
                return bin_key

def encrypt_credential(unsafe_credential):
        # Encrypts the given argument using the generated encryption key
        credential = unsafe_credential.encode()
        key_data = load_key()
        f = Fernet(key_data)
        encrypted_credential = f.encrypt(credential)
        return encrypted_credential

def make_json_friendly(data):
        # Decodes the given argument and makes it "json friendly" by changing the quotation marks
        json_friendly = data.decode("utf8").replace("'", '"')
        return json_friendly

def decrypt_credential(encrypted_credential):
        # Decrypts the argument by encoding it back first
        # Loading the encryption key
        # And decrypting it using the key
        encoded_encrypted_credential = encrypted_credential.encode()
        key_data = load_key()
        f = Fernet(key_data)
        decrypted_credential = f.decrypt(encoded_encrypted_credential)
        return decrypted_credential

def decrypt_credential_make_friendly(credential):
        # Takes the argument
        # Encodes it back
        # Decrypts it
        # Decodes it and changes the quotation marks for json friendliness
        decrypted_credential = decrypt_credential(credential)
        friendly_decrypted_credential = make_json_friendly(decrypted_credential)
        return friendly_decrypted_credential