from collections import Counter


def longestSubstring(s, k):
    freq = Counter(s)
    for c in freq:
        if freq[c] < k:
            return max(longestSubstring(t, k) for t in s.split(c))
    return len(s)


print(longestSubstring("aaabb", 3))
