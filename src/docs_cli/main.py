from .modules import create_documentation, list_documentation, update_documentation, delete_documentation

def main_menu():
    while True:
        print("\n===================")
        print("---Docs To Read---")
        print("1. Display List")
        print("2. Add Doc")
        print("3. Update Doc")
        print("4. Delete Doc")
        print("5. Quit")
        print("===================")

        try:
            choice = int(input("Enter your choice: "))
            print("===================\n")
        except ValueError:
            print("Please enter a number between 1-5")
            print("===================\n")
            continue

        match choice:
            case 1:
                print("List of Docs")
                list_documentation()
            case 2:
                print("Add Documentation")
                create_documentation()
            case 3:
                print("Update Documentation Record")
                update_documentation()
            case 4:
                print("Delete Documentation")
                delete_documentation()
            case 5:
                print("Exiting program")
                break
            case _:
                print("Please select an option 1-5")

if __name__ == "__main__":
    main_menu()
