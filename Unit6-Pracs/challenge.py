
contacts = {
    "Alice": "0821112222",
    "Bob": "0833334444",
    "Charlie": "0844445555"
}

search_name = input("Enter the name of the friend you want to look up: ").strip()

if search_name in contacts:
    print(f"Found! {search_name}'s number is {contacts[search_name]}")
else:
    print("Contact not found.")