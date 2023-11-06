"""
Question Link: https://leetcode.com/problems/seat-reservation-manager/solutions/4254602/more-than-one-way-detail-explanation/?envType=daily-question&envId=2023-11-06
"""

#-----------Solution 1--------------
# class SeatManager(object):

#     def __init__(self, n):
#         """
#         :type n: int
#         """
#         self.res = []
#         self.unres = [i for i in range(1,n+1)]
        

#     def reserve(self):
#         """
#         :rtype: int
#         """
#         min_r = min(self.unres)
#         self.unres.remove(min_r)
#         self.res.append(min_r)
#         return min_r


        

#     def unreserve(self, seatNumber):
#         """
#         :type seatNumber: int
#         :rtype: None
#         """
#         self.res.remove(seatNumber)
#         self.unres.append(seatNumber)
                

#-------------Solution 2---------------------
# class SeatManager(object):

#     def __init__(self, n):
#         """
#         :type n: int
#         """
#         self.d = {i:False for i in range(1,n+1)}
#         self.min = 1
#         self.next_min = 1
        

#     def reserve(self):
#         """
#         :rtype: int
#         """
#         while self.d[self.min]:
#             self.min+=1
#         self.d[self.min] = True
#         temp = self.min
#         self.min+=self.next_min
#         self.next_min = 1
#         return temp
        

#     def unreserve(self, seatNumber):
#         """
#         :type seatNumber: int
#         :rtype: None
#         """
#         self.next_min = 1
#         if self.d[seatNumber]:
#             self.d[seatNumber] = False
#             if self.min>seatNumber:
#                 self.next_min = self.min-seatNumber
#                 self.min = seatNumber

#             if self.next_min>seatNumber:
#                 self.next_min = seatNumber-self.min
                
#-----------Solution 3---------------------      
import heapq


class SeatManager:

    def __init__(self, n):
        self.count = 0
        self.heap = []

    def reserve(self):
        if len(self.heap) == 0:
            self.count = self.count + 1
            return self.count
        else :
            return heapq.heappop(self.heap)

    def unreserve(self, seatNumber):
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)