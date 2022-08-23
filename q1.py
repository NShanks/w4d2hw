words = ['this' , 'is', 'a', 'sentence', '.']

words2 = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '10']

def swap(x):
     # Creating pointers for the list below:
    left = 0
    right = len(x) - 1
    while left <= right:
        x[left], x[right] = x[right],x[left]
        left += 1
        right -= 1
    return x

print(swap(words))
print(swap(words2))