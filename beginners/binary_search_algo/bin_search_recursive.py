import random

def bin_search_recursive(random_list, target, lower=0, upper=None):
    if upper is None:
        upper = len(random_list) - 1
    if lower > upper:
        return -1
    
    mid = (lower + upper) // 2
    if random_list[mid] == target:
        return mid
    elif random_list[mid] > target:
        bin_search_recursive(random_list, target, lower, mid-1)
    else:
        bin_search_recursive(random_list, target, mid+1, upper)

if __name__ == '__main__':
    target = int(input("Enter a number to search the list for: "))
    lst = sorted(random.sample(range(0, 101), 25))
    print(bin_search_recursive(lst, target))