from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices (i, j), i < j, with nums[i] + nums[j] == target, else None."""
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx
    return None


def main():
    nums, target = [2, 7, 11, 15], 9
    print(f"two_sum({nums}, {target}) = {two_sum(nums, target)}")


if __name__ == "__main__":
    main()