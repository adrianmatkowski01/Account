import utils
import account

def main():
    # Main funtion
    utils.generate_key()
    print("Hello, would you want to Log in or Register?\n")
    choice = input()
    if choice == "Log in":
        account.login()
    elif choice == "Register":
        account.register()
    elif choice == "close":
        print("Closing!")

if __name__ == "__main__":
    main()