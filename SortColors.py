Sort Colors:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Passed all testcases on leetcode successfully

Space Complexity  O(1)
Time Complexity   O(n) 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums ==None or len(nums) == 0:
            return []
        result = []
        #using two pointers
        low,mid = 0,0
        high = len(nums) - 1
        while (mid <= high):
            #totatlly 3 cases in the problem value an be 0,1,2
           
            if nums[mid] == 0:
        #Value 0 should be at the low of the list  swap the number increment mid and low 
                self.__swap(nums,low,mid)
                low += 1
                mid += 1
                
        #Value 1 should be at the mid of the list increment mid   
            elif nums[mid] == 1:
                mid += 1
         #Value 2 should be at the end of the list swap the number and decrement high 
            elif nums[mid] == 2:
                self.__swap(nums,mid,high)
                high -= 1
        return
                
                
    def __swap(self,nums,i,j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
