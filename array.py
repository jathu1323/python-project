import numpy as np

print()
print ('*_*_*_*_*_*CALCULATING GPA*_*_*_*_*_*')
print()
a=input('How Many Subjet Are Using For GPA Calculation : \n')
sub_name={}
#sub_name=[]
sub_name=[input('Input the subject name :  \n') for i in range(int(a))]
print ()

sub_credit={}
#sub_credit=[]
sub_credit=[input('Input the subject credits :  \n') for i in range(int(a))]
print ()

sub_marks={}
# sub_marks=[]
sub_marks=[int(input('Input the subject marks :  \n')) for i in range(int(a))]
print ()

sub_assignment={}
# sub_assignment=[]
sub_assignment=[int(input('Input the subject assignment marks :  \n')) for i in range(int(a))]
print()
GPA=[]
GPA.append (sub_name)
GPA.append (sub_credit)
GPA.append (sub_marks)
GPA.append (sub_assignment)
print (GPA)


  
arr1 = np.array([[2, -7, 5], [-6, 2, 0]])
arr2 = np.array([[0, -7, 8], [5, -2, 9]])
   
print ("1st Input array : ", arr1)
print ("2nd Input array : ", arr2)
   
    
arr = np.multiply(arr1, arr2) 
arr3= np.add(arr1,arr2)
print ("Resultant output array: ", arr)
print ("Resultant output array: ", arr3)
