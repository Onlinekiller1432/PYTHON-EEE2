# 24)Write a program that asksthe user for a word and finds all the smaller words that can be made from the letters of that word. The number of occurrences of a letter in asmaller word can’t exceed the number of occurrences of the letter in the user’s word.
wd=input("enter word: ")
from itertools import permutations
for i in range(2,len(wd)):
    for p in permutations(wd,i):
        print(' '.join(p),end=" ")
    print()
