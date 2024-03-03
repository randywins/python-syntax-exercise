def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    total = 0 #initializes the total

    for num in nums: #for loop for list of nums
        total = total + num #increments and adds the nums in the list

    return total   #returns new total

print("sum_nums returned", sum_nums([1, 2, 3, 4])) #adds 1 + 2 + 3 + 4 = 10
