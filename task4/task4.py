import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        nums = [int(line.strip()) for line in f]

    print(min_moves(nums))
