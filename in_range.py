def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE

    for num in nums: #for loop for range
        if num >= lowest and num <= highest: #conditional that finds lowest and highest
            print(f"{num} fits") #prints nums that fit in the range

#nums in range are outside of [] and nums to find are inside of the brackets


in_range([10, 20, 30, 40, 50], 15, 30) #looks to see which numbers in brackets fits inside of 15 to 30

