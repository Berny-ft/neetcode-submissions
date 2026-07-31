from collections import deque
class Twitter:

    def __init__(self):
        self.c = 0
        self.h = {} # for each user id we keep their tweet ids , values of tweet ids have to be in the (count, id)
        self.f = {} # for each user id we keep their follow list
        # when getting the newsfeed ; per tweet you need to tell when it happend so that you can order from the list of followed users the tweets in decreasing order 
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.h:
            self.h[userId] = []
        self.h[userId].append( (self.c, tweetId))
        self.c += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [ ]
        followkeys = list(self.f.get(userId, set())) + [userId]

        for i in self.h:
            if i in followkeys:
                tweets += (self.h[i])
                print(tweets)
        tweets.sort(reverse=True)

        return [ y for x,y in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.f:
            self.f[followerId] = set()
        self.f[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.f:
            self.f[followerId].discard(followeeId)
