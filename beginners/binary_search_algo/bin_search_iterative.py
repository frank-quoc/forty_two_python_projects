import random

def bin_search_iterative(random_list, target):
    """Uses the iterative version of binary search to find the index of target if it exists."""
    lower = 0
    upper = len(random_list) - 1
    while lower < upper:
        mid = (lower + upper) // 2
        if random_list[mid] == target:
            return mid
        elif random_list[mid] > lower:
            lower = mid + 1
        else:
            upper = mid - 1
    return - 1

if __name__ == '__main__':
    target = int(input("Enter a number to find in a random list of numbers from 0 to 100: "))
    lst = sorted(random.sample(range(0, 101), 50))
    print(bin_search_iterative(lst, target))
