string = "ahmed"
if len(string)%2 == 0:
    middle1 = (len(string)//2)-1
    middle2= len(string)//2
    print(string[middle1]+string[middle2])
else:
    middle = int(len(string)/2)
    print(string[middle])