"""
Question Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
"""
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        # ops = []
        # s = []
        # for i in range(1,n+1):
        #     if s and s[-1] not in target:
        #         s.pop()
        #         ops.append("Pop")
        #     s.append(i)
        #     ops.append("Push")
        #     if s==target:
        #         return ops
        # return ops

        ops = []
        if target[0]>1:
            ops.extend(["Push","Pop"]*(target[0]-1))

        ops.append("Push")

        for i in range(1,len(target)):
            temp = target[i]-target[i-1]
            if temp>1:
                ops.extend(["Push","Pop"]*(temp-1))
                ops.append("Push")

            else:
                ops.append("Push")
        return ops