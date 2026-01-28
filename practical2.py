SIZE = 10
hash_table = [[] for _ in range(SIZE)]  # each index stores a list for chaining

def hash_function(key):
    return key % SIZE  # Division method

def insert(key):
    index = hash_function(key)
    if key not in hash_table[index]:
        hash_table[index].append(key)
        print(f"Inserted key {key}")
    else:
        print(f"Key {key} already exists")

def search(key):
    index = hash_function(key)
    if key in hash_table[index]:
        print(f"Key {key} found at index {index}")
    else:
        print(f"Key {key} not found")

def delete(key):
    index = hash_function(key)
    if key in hash_table[index]:
        hash_table[index].remove(key)
        print(f"Key {key} deleted successfully")
    else:
        print(f"Key {key} not found")

def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")

# Menu Driven Program
while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

