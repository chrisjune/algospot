class Solution:
    def jump(self, nums) -> int:
        left = 0
        count = 0
        while True:
            target_list = nums[left:]
            if len(target_list) == 1:
                break
            count += 1

            first = target_list[0]
            maxvalue = (-1, -1)
            for i in range(1, min(first + 1, len(target_list))):
                val = i + target_list[i]
                if i >= len(target_list) - 1:
                    maxvalue = (i, val)
                    break

                if maxvalue[1] <= val:
                    maxvalue = (i, val)

            idx = maxvalue[0]
            left += idx
        return count


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([0]) == 0
    assert Solution().jump([1, 2]) == 1
    assert Solution().jump([2, 1]) == 1
    assert Solution().jump([3, 2, 1]) == 1
    assert Solution().jump([2, 3, 1]) == 1
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
    assert Solution().jump([1, 1, 1, 1, 1, 1]) == 5
    assert Solution().jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == 3
