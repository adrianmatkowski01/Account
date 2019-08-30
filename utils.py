# utils.py
import json
import os
from cryptography.fernet import Fernet

key_path = "key.data"

def write_file(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)

def load_file(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

def check_file(file_path):
        if os.path.isfile(file_path) == False:
                msg = {}
                write_file(file_path, msg)

def generate_key():
        if os.path.isfile(key_path) == False:
                key_data = Fernet.generate_key()
                key_file = open("key.data", "wb")
                key_file.write(key_data)
                key_file.close()

def load_key():
        with open(key_path, "rb") as key:
                bin_key = key.read()
                return bin_key

def encrypt_credential(unsafe_credential):
        credential = unsafe_credential.encode()
        key_data = load_key()
        f = Fernet(key_data)
        encrypted_credential = f.encrypt(credential)
        return encrypted_credential

def make_json_friendly(data):
        json_friendly = data.decode("utf8").replace("'", '"')
        return json_friendly

def decrypt_credential(encrypted_credential):
        encoded_encrypted_credential = encrypted_credential.encode()
        key_data = load_key()
        f = Fernet(key_data)
        decrypted_credential = f.decrypt(encoded_encrypted_credential)
        return decrypted_credential

def decrypt_credential_make_friendly(credential):
        decrypted_credential = decrypt_credential(credential)
        friendly_decrypted_credential = make_json_friendly(decrypted_credential)
        return friendly_decrypted_credential