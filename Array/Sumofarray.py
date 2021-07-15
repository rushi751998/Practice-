"""
problem statement

input = arrp[] = {1,2,3}
output = 6


input :
arr[] = {15,12,13,10}

output : 50

"""

arr = [12,3,4,15]

def sum(arr) :
    sum = 0

    for i in arr:
        sum=sum+i
        
    return (sum)

ans = sum(arr)
print ('Sum of the array ',ans)




