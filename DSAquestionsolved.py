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

# class solution():
#     def maxsubarray(self,arr):
#         n= len(arr)
#         maxi  = float('-inf')
#         total = 0
#         for i in range(0,n):
#             total  = total + arr[i]
#             maxi = max(maxi,total)
#             if total<0:
#                 total = 0
#         return(maxi)
# obj = solution()
# result = obj.maxsubarray([2,-2,-3,5,-5,6,9,7,8]) 
# print(result)   

# class Solution:
#     def missingNum(self, arr):
#         n = len(arr) +1
#         total = n*(n+1)//2
#         return total - sum(arr)

# class Solution:
#     def getSecondLargest(self, arr):
#         arr3 = list(set(arr))
#         m = len(arr3)
#         if len(arr3)<2:
#             return -1
#         new_arr = max(arr3)
#         arr3.remove(new_arr)
#         return max(arr3)
# obj = Solution()
# result = obj.getSecondLargest([2,6,4,8,1,3,5,9]) 
# print(result) 
# 

# arr = [12,35,24,69,85,42,45]
# max = arr[0]
# for i in range(1,len(arr)):
#        if arr[i]>max:
#               max = arr[i]
# print("maximin number",max)

# arr = [12,35,24,69,85,42,45]
# max = arr[0]
# for i in range(1,len(arr)):
#        if arr[i]<max:
#               max = arr[i]
# print("minimum number",max)

# arr = [12,35,24,69,85,42,45]
# max = arr[0]
# for i in range(-1,-len(arr),-1):
#        print(arr[i],end=" ")

# arr = [12,35,24,69,12,85,42,45]
# count = 0
# for i in range(1,len(arr)):
#        for j in range(1,len(arr)):
#               if i == j:
#                      count += 1
# print(count)

# arr = [12, 7, 9, 20, 33, 40]

# even_count = 0
# odd_count = 0

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)

# arr = [10,23,56,45,3,21,5]
# for i in range(1,len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i]<arr[j]:
#             print(arr[j],end=' ')

# class Solution:
#     def leaders(self, arr):
#         n = len(arr)
#         result = []
        
#         max_from_right = arr[-1]
#         result.append(max_from_right)
        
#         for i in range(n-2, -1, -1):
#             if arr[i] >= max_from_right:
#                 max_from_right = arr[i]
#                 result.append(arr[i])
        
#         result.reverse()
#         return result


# class Solution:
#     def findDuplicates(self, arr):
#         freq = {}
#         result = []
        
#         for num in arr:
#             freq[num] = freq.get(num, 0) + 1
            
#         for key in freq:
#             if freq[key] > 1:
#                 result.append(key)
                
#         return result
# ans = Solution()
# print(ans.findDuplicates([3,2,1,2,3]))

class Solution:
    def sort012(self, arr):
        c0 = c1 = c2 = 0
        
        for num in arr:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        
        i = 0
        
        while c0 > 0:
            arr[i] = 0
            i += 1
            c0 -= 1
            
        while c1 > 0:
            arr[i] = 1
            i += 1
            c1 -= 1
            
        while c2 > 0:
            arr[i] = 2
            i += 1
            c2 -= 1
ans = Solution()
print(ans.sort012([0,2,0,1,2,1,0,2]))

# class Solution():
#     def sort012(self, arr):
#         low = 0
#         mid = 0
#         high = len(arr) - 1
        
#         while mid <= high:
#             if arr[mid] == 0:
#                 arr[low], arr[mid] = arr[mid], arr[low]
#                 low += 1
#                 mid += 1
                
#             elif arr[mid] == 1:
#                 mid += 1
                
#             else:  # arr[mid] == 2
#                 arr[mid], arr[high] = arr[high], arr[mid]
#                 high -= 1
# ans = Solution()
# print(ans.sort012([0,2,0,1,2,1,0,2]))

arr = [1,2,3,1,2,3,1,1,1]
majority = None
count = 0
for num in arr:
    if count == 0:
        majority = num
    if num == majority:
        count+=1
    else:
        count -= 1
count =0
for num in arr:
    if num == majority:
        count+=1
        
if count > len(arr)//2:
    print(majority) 
else:
    print('-1') 
