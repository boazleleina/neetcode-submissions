class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.tweetTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.tweetTime])
        self.tweetTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_users = self.following[userId].copy()
        feed_users.add(userId)
        maxHeap = []
        for user in feed_users:
            if self.tweets[user]:
                index = len(self.tweets[user]) -1
                tweetId, timestamp = self.tweets[user][index]
                heapq.heappush(maxHeap, [-timestamp, tweetId, user, index])

        res = []
        while maxHeap and len(res) < 10:
            timestamp, tweetId, user, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index > 0:
                next_tweetId, next_ts = self.tweets[user][index-1]
                heapq.heappush(maxHeap, [-next_ts, next_tweetId, user, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
