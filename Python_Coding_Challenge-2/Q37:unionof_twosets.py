#Write a program to find union of two sets.
#take input from the user
set1=set(map(int, input("Enter the first set of numbers separated by space: ").split()))#take input set of numbers and convert it to a set of integers
set2=set(map(int, input("Enter the second set of numbers separated by space: ").split()))#take input set of numbers and convert it to a set of integers
#find union of two sets
union_set=set1.union(set2) #find the union of the two sets using the union() method
print(union_set) #print the union of the two sets