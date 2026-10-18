class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_x, found_y, found_z = False,False, False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                found_x = True
            if t[1] == target[1]:
                found_y = True
            if t[2] == target[2]:
                found_z = True
        return found_x and found_y and found_z