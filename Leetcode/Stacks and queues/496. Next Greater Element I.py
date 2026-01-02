class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_g = defaultdict(lambda: -1)
        stack = []

        for i in nums2:
            while stack and stack[-1] < i:
                next_g[stack.pop()] = i
            stack.append(i)
        for i in nums1:
            return [next_g[i] for i in nums1]
