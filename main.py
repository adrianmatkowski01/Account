import utils

if __name__ == "__main__":
    main()

data_file = "data.json"
data = utils.load_file(data_file)
# Function used to log in
def login():
    log_in = None
    password = None
    log_in = input("Login: ")
    password = input("Password: ")
    if log_in == "".join(data.keys()) and password == "".join(data.values()):
        print("Log in successful!")
    elif log_in == "close":
        print("Closing!")
    else:
        print("Something went wrong...\nPlease try again!")
        # print("".join(data.keys()))
        # print("".join(data.values()))
        login()
# Function used to register
def register():
    log_in = input("Enter your Login: ")
    password = input("Enter your Password: ")
    re_password = input("Re-Enter your Password: ")
    if password == re_password:
        data = {}
        data[log_in] = password
        utils.write_file(data_file, data)
        print("Registered!")
    else:
        print("Your Passwords dont match!\nTry again!")
        register()
# Main function
def main():
    print("Hello, would you want to Log in or Register?\n")
    choice = input()
    if choice == "Log in":
        login()
    elif choice == "Register":
        register()