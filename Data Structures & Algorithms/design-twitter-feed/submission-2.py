class Twitter:

    def __init__(self):
        #keep track of tweets, map of lists to hold timestamp and tweetId
        self.tweets = defaultdict(list)
        #keep track of followees, a set for unique values of followeeId
        self.following = defaultdict(set)
        #global timestamp to keep track of tweet age
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #each userId will have a tweetId and a global incrementing timestamp
        self.tweets[userId].append([self.timestamp, tweetId])
        #increment the timestamp after each append
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #create a copy of the followees id to keep track of their tweets
        feed_users = self.following[userId].copy()
        feed_users.add(userId)

        #inititate the heap
        maxHeap = []

        #loop through all the users to get their timestamp and tweetId
        for user in feed_users:
            #check if the user has tweets
            if self.tweets[user]:
                #find the total number of tweets-1 for 0-indexed to fetch the tweets
                index = len(self.tweets[user]) -1
                #first get the very last tweet for this user
                timestamp, tweetId = self.tweets[user][index]
                #append that tweet to the heap with the timestamp, userid, and index
                heapq.heappush(maxHeap, [-timestamp, tweetId, user, index])
        res = []
        while maxHeap and len(res) < 10:
            #fetch the items from the maxHeap
            timestamp, tweetId, user, index = heapq.heappop(maxHeap)
            #append the tweetId to the result list
            res.append(tweetId)
            #fetch the next tweet in the timestamp
            if index>0:
                #fetch the next tweet in the list
                next_ts, next_tweet = self.tweets[user][index-1]
                #push that tweet to the heap
                heapq.heappush(maxHeap, [-next_ts, next_tweet, user, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #each follower holds a set of followees
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
