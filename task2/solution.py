'''
    Binary search is an algorith with runtime complexity O(logn). 
    In this algorithm the required target is searched repeatedly by dividing the search area by half everytime.
'''
class BinarySearch:
    
    def search(self, nums:list[int], target:int) -> int:  #type hinting
        
        if target not in nums:
            found = False   #used in case; if we need to find if target is present or not.
            nums.append(target)
            nums.sort()
            
        lower, upper = 0 , len(nums)-1      

        while lower<= upper:
            mid = (lower + upper)//2
            if nums[mid]==target:
                return mid
            if target > nums[mid]:
                lower = mid + 1
            else:
                upper = mid - 1 
    
#Taking data(sorted array) from the test sample or in this case from users
length = int(input("Enter the length of sorted array: "))
nums = [int(input(f"Enter the sorted array data index {i} : ")) for i in range(length)] #list comprehension
target = int(input("Enter the target: "))
        
solution = BinarySearch() #Creating object
print(solution.search(nums,target))            


