#Project: simple inventory management program using lists, dictionaries, and tuples.

inventory = {"egg": (18, 7), "bag": (22, 0.99)}

def checker():
    for item in inventory: 
        print("Item: ", item, ", ", "Quantity: ", inventory[item][0], ", Price: $", inventory[item][1])

print("Welcome to the Inventory Manager!")
print("Current inventory:")
checker()

"Adding a new item: skillet"
inventory["skillet"]= (20, 40)

print("Updated inventory:")
checker()

print("Deleting item: bag")
del inventory["bag"]
checker()

total=0
for item in inventory: 
    total+= inventory[item][1] * inventory[item][0]
print("Total value of inventory: $", total)