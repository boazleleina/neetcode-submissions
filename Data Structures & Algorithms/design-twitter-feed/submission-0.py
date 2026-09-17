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
        combined_tweets = []
        for user in feed_users:
            combined_tweets.extend(self.tweets[user])
        combined_tweets.sort(key=lambda x:x[1], reverse=True)

        return [tweet[0] for tweet in combined_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
