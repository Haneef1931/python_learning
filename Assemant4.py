import Haneef


#grades = {"Tiawo": 78,
         #"Kehinde" : 85,
         #"Haneef" : 92,
         #"Maryam" : 64,}
#print(grades)
#grades.update({"Maryam": 74})
#print(grades)
#grades["Zahara"] = 85
#print(grades)
#grades.pop("Tiawo")
#print(grades)
#input_name = "Ateeyah"
#if input_name in grades:
    #print(f"{input_name}'s grade is {grades[input_name]}")
#else:
    #print("That name doesn't exist")

prices = {"Keybord": 45.00,
          "Mouse": 25.00,
          "Monitor": 150.00,
          "Usb cable": 8.00,}
stock = {"Keybord": 12,
         "Mouse": 0,
         "Monitor": 5,
         "Usb cable": 30,}
print(prices)
print(stock)

# 1. Find out-of-stock products
for product, quantity in stock.items():
    if quantity == 0:
        print("Out of stock:", product)

# 2. Calculate total inventory value
total = 0

for product, quantity in stock.items():
    total += prices[product] * quantity

print(f"Total inventory value: £{total:.2f}")

# 3. Create low_stock dictionary
low_stock = {}

for product, quantity in stock.items():
    if quantity > 0 and quantity < 15:
        low_stock[product] = quantity

print("Low stock:", low_stock)

sentence ="python is great and pyhton is fun to learn because it make coding simple"
words = sentence.split()
print(words)
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
for word, count in word_counts.items():
    if count > 1:
        print(word, count)
        most_frequent_word = ""
highest_count = 0

for word, count in word_counts.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word

print("Most frequent word:", most_frequent_word)
print("Count:", highest_count)
users = {
    "user_01": {"username": "dev_alex", "role": "admin", "active": True},
    "user_02": {"username": "sarah_k", "role": "editor", "active": False},
    "user_03": {"username": "mike_99", "role": "viewer", "active": True},
    "user_04": {"username": "elena_r", "role": "editor", "active": True}
}

# 1. Print usernames of all active users
print("Active users:")
for user_id, details in users.items():
    if details["active"] == True:
        print(details["username"])


# 2. Update user_02
users["user_02"]["active"] = True
users["user_02"]["role"] = "admin"


# 3. Count total number of admin users
admin_count = 0

for user_id, details in users.items():
    if details["role"] == "admin":
        admin_count += 1

print("\nTotal admin users:", admin_count)
