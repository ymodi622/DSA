from collections import deque


def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    chars = "abcdefghijklmnopqrstuvwxyz"
    q = deque()
    q.append((beginWord, 1))
    wordList.discard(beginWord)
    while q:
        node = q.popleft()
        word = node[0]
        level = node[1]
        for i in range(len(word)):
            for char in chars:
                new = word[:i] + char + word[i + 1 :]
                if new == endWord:
                    return level + 1
                if new in wordList:
                    q.append((new, level + 1))
                    wordList.discard(new)
    return 0


print(ladderLength("hot", "dog", ["hot", "dog"]))
