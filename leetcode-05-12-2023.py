class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        #--------Solution 1-----------
        # if k>len(arr):
        #     return max(arr)

        # d = {}
        # while True:
        #     i = 1
        #     if arr[i-1]>arr[i]:
        #         d[arr[i-1]] = d.get(arr[i-1],0)+1
        #         if d[arr[i-1]]==k:
        #             return arr[i-1]
        #         d[arr[i]] = 0
        #         arr.append(arr.pop(i))
        #     else:
        #         d[arr[i]] = d.get(arr[i],0)+1
        #         if d[arr[i]]==k:
        #             return arr[i]
        #         d[arr[i-1]] = 0
        #         arr.append(arr.pop(i-1))

        #----------Solution 2---------------
        # if k>len(arr):
        #     return max(arr)

        # d = {}
        # m_arr = max(arr)
        # while True:
        #     if arr[0]==m_arr or arr[1]==m_arr:
        #         return m_arr
        #     if arr[0]>arr[1]:
        #         d[arr[0]] = d.get(arr[0],0)+1
        #         if d[arr[0]]==k:
        #             return arr[0]
        #         d[arr[1]] = 0
        #         arr.append(arr.pop(1))
        #     else:
        #         d[arr[1]] = d.get(arr[1],0)+1
        #         if d[arr[1]]==k:
        #             return arr[1]
        #         d[arr[0]] = 0
        #         arr.append(arr.pop(0))

        #---------Solution 3--------------
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)

        m_arr = max(arr)
        current_winner = arr[0]
        consecutive_wins = 0

        if current_winner==m_arr:
            return m_arr

        for i in range(1, len(arr)):
            if arr[i]==m_arr:
                return m_arr

            if current_winner > arr[i]:
                consecutive_wins += 1
            else:
                current_winner = arr[i]
                consecutive_wins = 1

            if consecutive_wins == k:
                return current_winner

        return current_winner