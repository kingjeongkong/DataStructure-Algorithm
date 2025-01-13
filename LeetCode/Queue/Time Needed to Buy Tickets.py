from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time = 0

        while True:
            value = queue.popleft()
            value -= 1
            time += 1

            if k == 0 and value == 0:
                return time

            if value != 0:
                queue.append(value)

            if k == 0:
                k = len(queue) - 1
            else:
                k -= 1

# When I started this problem, I figured out that the main point is how to track the k index and k's remaining tickets
# So I declared tickets_k for tracking k's ticket number and another index_k. And also useing 'for' loop in 'while' loop made it really complicated and also couldn't solve the problem. And even time complexity was the worst.

# After thinking and searching I found out how to track and change the k's index and tickets number.
# Only in while loop, decrease the k(index)'s value until the k comes front of queue(k == 0). And if the k reaches front of the queue, then assigns the length of queue to the k. Then the logic is carried out until the k's ticket number reaches 0 (value == 0).
# In this logic my intention is after popleft from queue -1 from that value and comparing this index is k or not. After that if it's not, check the value if it's 0 or not. If it's 0, I don't have to do anything cause I already did popleft so it's gonna be gone. But if it's not 0, I have to append this value in the queue again. And then process the k.