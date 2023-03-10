# https://leetcode.com/problems/design-twitter/

from typing import List
from datetime import datetime
from collections import defaultdict
from heapq import heappush, heappop, nlargest


class Twitter:
    def __init__(self):
        self.posts = defaultdict(lambda: [])
        self.following = defaultdict(lambda: set())

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((datetime.now(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for p in self.posts[userId]:
            heappush(feed, p)

        for f in self.following[userId]:
            for p in self.posts[f]:
                heappush(feed, p)

        feed = [tid for ts, tid in nlargest(10, feed)]
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Tests
twitter = Twitter()
twitter.postTweet(1, 5)
assert twitter.getNewsFeed(1) == [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
assert twitter.getNewsFeed(1) == [6, 5]
twitter.unfollow(1, 2)
assert twitter.getNewsFeed(1) == [5]

twitter = Twitter()
twitter.postTweet(2, 5)
twitter.follow(1, 2)
twitter.follow(1, 2)
assert twitter.getNewsFeed(1) == [5]
