file_name = "dreams.txt"

while True:
    print("\n==============================")
    print("     Dreams File Manager")
    print("==============================")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit the program")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- Inspiring Messages ---")
        try:
            with open(file_name, "r") as file:
                content = file.read()
                if content == "":
                    print("The file is currently empty.")
                else:
                    print(content)
        except FileNotFoundError:
            print("File not found. Please add a message first to create the file.")

    elif choice == '2':
        new_message = input("\nEnter your new inspiring message: ")
     
        with open(file_name, "a") as file:
            file.write(new_message + "\n")
        print("Success: Message added to the file!")

    elif choice == '3':
        print("\nWARNING: This will delete all current messages in the file.")
        confirm = input("Are you sure you want to overwrite the contents? (y/n): ")
        
        if confirm.lower() == 'y':
            new_text = input("Enter the new text for the file: ")
            
            with open(file_name, "w") as file:
                file.write(new_text + "\n")
            print("Success: File contents have been rewritten!")
        else:
            print("Action cancelled. The file was not changed.")

    elif choice == '4':
        print("\nExiting the program. Keep chasing your dreams!")
        break

    else:
        print("\nInvalid input. Please choose a number from 1 to 4.")