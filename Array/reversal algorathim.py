'''
Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output : arr[] = [3, 4, 5, 6, 7, 1, 2] 
'''

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len (arr)

def reversal(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
# print(arr)

print ("Reversal araray is ",(reversal(arr,d,n)))