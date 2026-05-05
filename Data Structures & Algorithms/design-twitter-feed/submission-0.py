class Twitter:

    def __init__(self):
        self.followermap=defaultdict(set)
        self.tweetmap=defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time, tweetId))
        self.time += 1   # decreasing → latest = smallest
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # include self + followees
        self.followermap[userId].add(userId)

        for followee in self.followermap[userId]:
            tweets = self.tweetmap[followee]
            # take last 10 tweets only (optimization)
            for time, tweetId in tweets[-10:]:
                heapq.heappush(heap, (time, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)

        # extract tweets sorted by most recent
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId]:
            self.followermap[followerId].remove(followeeId)
        
