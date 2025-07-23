def count_freq(lst1):
    freq = {}
    for item in lst1:
        if item in freq:
            freq[item] += 1 
        else:
            freq[item] = 1 
    return freq
l1=['Ayush', 19, 'Chicago', 'Ayush', 21, 19]
print(count_freq(l1))