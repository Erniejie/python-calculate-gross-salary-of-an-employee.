#Iterators and Iterables
#Computer Programming Tutor,April 14,2021

import itertools as ite

def permutationsList(it1,lent):
    return ite.permutations(it1,lent)

#List
output = permutationsList(["A","B","C"],3)
print("\nIterator to get numbers of permutations of elements:")
for k in output:
    print(k)

#String

output = permutationsList("God",2)
print("\nIterator to get numbers of permutations of elements:")
for k in output:
    print(k)
