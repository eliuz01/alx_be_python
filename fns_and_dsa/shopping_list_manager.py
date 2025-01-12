def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("enter your choice:  ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list")
            else:
                print(f"{item} not found in the shopping list")
        elif choice == '3':
            if shopping_list:
                print("\nShopping List:")
                for item in shopping_list:
                    print(item)
            else: print("Your shopping list is empty.") 
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    

print(main())
