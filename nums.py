def find_missing_nums(nums):
    number = input()
    nums = number.split()
    nums = list(map(int, nums))
    nums.sort()
    number = nums[-1]
    spasite = [x for x in range(1, number + 1)]
    missing = []

    for value in spasite:
        if value in nums:
            continue
        else:
            missing.append(value)
    return missing

print(find_missing_nums(nums))
