# Use of dictionaries
# Dictionaries are used to store data values in key:value pairs.    
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Example
progamming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
print(progamming_dictionary["Bug"])

#add new items to the dictionary
progamming_dictionary["New Key"] = "New Value"
print(progamming_dictionary)

# Create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

# Wipe an existing dictionary
# progamming_dictionary = {}  
# print(progamming_dictionary)

# edit an item in the dictionary
progamming_dictionary["Bug"] = "A moth in your computer."
print(progamming_dictionary)
print("-------------------")

# Loop through a dictionary
for key in progamming_dictionary:
    print(key)
    print(progamming_dictionary[key]) # print the value of the key