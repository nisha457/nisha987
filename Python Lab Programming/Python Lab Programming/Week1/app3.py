            def get_person_details():
                """
                Function to read a person's details from the keyboard.
                """
                name = input("Enter your name: ")
                address = input("Enter your address: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                return name, address, email, phone

            def print_person_details(name, address, email, phone):
                """
                Function to print a person's details.
                """
                print("\n--- Personal Details ---")
                print(f"Name: {name}")
                print(f"Address: {address}")
                print(f"Email: {email}")
                print(f"Phone Number: {phone}")

            # Get details from the user
            name, address, email, phone = get_person_details()

            # Print the details
            print_person_details(name, address, email, phone)
