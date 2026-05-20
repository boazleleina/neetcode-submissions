class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        low, high = 0, len(self.key_value[key])-1
        result = ""
        while low <= high:
            mid = (low+high)//2

            if self.key_value[key][mid][1] <= timestamp:
                result = self.key_value[key][mid][0]
                low = mid + 1
            else:
                high = mid -1
        return result
        
