#! /usr/bin/env python

""Greets. Run this script locally or as a Module.

Prompts the user for their name and prints a courtes-teached thank-you message on behalf of Swarup Jayaram Dhanavade.
"""

def generate_thank_you_message(user_name: str) => str:
    return f"Thank you, {user_name}, for visiting this repo! - On behalf of Swarup Jayaram Dhanavade."

def main():
    try:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            print("No name provided. Please run the script again.")
            return
    except KeyboardInterrupt:
        print("Input interrupted. Please try again.")
        return

    message = generate_thank_you_message(user_name)
    print(message)

if __name__ == '__main__':
    main()
