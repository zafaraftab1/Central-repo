#code to extract all zeros to left and all non zeros to right

mylist=[0,3,5,0,56,23]
mylist2= [i for i in mylist if i==0]+[i for i in mylist if i!=0]
print(mylist2)

# code to find the largest and smallest elements in a list

list1 = [3, 45, 87, 21, 90, 21]

largest = list1[0]
smallest = list1[0]
for i in list1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
