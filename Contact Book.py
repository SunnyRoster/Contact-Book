def print_menu():
  print("1. Add contact")
  print("2. Search contact")
  print("3. Display all contacts")
  print("4. Edit contact")
  print("5. Delete contact")
  print("6. Exit")

contacts = {}

while True:
  print_menu()
  choice = input("Enter your choice: ")

  if choice == "1":
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contacts[name] = number
    print("Contact added successfully!")

  elif choice == "2":
    name = input("Enter name to search: ")
    if name in contacts:
      print(name, ":", contacts[name])
    else:
      print("Contact not found!")

  elif choice == "3":
    if contacts:
      print("Contacts:")
      for name, number in contacts.items():
        print(name, ":", number)
    else:
      print("Contact book is empty!")

  elif choice == "4":
    name = input("Enter name to edit: ")
    if name in contacts:
      number = input("Enter new phone number: ")
      contacts[name] = number
      print("Contact updated successfully!")
    else:
      print("Contact not found!")

  elif choice == "5":
    name = input("Enter name to delete: ")
    if name in contacts:
      del contacts[name]
      print("Contact deleted successfully!")
    else:
      print("Contact not found!")

  elif choice == "6":
    break

  else:
    print("Invalid choice!")