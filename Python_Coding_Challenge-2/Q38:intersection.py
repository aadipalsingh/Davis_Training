#Write a program to find intersection

#take input from the user
set1=set(map(int, input("Enter the first set of numbers separated by space: ").split()))#take input set of numbers and convert it to a set of integers
set2=set(map(int, input("Enter the second set of numbers separated by space: ").split()))#take input set of numbers and convert it to a set of integers
#find intersection of two sets

intersection_set=set1.intersection(set2) #find the intersection of the two sets using the intersection() method
print(intersection_set) #print the intersection of the two sets 
