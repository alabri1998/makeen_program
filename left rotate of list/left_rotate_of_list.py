# initializing list
test_list = [1, 4, 6, 7, 2]

# printing original list
print ("Original list : " + str(test_list))

# using slicing to left rotate by 3
test_list = test_list[2:] + test_list[:2]

# Printing list after left rotate
print ("List after left rotate by 2 : " + str(test_list))



