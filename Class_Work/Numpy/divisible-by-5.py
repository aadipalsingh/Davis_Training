#divisible by 5
# we will check which elements are greater than 50 and then we will divide each element by 5
import numpy as np
myarray = np.array([45,36,54,67,49,20])
#elem greator than 50
print("elements greater than 50: ")
print(myarray>50)
#divisible by 5
num = myarray/5
print("after dividing each element by 5")
print(num)


#output
#elements greater than 50: 
#[False False  True  True False False]
#after dividing each element by 5
#[ 9.   7.2 10.8 13.4  9.8  4. ]