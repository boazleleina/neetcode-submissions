class TimeMap:

    def __init__(self):
        self.key_val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        search = self.key_val[key]

        left, right = 0, len(search)-1

        res = ""

        while left <= right:
            mid = (left + right) // 2

            if search[mid][1] <= timestamp:
                res = search[mid][0]
                left = mid + 1
            else:
                right = mid-1
        return res
        
