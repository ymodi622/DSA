import heapq
from collections import defaultdict, deque


class Twitter:
    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.tweets[userId].appendleft((self.timer, tweetId))
        # optimize
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int):
        users = self.following[userId] | {userId}
        heap = []

        for userId in users:
            for timer, tid in self.tweets[userId]:
                heapq.heappush(heap, (-timer, tid))
        feed = []
        cnt = 0
        while heap and cnt < 10:
            cnt += 1
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
