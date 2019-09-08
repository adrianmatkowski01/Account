import utils
import gui

utils.generate_key()
data_file = "data.json"
utils.check_file(data_file)

def login_variable(var):
    global login_entry_variable
    login_entry_variable = var

def password_variable(var):
    global password_entry_variable
    password_entry_variable = var

def register_login_variable(var):
    global login_register_entry_variable
    login_register_entry_variable = var

def register_password_variable(var):
    global password_register_entry_variable
    password_register_entry_variable = var

def register_repassword_variable(var):
    global repassword_register_entry_variable
    repassword_register_entry_variable = var

def login():
    # Login function
    log_in = login_entry_variable
    password = password_entry_variable
    data = utils.load_file(data_file)
    encrypted_log_in = "".join(data.keys())
    encrypted_password = "".join(data.values())
    friendly_decrypted_log_in = utils.decrypt_credential_make_friendly(encrypted_log_in)
    friendly_decrypted_password = utils.decrypt_credential_make_friendly(encrypted_password)
    if log_in == friendly_decrypted_log_in and password == friendly_decrypted_password:
        # Login success 
        gui.label_text_variable = "Login successful"
    else:
        # Login bad
        gui.label_text_variable = "Wrong Login or Password!"
    
def register():
    # Register function
    log_in = login_register_entry_variable
    password = password_register_entry_variable
    re_password = repassword_register_entry_variable
    if password == re_password:
        encrypted_login = utils.encrypt_credential(log_in)
        encrypted_password = utils.encrypt_credential(password)
        json_friendly_login = utils.make_json_friendly(encrypted_login)
        json_friendly_password = utils.make_json_friendly(encrypted_password)
        data = {}
        data[json_friendly_login] = json_friendly_password
        utils.write_file(data_file, data)
        gui.label_text_variable = "Registered!"
    else:
        gui.label_text_variable = "Your Passwords dont match!\nTry again!"