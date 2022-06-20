from numpy import *

# break statement

# av=10
# x=int(input("how many candies you want ?"))
# i=1
# while i<=x:
#     if i>av:
#         break
#
#     print("candy")
#     i=i+1
#
# print("exit")
#

# ------------divisible by 3 --------------------
# for i in range(1,101):
#     if i%3==0:
#         continue
#     print(i)

# -------------------oddd numbers------------
# for i in range(1,101):
#     if(i%2!=0):
#         pass
#     else:
#         print(i)


# for i in range(5):
#     if i==3:
#         break
#     print("hell")

#

# --------------------square pattern------------------

# for i in range(4):
#     for j in range(4):
#         print("#", end=" ")
#     print()
# -------------------------triangle pattern
#
# for i in range(4):
#     for j in range(i+1):
#         print("#" , end="")
#     print()


# for i in range(4):
#     for j in range(4-i):
#         print("#", end="")
#     print()
#
#


# -----------------------------for else--------------
#
# nums=[12 ,15,19,234,46]
# for num in nums:
#     if num%5==0:
#         print(num)

# ---------------------------take value from user for arrray

# arr = array('i' ,[])
# n = int(input("enter the length of the array"))
#
# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
#
# print(arr)
#
# Val=int(input("enter the value fro search"))
#
# k=0
# for e in arr:
#     if e==Val:
#         print(k)
#         break
#     k=k+1

# -----------------------multidimentional array
# arr =array([1,2,3,4,5,6])
# print(arr.dtype)
# print(arr)
#
#
# # --------------------
#
# arr=linspace(0,15)
#
# print(arr)
#
# # ---------------------------arange
#
# arr=arange(1,15,2)
#
# print(arr)
#
# # ------------------------logspcae
#
# arr=logspace(1,40,5)
# print('%2f'%arr[3])
# print(arr)
#
# # --------------------------zeros
#
# arr=ones(5 , int)
# print(arr)

# ------------------------copying array in python

# arr1= array([2,3,5,7,4])
# arr2=array([ 7 ,8, 10, 12 , 9])
# arr=arr1+arr2
# print(arr)
#
# arr1= array([2,3,5,7,4])
# arr2=array([ 7 ,8, 10, 12 , 9])
#
# print(concatenate([arr1,arr2]))
#
#
# arr1= array([2,3,5,7,4])
# arr2=arr1.copy()
# arr1[3]=6
# print(arr1)
# print(arr2)
#

# --------------------------------working on matrix------------------

# arr= array([
#     [1,2,3],
#     [2,3,4]
# ])
# print(arr)
#
# m =matrix('1,2,3;4 ,6 3 ;4,5,6')
# print(m)
