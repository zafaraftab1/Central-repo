#code to extract all zeros to left and all non zeros to right
mylist=[0,3,5,0,56,23]
mylist2= [i for i in mylist if i==0]+[i for i in mylist if i!=0]
print(mylist2)