#Write code to take a string like "data engineer" and return a dictionary of character counts:
#{"d":1, "a":2, "t":1, " ":1, "e":2, "n":2, "g":1, "i":1, "r":1}

#a = "data engineer"
#dict = {}
#for i in range(len(a)):
#    if a[i] in dict:
#        dict[a[i]] = dict[a[i]]+1
#    else:
#        dict[a[i]] = 1
#print(dict)

# 2nd Method

# def count_char(text):
#     dict = {}
#     for i in text:
#         dict[i] = dict.get(i,0)+1
#     print(dict.get('d'))
#     return dict
# s = "data engineer"
# print(count_char(s))

from collections import Counter

s = 'data engineer'
count  = dict(Counter(s))
print(count)