class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = {}
        stack = []

        for num in nums2:
            while stack and stack[-1]<num:
                hashmap[stack.pop()] = num
            stack.append(num)
        output = []
        for num in nums1:
            output.append(hashmap.get(num,-1))
        return output