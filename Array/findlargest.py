"""
Input : arr []={10,20,4}
output 20

"""


arr = [400,20,4]
n = len (arr)


def largest (arr):
    max = arr[0]
   
    for i in range (0 ,n):
        if arr[i]>max:
            max = arr[i]
    return max



ans = largest (arr)
print ("largest nuber in Set is : ", ans)
