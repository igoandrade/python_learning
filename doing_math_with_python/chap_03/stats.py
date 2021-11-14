"""
Calculating the median
"""
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        # convert to integer, match position
        m = int(m) - 1
        median = numbers(m)
    return median

"""
Calculating the mode
"""
from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


""""
Calculating the mode when the list of numbers may have multiple modes
"""
def calculate_mode2(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

"""
Frequency table for a list of numbers
"""
from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print(f"{number[0]:3d}\t{number[1]:3d}")


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print(f"Median donation over the last {N} days is {median}.")

    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)
    print(f"The mode of the list of numbers is: {mode}.")

    scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
    modes = calculate_mode2(scores)
    print(f"The mode(s) of the list of numbers are:")
    for mode in modes:
        print(mode)

    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)