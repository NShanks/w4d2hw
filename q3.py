nums_list = [10,23,45,70,11,15]
target = 70

# If number is not present return -1
def searcher(x):
    for i in x:
        if i == target:
            print(target)
            return target
    print(-1)
    return -1
        
searcher(nums_list)

# Time complexity is O(N) because it takes N steps for N elements in the array. In the worst case scenario, 
# it has to loop through every element in the array once but never more than once.
# Space complexity is O(1)