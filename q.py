# arr = [1,2,3,6,5,4,9,8,7]
# target = 9
# curr_sum = 0
# left=0
# found = False
# for right in range(len(arr)):
#             curr_sum += arr[right]

#             # shrink window if sum exceeds target
#             while curr_sum > target and left <= right:
#                 curr_sum -= arr[left]
#                 left += 1

#             if curr_sum == target:
#                 print([left + 1, right + 1])
#                 found = True
#                 break
# if not found:
#        print([-1])

# arr = [2,6,4,8,1,3,5,9]
# m = len(arr)+1

# total_sum = m*(m+1)//2

# arr_sum = 0
# for i in arr:
#     arr_sum += i

# missing = total_sum - arr_sum
# print(missing)

# arr = [2,6,4,8,1,3,5,9]
# m = max(arr)
# arr.remove(m)
# n = max(arr)
# print(n)

# arr= [2,-2,-3,5,-5,6,9,7,8]
# n= len(arr)
# maxi  = float('-inf')
# total = 0
# for i in range(0,n):
#     total  = total + arr[i]
#     maxi = max(maxi,total)
#     if total<0:
#         total = 0
# print(maxi)

class solution():
    def maxsubarray(self,arr):
        n= len(arr)
        maxi  = float('-inf')
        total = 0
        for i in range(0,n):
            total  = total + arr[i]
            maxi = max(maxi,total)
            if total<0:
                total = 0
        return(maxi)
obj = solution()
result = obj.maxsubarray([2,-2,-3,5,-5,6,9,7,8]) 
print(result)   