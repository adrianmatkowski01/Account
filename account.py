import utils

data_file = "data.json"
utils.check_file(data_file)
data = utils.load_file(data_file)

def login():
    # Login function
    log_in = None
    password = None
    log_in = input("Login: ")
    password = input("Password: ")
    encrypted_log_in = "".join(data.keys())
    encrypted_password = "".join(data.values())
    friendly_decrypted_log_in = utils.decrypt_credential_make_friendly(encrypted_log_in)
    friendly_decrypted_password = utils.decrypt_credential_make_friendly(encrypted_password)
    if log_in == friendly_decrypted_log_in and password == friendly_decrypted_password:
        print("Log in successful!")
    elif log_in == "close":
        print("Closing!")
        pass
    else:
        print("Something went wrong...\nPlease try again!")
        login()

def register():
    # Register function
    log_in = input("Enter your Login: ")
    password = input("Enter your Password: ")
    re_password = input("Re-Enter your Password: ")
    if password == re_password:
        encrypted_login = utils.encrypt_credential(log_in)
        encrypted_password = utils.encrypt_credential(password)
        json_friendly_login = utils.make_json_friendly(encrypted_login)
        json_friendly_password = utils.make_json_friendly(encrypted_password)
        data = {}
        data[json_friendly_login] = json_friendly_password
        utils.write_file(data_file, data)
        print("Registered!")
    else:
        print("Your Passwords dont match!\nTry again!")
        register()
