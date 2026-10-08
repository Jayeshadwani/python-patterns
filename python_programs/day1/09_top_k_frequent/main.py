import heapq
from collections import Counter
from typing import List


def top_k_frequent(words: List[str], k: int) -> List[str]:
    """Return the k most frequent words: higher count first, ties alphabetical."""
    count = Counter(words)
    
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    result = []
    for _ in range(k):
        if heap:
            freq, word = heapq.heappop(heap)
            result.append(word)
    return result

   


def main():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(f"top_k_frequent({words}, 2) = {top_k_frequent(words, 2)}")


if __name__ == "__main__":
    main()