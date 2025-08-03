def jump(nums):
    jumps = 0
    max_jump = 0
    curr_end = 0
    for i in range(len(nums) - 1):
        max_jump = max(max_jump, i + nums[i])

        if i == curr_end:
            jumps += 1
            curr_end = max_jump

            if curr_end >= len(nums) - 1:
                break

    return jumps
