import json
import os

# File to store homework data
DATA_FILE = "homework_data.json"

# Load existing homework data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save homework data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new homework assignment
def add_homework(data):
    title = input("Enter the title of the homework: ")
    description = input("Enter the description: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    data.append({"title": title, "description": description, "due_date": due_date})
    save_data(data)
    print("Homework added successfully!")

# Edit an existing homework assignment
def edit_homework(data):
    list_homework(data)
    index = int(input("Enter the number of the homework to edit: ")) - 1
    if 0 <= index < len(data):
        data[index]["title"] = input("Enter new title: ") or data[index]["title"]
        data[index]["description"] = input("Enter new description: ") or data[index]["description"]
        data[index]["due_date"] = input("Enter new due date (YYYY-MM-DD): ") or data[index]["due_date"]
        save_data(data)
        print("Homework updated successfully!")
    else:
        print("Invalid selection.")

# Delete a homework assignment
def delete_homework(data):
    list_homework(data)
    index = int(input("Enter the number of the homework to delete: ")) - 1
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        print("Homework deleted successfully!")
    else:
        print("Invalid selection.")

# List all homework assignments
def list_homework(data):
    if not data:
        print("No homework assignments found.")
    else:
        for i, hw in enumerate(data, start=1):
            print(f"{i}. {hw['title']} - Due: {hw['due_date']}")

# Main menu
def main():
    data = load_data()
    while True:
        print("\nHomework Tracker")
        print("1. Add Homework")
        print("2. Edit Homework")
        print("3. Delete Homework")
        print("4. List Homework")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_homework(data)
        elif choice == "2":
            edit_homework(data)
        elif choice == "3":
            delete_homework(data)
        elif choice == "4":
            list_homework(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()