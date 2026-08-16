class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket sort

        #first create a hashmap, where the key is the integer in nums and the value is count of that integer
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #create a bucket, which is an array of lists, the value(count) is the index and the key(integer) is put in the list at that index, for example {3:2}, adds [3] to index 2
        #we need the indexes to exist,in case the first item is 2, we need index 2 to exist
        bucket = [[] for _ in range(len(nums) + 1)]

        for key,val in count.items():
            bucket[val].append(key)

        #get the freq-k elements from the bucket, this will be at the last elements in the bucket going back
        res = []
        for num in bucket[::-1]:
            for i in num:
                if len(res) < k:
                    res.append(i)
        return res
            
