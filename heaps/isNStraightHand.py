from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        # Step 1: Check if grouping is possible
        if len(hand) % groupSize != 0:
            return False

        # Step 2: Count the occurrences of each card
        count = Counter(hand)
        print(count)

        # Step 3: Sort the unique card values
        sorted_keys = sorted(count.keys())

        # Step 4: Form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
                    print(count)

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
