def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    while start <= stop: #while loop that counts from start to stop
        print(start) #prints nums until stop
        start = start + 1  #adds 1 to start

count_up(5, 7)        
