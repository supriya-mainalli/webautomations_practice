class Solution:
    def threeSum(self, nums):
        n = len(nums)
        seen = set()
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if(nums[i]+nums[j]+nums[k] == 0) and (i!=j) and (j!=k) and (i!=k):
                        sorted_num = sorted([nums[i], nums[j], nums[k]])
                        print(sorted_num)
                        seen.add(tuple(sorted_num))
        
        new_seen = list(seen)
        print(new_seen)
        return [list(x) for x in new_seen]
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))



        