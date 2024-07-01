class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i%2 != 0:
                count += 1
                if count == 3: return True
            else:
                count = 0
        return False

#==================================================================================#

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3: return False
        one, two = 0, 1
        while (two+1)<n:
            if self.odd(arr[one]) and self.odd(arr[two]):
                two+=1
                if self.odd(arr[two]):
                    return True
                else:
                    one = two + 1
                    two = one + 1
            else:
                one+=1
                two+=1
        return False

    def odd(self,x):
        if x%2 != 0: return True
        else: return False