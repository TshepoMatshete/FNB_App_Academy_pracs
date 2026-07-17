firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
bio = input("Please enter a short bio about yourself: ")

username = (firstName[0] + lastName).lower()
bio_stripped = bio.strip()
bio_char_count = len(bio_stripped)
bio_replaced = bio_stripped.replace("I am", "I'm")

print(f"Your username is: {username} \n YSour bio is: \n{bio_replaced}")