class Solution:
    def leastInterval(self, tasks, n) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)


ob = Solution()
print(ob.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
