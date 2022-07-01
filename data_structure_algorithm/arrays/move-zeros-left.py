# Move Zeros left
def movezerosleft(nums):
    read_index = len(nums)-1
    write_index = len(nums)-1
    while read_index >= 0:
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index -= 1
        read_index -= 1
    while write_index >= 0:
        nums[write_index] = 0
        write_index -= 1
    return nums

nums = [1,56,4,3,0,8,90,6,0,4,5,0]
print(movezerosleft(nums))

# move zeros to the end
def movezerosend(nums):
    read_index = 0
    write_index = 0
    while read_index <= len(nums)-1:
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index += 1
        read_index += 1
    while write_index <= len(nums)-1:
        nums[write_index] = 0
        write_index += 1
    return nums

nums = [1,56,4,3,0,8,90,6,0,4,5,0]
print(movezerosend(nums))