a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
tracker = {}
def wordCount(x):
    for word in x.lower().split():
        if word in tracker:
            tracker[word] += 1
            # add +1 to count value to the key of 'word'
        else:
            tracker[word] = 1
            # add 'word' to the dictionary as a key
    return tracker
# print(wordCount(a_text))
wordCount(a_text)
sorted_string = dict(sorted(tracker.items(), key=lambda item:item[0]))
print(sorted_string)
