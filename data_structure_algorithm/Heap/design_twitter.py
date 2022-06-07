class Twitter(object):

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time_map = defaultdict(int)
        self.time = -1

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweet_map[userId].append(self.time)
        self.time_map[self.time] = tweetId
        self.time -= 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        followees = self.follow_map[userId]
        followees.add(userId)
        minheap = []
        for followee in followees:
            for time in self.tweet_map[followee]:
                heapq.heappush(minheap,time)
                    
        res = []
        count = 10
        while minheap and count:
            res.append(self.time_map[minheap[0]])
            heapq.heappop(minheap)
            count -= 1
        return res
                        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_map[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)