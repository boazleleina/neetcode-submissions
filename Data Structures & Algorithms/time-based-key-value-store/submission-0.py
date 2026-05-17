class TimeMap:

    def __init__(self):
        #initialize hashmap to keep track of my key-value pairs
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #map the array, value and timestamp to key
        self.key_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        #initialize low, high
        low,high = 0, len(self.key_map[key])-1
        #initialize result
        result = ""
        #while low is less than high:
        while low <= high:
            #calculate middle index
            mid = (low + high) // 2
            #if the entry_timestamp == query_timestamp:
            if self.key_map[key][mid][1] == timestamp:
                #return value
                return self.key_map[key][mid][0]
            #if entry_timestamp < query_timestamp:
            if self.key_map[key][mid][1] < timestamp:
                #assign the value here to result
                result = self.key_map[key][mid][0]
                #move the low to mid+1 to check if there's a valid higher timestamp
                low = mid + 1
            #else: meaning entry_timestamp>query_timestamp
            else:
                #move high to mid-1
                high = mid - 1
        #return result
        return result
