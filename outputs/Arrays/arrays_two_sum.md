# Problem

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

---

## Approach

Use a hashmap to store the difference and index while iterating through the array.

---

## Code

```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
```