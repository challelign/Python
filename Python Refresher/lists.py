
# Definition: An ordered, mutable (changeable) collection of items.
##Key Features:
# Items are stored in the order they are added.
# You can modify, add, or remove items.
# Allows duplicate items.
# Use Case: When you need a dynamic, ordered collection of items that may include duplicates.

# 
my_list =[83,96,99,81,10]
print("[my_list]=>",my_list)

my_list.append(55)
print("[my_list after append]=>",my_list)

my_list.insert(2,77)
print("[my_list after insert]=>",my_list) 

my_list.remove(55) # reomve the value not the index
print("[my_list remove]=>",my_list) 

my_list.pop(2) # reomve the value by locakting the index
print("[my_list pop]=>",my_list) 

my_list.sort()
print("[my_list sort]=>",my_list) 
for x in my_list: {
    print(x)
} 