# Problem

Given an integer array 'nums', move all 0's to the end of it while maintaining the relative order of the non-zero elements. Do this in-place without making a copy of the array.

---

## Approach

We use two pointers:
- `left` tracks where the next non-zero element should go.
- `right` scans through the array.
If nums[right] != 0, we swap nums[left] and nums[right], then increment left.
Finally, all non-zero elements are at the beginning, and zeros are pushed to the end.

---

## Code

```python
def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
```