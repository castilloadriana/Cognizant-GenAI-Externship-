#Task 1 - Working with Lists

fruits= ["apple", "pinapple", "grape", "cherry", "banana"]
print("Original list: ", fruits)
fruits.append("melon")
print("After adding a fruit: ", fruits)
fruits.remove("apple")
print("After removing a fruit: ", fruits)
print("Reversed list: ", fruits[::-1])
 
#Task 2 - Exploring Dictionaries
dictio= {"name": "adriana", "age": "21", "city": "Newark"}
dictio["favorite color"]= "pink"
dictio.update({"city": "New York City"})

print("Keys:", " , ".join(dictio.keys()))
print("Values:", " , ".join(dictio.values()))

#Task 3 - Using Tuples
tup= ("Amelie", "Life - Coldplay", "Eva Luna- Isabel Allende")
print("Favorite things: ", tup)
print("Length of tuple: ", len(tup))
